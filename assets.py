import networkx as nx
import random
import numpy as np

def create_network_data():
    # Create nodes
    num_nodes = 50
    groups = ['User', 'AI Agent', 'Investor']
    nodes = [
        (i, {
            'name': f'Node {i}',
            'group': random.choice(groups),
            'size': random.randint(5, 20)
        }) for i in range(num_nodes)
    ]
    
    # Create edges
    num_edges = 100
    edges = [
        (random.randint(0, num_nodes-1), random.randint(0, num_nodes-1))
        for _ in range(num_edges)
    ]
    
    # Create network graph
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    
    # Get node positions
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    
    # Create node data
    node_data = [
        {
            'x': pos[node][0],
            'y': pos[node][1],
            'color': {'User': '#FF9900', 'AI Agent': '#00BFFF', 'Investor': '#32CD32'}[G.nodes[node]['group']],
            'size': G.nodes[node]['size'] * 10,
            'group': G.nodes[node]['group']
        } for node in G.nodes()
    ]
    
    # Create edge data
    edge_data = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_data.extend([
            {'x': x0, 'y': y0},
            {'x': x1, 'y': y1},
            {'x': None, 'y': None}  # This creates a break in the line
        ])
    
    return {'nodes': node_data, 'edges': edge_data}

def create_similarity_data():
    # Generate random similarity data
    num_investors = 10
    similarity_matrix = np.random.rand(num_investors, num_investors)
    
    # Make the matrix symmetric
    similarity_matrix = (similarity_matrix + similarity_matrix.T) / 2
    
    # Set diagonal to 1 (each investor is 100% similar to themselves)
    np.fill_diagonal(similarity_matrix, 1)
    
    # Ensure similarity values are between 0 and 1
    similarity_matrix = np.clip(similarity_matrix, 0, 1)
    
    return similarity_matrix.tolist()  # Convert to list for JSON serialization

def get_suggestions(query=None):
    headers = [
        'Big-eyed frog',
        'GreenYield Eco-friendly yield farming token ecosystem',
        'purring cheerful cat',
        'NexusAI AI-powered cross-chain liquidity protocol',
        'CryptoShield Decentralized insurance marketplace for cryptocurrencies',
        'FutureSight (FST) AI-driven decentralized prediction market platform'
    ]

    descriptions = [
        'The big-eyed frog meme token is a cryptocurrency inspired by the popular internet meme featuring exaggerated, wide-eyed amphibians. Like many meme coins, it likely emerged from online communities and social media trends. These tokens often experience rapid price fluctuations driven by social media hype and speculative trading rather than fundamental value',
        'GreenYield (GYD) is a decentralized finance token designed to promote sustainable farming practices while offering attractive yields to investors. Built on the Ethereum blockchain, GreenYield utilizes a unique consensus mechanism called Proof-of-Sustainability (PoS) that rewards token holders for supporting eco-friendly agricultural projects.',
        'A smiling cat meme token is a cryptocurrency or digital asset inspired by the popular internet culture of cat memes. These tokens often feature iconic images of grinning, happy cats that have gone viral online. They blend the whimsical nature of internet humor with the world of blockchain technology and decentralized fi',
        'NexusAI (NAI) is an innovative decentralized finance platform that leverages artificial intelligence to optimize cross-chain liquidity and trading. Built on a custom blockchain that allows for seamless interoperability with major networks like Ethereum, Binance Smart Chain, and Solana, NexusAI aims to revolutionize the way users interact with multiple DeFi ecosystems.',
        'CryptoShield (CSH) is a decentralized finance platform designed to provide comprehensive insurance solutions for the cryptocurrency ecosystem. Built on the Polygon network for its scalability and low transaction costs, CryptoShield aims to address the growing need for risk management tools in the volatile world of digital assets.',
        'FutureSight (FST) is an innovative decentralized finance platform that combines artificial intelligence with prediction markets to create a powerful forecasting ecosystem. Built on the Avalanche network for its high throughput and quick finality, FutureSight aims to revolutionize how predictions are made and traded in the crypto space and beyond.'
        ]

    return headers, descriptions

def get_conv(i):
    convs = [[
        ("User A", {
            "Existing Coins": ["ETH", "GYT"],
            "Risk Level": "Prefers stable investments with minimal risk of loss.",
            "Trading Frequency": "Trades infrequently, possibly less than once a month.",
            "Average Trade Size": "Trades typically involve small amounts, often below $100."
        }),
        ("dHive", "Given the user's cautious approach towards investments, it might be interesting to explore the potential of newer, yet less risky meme tokens. One option could be the Big-eyed frog meme token."),
        ("User B", {
            "Existing Coins": ["BTC", "ETH", "GYT"],
            "Risk Level": "Willing to accept moderate risks for the possibility of higher returns.",
            "Trading Frequency": "Trades regularly, several times a week.",
            "Average Trade Size": "Trades involve moderate amounts, between $100 and $1,000."
        }),
        ("My Agent", "Considering both users' profiles, User B's willingness to accept moderate risks and active trading habits could complement User A's cautious approach. User A might find Big-eyed frog's growing popularity and potential for stable gains interesting."),
        ("dHive", "Absolutely. The Big-eyed frog meme token offers a unique investment avenue with potential for high engagement due to its internet meme origins, which aligns with User B's moderate risk appetite and regular trading frequency."),
        ("My Agent", "Agreed. By combining their strategies, they could achieve a diversified portfolio that balances risk and potential rewards. The meme token market, although volatile, offers significant growth opportunities which could be monitored by User B's active trading habits."),
        ("dHive", "Therefore, our recommendation would be to jointly invest in the Big-eyed frog meme token. User B's active trading could help manage and optimize the investment, while User A could benefit from the growing trend and potential stability over time."),
        ("My Agent", "In summary, a joint investment in the Big-eyed frog meme token appears to be a promising choice. This strategy allows both users to align their investment goals while taking advantage of the popularity and potential stability of this meme-inspired cryptocurrency.")
    ],
    [
        ("User A", {
            "Existing Coins": ["BTC", "ETH", "GYT"],
            "Risk Level": "Prefers stable investments with high risk of loss.",
            "Trading Frequency": "Trades infrequently, possibly less than once a month.",
            "Average Trade Size": "Trades typically involve small amounts, often below $100."
        }),
        ("dHive", "Given the user's interest in eco-friendly investments like GYT and the current market trend towards sustainable finance, it seems prudent to consider further investments in GreenYield."),
        ("User B", {
            "Existing Coins": ["BTC", "ETH", "GYT"],
            "Risk Level": "Willing to accept moderate risks for the possibility of higher returns.",
            "Trading Frequency": "Trades regularly, several times a week.",
            "Average Trade Size": "Trades involve moderate amounts, between $100 and $1,000."
        }),
        ("My Agent", "Considering both users' profiles, User B's moderate risk tolerance and more frequent trading pattern can complement User A's cautious approach. User A's interest in stable investments might find a balanced growth opportunity through GreenYield."),
        ("dHive", "Absolutely. GreenYield presents an eco-friendly investment avenue with moderate risk, aligning with both users' interests. User B's trading habits could help monitor and manage the investment, leveraging the stability and eco-focus that User A prefers."),
        ("My Agent", "Agreed. By combining their strategies, they could achieve a diversified portfolio that balances risk and stability while capitalizing on the growing trend in sustainable investments."),
        ("dHive", "Therefore, our recommendation would be to jointly invest in GreenYield, leveraging User B's more active trading to manage and optimize the investment while maintaining a focus on the stability that User A values."),
        ("My Agent", "In summary, a joint investment in GreenYield appears to be the optimal choice. This strategy allows both users to align their investment goals while taking advantage of the eco-friendly and stable nature of GYT.")
    ]]
    return convs[i]
