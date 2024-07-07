import numpy as np
from datetime import datetime
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
import json
import os
from minisom import MiniSom
from sklearn.preprocessing import StandardScaler

SYMBOLS = ["USDT", "USDC", "WETH", "BTC", "ETH"]

def categorize_trading_frequency(avg_diff):
    if avg_diff < 60:
        return 0  # trades on average every less than a minute
    elif avg_diff < 3600:
        return 1  # trades on average every less than an hour
    elif avg_diff < 86400:
        return 2  # trades on average every less than a day
    elif avg_diff < 604800:
        return 3  # trades on average every less than a week
    elif avg_diff < 2592000:
        return 4  # trades on average every less than a month
    else:
        return 5

def categorize_trade_size(avg_size):
    if avg_size < 100:
        return 0  # average trade size less than $100
    elif avg_size < 1000:
        return 1  # average trade size less than $1000
    elif avg_size < 10000:
        return 2  # average trade size less than $10000
    elif avg_size < 50000:
        return 3  # average trade size less than $50000
    else:
        return 4  # average trade size more than $50000

def extract_features(transactions):
    # Sort transactions by timestamp
    transactions.sort(key=lambda x: x["timestamp"])

    # Extract timestamps, values, and symbols
    timestamps = [t["timestamp"] for t in transactions]
    values = [t["value"] for t in transactions]
    symbols = [t["symbol"] for t in transactions]
    
    # Risk level: proportion of trades in stablecoins vs. volatile coins
    risk_level = sum(1 for t in transactions if "Stablecoins" in t["name"]) / len(transactions)
    
    # Trading frequency: average difference between timestamps
    if len(timestamps) > 1:
        timestamp_diffs = [j-i for i, j in zip(timestamps[:-1], timestamps[1:])]
        trading_frequency = sum(timestamp_diffs) / len(timestamp_diffs)
        trading_frequency = categorize_trading_frequency(trading_frequency)
    else:
        trading_frequency = 5
    
    # Average trade size
    average_trade_size = sum(values) / len(transactions)
    average_trade_size = categorize_trade_size(average_trade_size)
    
    # Preference for certain assets: normalized count of trades per asset
    symbol_counts = Counter(symbols)
    normalized_symbol_counts = [symbol_counts[symbol] / len(transactions) for symbol in SYMBOLS]
    
    # Combine all features into a single vector
    features = [
        risk_level, trading_frequency,
        average_trade_size
    ] + normalized_symbol_counts
    
    return np.array(features)

def load_user_data(directory):
    user_data = {}
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            user_id = filename.split(".")[0]
            with open(os.path.join(directory, filename), 'r') as file:
                transactions = json.load(file)
                user_data[user_id] = extract_features(transactions)
    return user_data

def find_closest_users(target_user_id, user_data, top_k=5):
    target_vector = user_data[target_user_id]
    similarities = []
    
    for user_id, feature_vector in user_data.items():
        if user_id != target_user_id:
            similarity = cosine_similarity([target_vector], [feature_vector])[0][0]
            similarities.append((user_id, similarity))
    
    # Sort by similarity in descending order
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    return similarities[:top_k]

def diff(cluster1, cluster2):
    return abs(cluster1[0]-cluster2[0]) + abs(cluster1[1]-cluster2[1])

if __name__ == "__main__":

    # Find closest users to a specific user
    target_user_id = "user_1"  # Change to the user ID you want to check
    data_directory = "data"
    
    # Load user data
    user_data = load_user_data(data_directory)
    closest_users = find_closest_users(target_user_id, user_data)

    print(f"Closest users to {target_user_id}:")
    for user_id, similarity in closest_users:
        print(f"{user_id} with similarity score: {similarity:.4f}")
    
    scaler = StandardScaler()
    users = []
    embeddings = []
    for ind, (user, emb) in enumerate(user_data.items()):
        users.append(user)
        embeddings.append(emb)
    embeddings = np.stack(embeddings)
    embeddings = scaler.fit_transform(embeddings)

    # Initialize and train the SOM
    som = MiniSom(x=10, y=5, input_len=embeddings.shape[1], sigma=0.5, learning_rate=0.5)
    som.random_weights_init(embeddings)
    som.train_random(embeddings, num_iteration=100)

    # Get the winning nodes (clusters)
    clusters = np.array([som.winner(x) for x in embeddings])
    #print(clusters)

    target_cluster = clusters[users.index(target_user_id)]

    user_cluster_diff = [(user, cluster, diff(cluster, target_cluster)) for user, cluster in zip(users, clusters)]
    user_cluster_diff_sorted = sorted(user_cluster_diff, key=lambda x: x[2])

    # Print users in the order of ascending differences
    for user, cluster, difference in user_cluster_diff_sorted:
        print(user, cluster, difference)
    
    print("")
    for user_id, similarity in closest_users:
        print(user_cluster_diff[users.index(user_id)])
