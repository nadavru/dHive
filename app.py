# # import streamlit as st
# # import pandas as pd
# # import random
# # import time
# # from streamlit_extras.colored_header import colored_header
# # from streamlit_extras.metric_cards import style_metric_cards
# # import assets

# # # Initialize session state
# # if "init" not in st.session_state:
# #     st.session_state.init = True
# #     st.session_state.suggestions_name, st.session_state.suggestions_desc = assets.get_suggestions()
# #     st.session_state.clicked_suggestion = None
# #     st.session_state.show_urgent = False
# #     st.session_state.start_time = time.time()
    
# #     base_values = [random.uniform(0.0, 0.5) for _ in range(6)]
# #     st.session_state.progress_values = {
# #                                             f'{type}_{i}': abs(random.uniform(base - 0.1, base + 0.1))
# #                                             for i, base in enumerate(base_values)
# #                                             for type in ['bonding', 'king']
# #                                         }

# # # Page config
# # st.set_page_config(page_title="dHive - AI-Driven Social Investment", layout="wide", initial_sidebar_state="expanded")

# # # Custom CSS
# # st.markdown("""
# # <style>
# #     .main .block-container {padding-top: 2rem;}
# #     .stProgress > div > div > div > div {background-color: #FF9900;}
# #     .stProgress {height: 20px;}
# #     .css-1kyxreq {justify-content: center;}
# #     .css-10trblm {color: #FF9900;}
# #     .suggestion-button {
# #         background-color: #1E1E1E;
# #         color: white;
# #         border: 1px solid #FF9900;
# #         border-radius: 5px;
# #         padding: 10px;
# #         margin-bottom: 10px;
# #         cursor: pointer;
# #         transition: background-color 0.3s;
# #     }
# #     .suggestion-button:hover {background-color: #FF9900; color: #1E1E1E;}
# #     .css-1kyxreq {background-color: #1E1E1E; padding: 20px; border-radius: 10px;}
# # </style>
# # """, unsafe_allow_html=True)

# # # Helper functions
# # def handle_click(suggestion_number):
# #     st.session_state.clicked_suggestion = suggestion_number if st.session_state.clicked_suggestion != suggestion_number else None

# # @st.cache_data(ttl=1)
# # def get_progress_values():
# #     for i in range(6):
# #         for type in ['bonding', 'king']:
# #             if random.uniform(0.0, 1.0) > 0.8:
# #                 increment = random.uniform(0.0, 0.01)
# #                 st.session_state.progress_values[f'{type}_{i}'] = min(st.session_state.progress_values[f'{type}_{i}'] + increment, 1.0) 
# #     return st.session_state.progress_values

# # def create_network_visualization():
# #     nodes = [
# #         {'name': 'User', 'size': 20, 'group': 1},
# #         {'name': 'AI Agent 1', 'size': 15, 'group': 2},
# #         {'name': 'AI Agent 2', 'size': 15, 'group': 2},
# #         {'name': 'AI Agent 3', 'size': 15, 'group': 2},
# #         {'name': 'Investor 1', 'size': 10, 'group': 3},
# #         {'name': 'Investor 2', 'size': 10, 'group': 3},
# #         {'name': 'Investor 3', 'size': 10, 'group': 3},
# #     ]
    
# #     df = pd.DataFrame(nodes)
# #     df['x'] = [random.uniform(0, 100) for _ in range(len(df))]
# #     df['y'] = [random.uniform(0, 100) for _ in range(len(df))]
    
# #     st.subheader("AI-Driven Social Investment Network")
# #     chart = st.scatter_chart(
# #         df,
# #         x='x',
# #         y='y',
# #         size='size',
# #         color='group',
# #         height=400,
# #     )
    
# #     st.caption("Network Nodes:")
# #     for _, node in df.iterrows():
# #         st.text(f"{node['name']} (Group {node['group']})")
    
# #     return chart

# # # Main layout
# # logo_col, title_col = st.columns([1, 4])
# # with logo_col:
# #     st.image("logo_no_bg.png", width=100)
# # with title_col:
# #     colored_header(label="dHive - AI-Driven Social Investment", description="Personalized investment matching based on shared values", color_name="orange-70")

# # # Get updated progress values
# # progress_values = get_progress_values()

# # # Sidebar
# # with st.sidebar:
# #     st.subheader("Investment Opportunities")
    
# #     # Check if it's time to show the urgent suggestion (after 30 seconds)
# #     if time.time() - st.session_state.start_time > 5:
# #         st.session_state.show_urgent = True
    
    
# #     # Display suggestions
# #     suggestion_range = range(6) if st.session_state.show_urgent else range(1, 6)
# #     for i in suggestion_range:
# #         if i == 0 and st.session_state.show_urgent:
# #             st.markdown("### ❗️ New Urgent Suggestion!")
        
# #         if st.button(f"{'❗️' if i == 0 else ''}{st.session_state.suggestions_name[i]}", key=f"suggestion_{i}", on_click=handle_click, args=(i,), use_container_width=True):
# #             pass
        
# #         col1, col2 = st.columns(2)
# #         with col1:
# #             st.markdown("##### Bonding Curve")
# #             st.progress(progress_values[f'bonding_{i}'])
# #         with col2:
# #             st.markdown("##### Private Sale")
# #             st.progress(progress_values[f'king_{i}'])
        
# #         st.markdown("---")
    
# #     st.markdown("### Dethrone the King")
# #     st.metric("Current King's Market Cap", "$28,404")
    
# #     st.markdown("### Top Holders")
# #     holder_data = {
# #         "Holder": ["4C5KNe 🏦", "8vwwCL", "DMxYya", "HQJqjZ 💡", "3R526g", "3kSyhx", "6pkPW9"],
# #         "Percentage": [49.03, 2.56, 2.51, 2.50, 1.59, 1.03, 1.01]
# #     }
# #     df = pd.DataFrame(holder_data)
# #     st.dataframe(df, hide_index=True, use_container_width=True)

# # # Main content
# # if st.session_state.clicked_suggestion is not None:
# #     st.subheader(st.session_state.suggestions_name[st.session_state.clicked_suggestion])
# #     st.write(st.session_state.suggestions_desc[st.session_state.clicked_suggestion])
    
# #     col1, col2, col3 = st.columns(3)
# #     col1.metric("AI Confidence", f"{random.randint(70, 99)}%")
# #     col2.metric("Potential ROI", f"{random.randint(5, 50)}%")
# #     col3.metric("Risk Level", f"{random.choice(['Low', 'Medium', 'High'])}")
# #     style_metric_cards(background_color="#e8e3e3", border_left_color="#FF9900")
    
# #     create_network_visualization()
# # else:
# #     st.write("""
# #     Welcome to dHive, an AI-driven algorithm for personalized social investment. Our platform matches people based on shared values, trading activity, and risk tolerance, providing clear and explainable results through our on-chain multi-agent system.
    
# #     Key Features:
# #     - Passive Deal Flow
# #     - LLM-Based Profiles
# #     - Naptha AI Agents
# #     - Generative Social Recommendations
# #     - On-Chain Infrastructure
    
# #     Explore investment opportunities in the sidebar and dive into a new era of community-driven, AI-powered investing!
# #     """)
    
# #     create_network_visualization()

# # # Force a rerun every second to update the progress bars
# # time.sleep(1)
# # st.rerun()

# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import random
# import time
# import networkx as nx
# from streamlit_extras.colored_header import colored_header
# from streamlit_extras.metric_cards import style_metric_cards
# import assets

# # Initialize session state
# if "init" not in st.session_state:
#     st.session_state.init = True
#     st.session_state.suggestions_name, st.session_state.suggestions_desc = assets.get_suggestions()
#     st.session_state.clicked_suggestion = None
#     st.session_state.show_urgent = False
#     st.session_state.start_time = time.time()
#     st.session_state.selected_cluster = None
#     st.session_state.show_recommendation = False
    
#     base_values = [random.uniform(0.0, 0.5) for _ in range(6)]
#     st.session_state.progress_values = {
#         f'{type}_{i}': abs(random.uniform(base - 0.1, base + 0.1))
#         for i, base in enumerate(base_values)
#         for type in ['bonding', 'king']
#     }

# # Page config
# st.set_page_config(page_title="dHive - AI-Driven Social Investment", layout="wide", initial_sidebar_state="expanded")

# # Custom CSS
# st.markdown("""
# <style>
#     .main .block-container {padding-top: 2rem;}
#     .stProgress > div > div > div > div {background-color: #FF9900;}
#     .stProgress {height: 20px;}
#     .css-1kyxreq {justify-content: center;}
#     .css-10trblm {color: #FF9900;}
#     .suggestion-button {
#         background-color: #1E1E1E;
#         color: white;
#         border: 1px solid #FF9900;
#         border-radius: 5px;
#         padding: 10px;
#         margin-bottom: 10px;
#         cursor: pointer;
#         transition: background-color 0.3s;
#     }
#     .suggestion-button:hover {background-color: #FF9900; color: #1E1E1E;}
#     .css-1kyxreq {background-color: #1E1E1E; padding: 20px; border-radius: 10px;}
#     .css-1v0mbdj {border-color: #FF9900;}
#     .st-bw {border-width: 2px;}
#     .stPlotlyChart {background-color: #2b2b2b; border-radius: 10px; padding: 10px;}
# </style>
# """, unsafe_allow_html=True)

# # Helper functions
# def handle_click(suggestion_number):
#     st.session_state.clicked_suggestion = suggestion_number if st.session_state.clicked_suggestion != suggestion_number else None

# @st.cache_data(ttl=1)
# def get_progress_values():
#     for i in range(6):
#         for type in ['bonding', 'king']:
#             if random.uniform(0.0, 1.0) > 0.8:
#                 increment = random.uniform(0.0, 0.01)
#                 st.session_state.progress_values[f'{type}_{i}'] = min(st.session_state.progress_values[f'{type}_{i}'] + increment, 1.0) 
#     return st.session_state.progress_values

# def create_network_visualization():
#     # Create nodes
#     num_nodes = 50
#     groups = ['User', 'AI Agent', 'Investor']
#     nodes = [
#         (i, {
#             'name': f'Node {i}',
#             'group': random.choice(groups),
#             'size': random.randint(5, 20)
#         }) for i in range(num_nodes)
#     ]
    
#     # Create edges
#     num_edges = 100
#     edges = [
#         (random.randint(0, num_nodes-1), random.randint(0, num_nodes-1))
#         for _ in range(num_edges)
#     ]
    
#     # Create network graph
#     G = nx.Graph()
#     G.add_nodes_from(nodes)
#     G.add_edges_from(edges)
    
#     # Get node positions
#     pos = nx.spring_layout(G)
    
#     # Create node data
#     node_data = [
#         {
#             'x': pos[node][0],
#             'y': pos[node][1],
#             'color': {'User': '#FF9900', 'AI Agent': '#00BFFF', 'Investor': '#32CD32'}[G.nodes[node]['group']],
#             'size': G.nodes[node]['size'] * 10,
#             'group': G.nodes[node]['group']
#         } for node in G.nodes()
#     ]
    
#     # Create edge data
#     edge_data = []
#     for edge in G.edges():
#         x0, y0 = pos[edge[0]]
#         x1, y1 = pos[edge[1]]
#         edge_data.extend([
#             {'x': x0, 'y': y0},
#             {'x': x1, 'y': y1},
#             {'x': None, 'y': None}  # This creates a break in the line
#         ])
    
#     # Plot using Streamlit's native chart
#     st.subheader("Investment Network")
#     chart = st.vega_lite_chart({
#         'width': 600,
#         'height': 400,
#         'layer': [
#             {
#                 'data': {'values': edge_data},
#                 'mark': {'type': 'line', 'color': '#888', 'opacity': 0.5},
#                 'encoding': {
#                     'x': {'field': 'x', 'type': 'quantitative'},
#                     'y': {'field': 'y', 'type': 'quantitative'}
#                 }
#             },
#             {
#                 'data': {'values': node_data},
#                 'mark': 'circle',
#                 'encoding': {
#                     'x': {'field': 'x', 'type': 'quantitative'},
#                     'y': {'field': 'y', 'type': 'quantitative'},
#                     'size': {'field': 'size', 'type': 'quantitative'},
#                     'color': {'field': 'color', 'type': 'nominal', 'scale': None},
#                     'tooltip': ['group']
#                 }
#             }
#         ]
#     }, use_container_width=True)
    
#     return chart

# def create_similarity_heatmap():
#     # Generate random similarity data
#     similarity_matrix = np.random.rand(10, 10)
#     np.fill_diagonal(similarity_matrix, 1)
    
#     # Create heatmap
#     fig = px.imshow(similarity_matrix,
#                     labels=dict(x="Investors", y="Investors", color="Similarity"),
#                     x=['Inv ' + str(i) for i in range(1, 11)],
#                     y=['Inv ' + str(i) for i in range(1, 11)],
#                     color_continuous_scale="Viridis")
    
#     fig.update_layout(
#         title="Investor Similarity Heatmap",
#         xaxis_title="Investors",
#         yaxis_title="Investors",
#         plot_bgcolor='rgba(0,0,0,0)',
#         paper_bgcolor='rgba(0,0,0,0)',
#     )
    
#     return fig

# # Main layout
# logo_col, title_col = st.columns([1, 4])
# with logo_col:
#     st.image("logo_no_bg.png", width=100)
# with title_col:
#     colored_header(label="dHive - AI-Driven Social Investment", description="Personalized investment matching based on shared values", color_name="orange-70")

# # Get updated progress values
# progress_values = get_progress_values()

# # Sidebar
# with st.sidebar:
#     st.subheader("User Profile")
#     st.text_input("Wallet Address", value="0x1234...5678", disabled=True)
#     st.slider("Risk Tolerance", min_value=1, max_value=10, value=5)
#     st.multiselect("Investment Interests", ["DeFi", "NFTs", "GameFi", "Web3", "Metaverse"], default=["DeFi", "Web3"])
    
#     st.subheader("AI-Driven Insights")
#     st.metric("AI Confidence Score", "87%", delta="5%")
#     st.metric("Portfolio Health", "Good", delta="Stable")
    
#     if st.button("Generate Recommendations"):
#         st.session_state.show_recommendation = True

#     st.subheader("Investment Opportunities")
    
#     # Check if it's time to show the urgent suggestion (after 30 seconds)
#     if time.time() - st.session_state.start_time > 5:
#         st.session_state.show_urgent = True
    
#     # Display suggestions
#     suggestion_range = range(6) if st.session_state.show_urgent else range(1, 6)
#     for i in suggestion_range:
#         if i == 0 and st.session_state.show_urgent:
#             st.markdown("### ❗️ New Urgent Suggestion!")
        
#         if st.button(f"{'❗️' if i == 0 else ''}{st.session_state.suggestions_name[i]}", key=f"suggestion_{i}", on_click=handle_click, args=(i,), use_container_width=True):
#             pass
        
#         col1, col2 = st.columns(2)
#         with col1:
#             st.markdown("##### Bonding Curve")
#             st.progress(progress_values[f'bonding_{i}'])
#         with col2:
#             st.markdown("##### Private Sale")
#             st.progress(progress_values[f'king_{i}'])
        
#         st.markdown("---")
    
#     st.markdown("### Dethrone the King")
#     st.metric("Current King's Market Cap", "$28,404")
    
#     st.markdown("### Top Holders")
#     holder_data = {
#         "Holder": ["4C5KNe 🏦", "8vwwCL", "DMxYya", "HQJqjZ 💡", "3R526g", "3kSyhx", "6pkPW9"],
#         "Percentage": [49.03, 2.56, 2.51, 2.50, 1.59, 1.03, 1.01]
#     }
#     df = pd.DataFrame(holder_data)
#     st.dataframe(df, hide_index=True, use_container_width=True)

# # Main content
# tab1, tab2, tab3 = st.tabs(["Dashboard", "Investor Clusters", "On-Chain Discussion"])

# with tab1:
#     col1, col2, col3 = st.columns(3)
#     col1.metric("Total Investments", "$12,450", delta="8%")
#     col2.metric("Active Deals", "3", delta="1")
#     col3.metric("Potential ROI", "22%", delta="3%")
#     style_metric_cards(background_color="#e8e3e3", border_left_color="#FF9900")
    
#     create_network_visualization()
    
#     if st.session_state.show_recommendation:
#         st.info("🚀 New Investment Opportunity: Web3 Social Platform Token Sale")
#         st.write("AI Recommendation: This opportunity aligns with your interest in Web3 and has a favorable risk-reward profile.")
#         if st.button("View Details"):
#             st.session_state.selected_cluster = "Web3 Enthusiasts"
    
#     if st.session_state.clicked_suggestion is not None:
#         st.subheader(st.session_state.suggestions_name[st.session_state.clicked_suggestion])
#         st.write(st.session_state.suggestions_desc[st.session_state.clicked_suggestion])
        
#         col1, col2, col3 = st.columns(3)
#         col1.metric("AI Confidence", f"{random.randint(70, 99)}%")
#         col2.metric("Potential ROI", f"{random.randint(5, 50)}%")
#         col3.metric("Risk Level", f"{random.choice(['Low', 'Medium', 'High'])}")
#         style_metric_cards(background_color="#e8e3e3", border_left_color="#FF9900")

# with tab2:
#     st.subheader("Investor Similarity")
#     similarity_fig = create_similarity_heatmap()
#     st.plotly_chart(similarity_fig, use_container_width=True)
    
#     st.subheader("Investor Clusters")
#     clusters = ["DeFi Experts", "NFT Collectors", "Web3 Enthusiasts", "GameFi Pioneers"]
#     selected_cluster = st.selectbox("Select a cluster to view", clusters)
    
#     if selected_cluster:
#         st.write(f"Investors in the {selected_cluster} cluster:")
#         df = pd.DataFrame({
#             "Investor": [f"Investor {i}" for i in range(1, 6)],
#             "Similarity Score": np.random.uniform(0.7, 0.99, 5),
#             "Common Investments": np.random.randint(1, 5, 5)
#         })
#         st.dataframe(df)

# with tab3:
#     st.subheader("On-Chain AI Agent Discussion")
#     if st.session_state.selected_cluster:
#         st.write(f"AI Agents are discussing investment opportunities for the {st.session_state.selected_cluster} cluster.")
        
#         for i in range(3):
#             with st.chat_message(f"AI Agent {i+1}"):
#                 st.write(f"Agent {i+1}: Based on the cluster's preferences and market trends, I propose we consider the following token: {random.choice(['$WEB3', '$DEFI', '$GAME', '$META'])}.")
        
#         if st.button("Generate Consensus Recommendation"):
#             with st.spinner("AI Agents are reaching a consensus..."):
#                 time.sleep(2)
#             st.success("Consensus Reached: Recommend $WEB3 token with 85% confidence.")
#     else:
#         st.write("Select a cluster in the 'Investor Clusters' tab to view AI agent discussions.")

# # Footer
# st.markdown("---")
# st.markdown("dHive - Empowering investors with AI-driven social recommendations and on-chain verification.")

# # Force a rerun every second to update the progress bars
# time.sleep(1)
# st.rerun()

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random
import time
import networkx as nx
from streamlit_extras.colored_header import colored_header
from streamlit_extras.metric_cards import style_metric_cards
import assets

def display_user_data(user_data, user_name):
    st.subheader(f"{user_name} Investment Data")
    for key, value in user_data.items():
        if isinstance(value, list):
            st.write(f"{key}: {', '.join(value)}")
        else:
            st.write(f"{key}: {value}")
    st.write("---")

# Initialize session state
if "init" not in st.session_state:
    st.session_state.init = True
    st.session_state.suggestions_name, st.session_state.suggestions_desc = assets.get_suggestions()
    st.session_state.clicked_suggestion = None
    st.session_state.show_urgent = False
    st.session_state.start_time = time.time()
    st.session_state.selected_cluster = None
    st.session_state.show_recommendation = False
    
    base_values = [random.uniform(0.2, 0.5) for _ in range(6)]
    st.session_state.progress_values = {
        f'{type}_{i}': abs(random.uniform(base - 0.1, base + 0.1))
        for i, base in enumerate(base_values)
        for type in ['bonding', 'king']
    }
    
    # Initialize static data
    st.session_state.network_data = assets.create_network_data()
    st.session_state.similarity_data = assets.create_similarity_data()

# Page config
st.set_page_config(page_title="dHive - AI-Driven Social Investment", layout="wide", initial_sidebar_state="expanded")

# Custom CSS
st.markdown("""
<style>
    .main .block-container {padding-top: 2rem;}
    .stProgress > div > div > div > div {background-color: #FF9900;}
    .stProgress {height: 20px;}
    .css-1kyxreq {justify-content: center;}
    .css-10trblm {color: #FF9900;}
    .suggestion-button {
        background-color: #1E1E1E;
        color: white;
        border: 1px solid #FF9900;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 10px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .suggestion-button:hover {background-color: #FF9900; color: #1E1E1E;}
    .css-1kyxreq {background-color: #1E1E1E; padding: 20px; border-radius: 10px;}
    .css-1v0mbdj {border-color: #FF9900;}
    .st-bw {border-width: 2px;}
    .stPlotlyChart {background-color: #2b2b2b; border-radius: 10px; padding: 10px;}
</style>
""", unsafe_allow_html=True)

# Helper functions
def handle_click(suggestion_number):
    st.session_state.clicked_suggestion = suggestion_number if st.session_state.clicked_suggestion != suggestion_number else None

@st.cache_data(ttl=1)
def get_progress_values():
    for i in range(6):
        for type in ['bonding', 'king']:
            if random.uniform(0.0, 1.0) > 0.8:
                increment = random.uniform(0.0, 0.01)
                st.session_state.progress_values[f'{type}_{i}'] = min(st.session_state.progress_values[f'{type}_{i}'] + increment, 1.0) 
    return st.session_state.progress_values

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
    pos = nx.spring_layout(G)
    
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

def create_network_visualization():
    network_data = st.session_state.network_data
    
    # Plot using Streamlit's native chart
    st.subheader("Investment Network Similarity")
    chart = st.vega_lite_chart({
        'width': 600,
        'height': 400,
        'layer': [
            {
                'data': {'values': network_data['edges']},
                'mark': {'type': 'line', 'color': '#888', 'opacity': 0.5},
                'encoding': {
                    'x': {'field': 'x', 'type': 'quantitative'},
                    'y': {'field': 'y', 'type': 'quantitative'}
                }
            },
            {
                'data': {'values': network_data['nodes']},
                'mark': 'circle',
                'encoding': {
                    'x': {'field': 'x', 'type': 'quantitative'},
                    'y': {'field': 'y', 'type': 'quantitative'},
                    'size': {'field': 'size', 'type': 'quantitative'},
                    'color': {'field': 'color', 'type': 'nominal', 'scale': None},
                    'tooltip': ['group']
                }
            }
        ]
    }, use_container_width=True)
    
    return chart

def create_similarity_data():
    # Generate random similarity data
    similarity_matrix = np.random.rand(10, 10)
    np.fill_diagonal(similarity_matrix, 1)
    return similarity_matrix


def create_similarity_heatmap():
    similarity_matrix = st.session_state.similarity_data
    
    # Create heatmap
    fig = px.imshow(similarity_matrix,
                    labels=dict(x="Investors", y="Investors", color="Similarity"),
                    x=['Inv ' + str(i) for i in range(1, 11)],
                    y=['Inv ' + str(i) for i in range(1, 11)],
                    color_continuous_scale="Viridis")
    
    fig.update_layout(
        title="Investor Similarity Heatmap",
        xaxis_title="Investors",
        yaxis_title="Investors",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    
    return fig

# Main layout
logo_col, title_col = st.columns([1, 4])
with logo_col:
    st.image("logo_no_bg.png", width=100)
with title_col:
    colored_header(label="dHive - AI-Driven Social Investment", description="Personalized investment matching based on shared values", color_name="orange-70")

# Get updated progress values
progress_values = get_progress_values()

# Sidebar
with st.sidebar:
    st.text_input("Wallet Address", value="0x1234...5678", disabled=True)
    # st.slider("Risk Tolerance", min_value=1, max_value=10, value=5)
    st.multiselect("Investment Category", ["DeFi", "NFTs", "GameFi", "Web3", "Metaverse"], default=["DeFi", "Web3"])
    
    # st.subheader("AI-Driven Insights")
    # st.metric("AI Confidence Score", "87%", delta="5%")
    # st.metric("Portfolio Health", "Good", delta="Stable")
    
    # if st.button("Generate Recommendations"):
    #     st.session_state.show_recommendation = True

    st.subheader("Investment Opportunities")
    
    # Check if it's time to show the urgent suggestion (after 5 seconds)
    if time.time() - st.session_state.start_time > 20:
        st.session_state.show_urgent = True
    
    # Display suggestions
    suggestion_range = range(6) if st.session_state.show_urgent else range(1, 6)
    for i in suggestion_range:
        if i == 0 and st.session_state.show_urgent:
            st.markdown("### ❗️ New Urgent Suggestion!")
        
        if st.button(f"{'❗️' if i == 0 else ''}{st.session_state.suggestions_name[i]}", key=f"suggestion_{i}", on_click=handle_click, args=(i,), use_container_width=True):
            pass
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### Bonding Curve")
            st.progress(progress_values[f'bonding_{i}'])
        with col2:
            st.markdown("##### Private Sale")
            st.progress(progress_values[f'king_{i}'])
        
        st.markdown("---")
    
    # st.markdown("### Network Market Cap")
    st.metric("Network Market Cap", "$28,404", delta="5%")
    
    st.markdown("### Top Holders")
    holder_data = {
        "Holder": ["4C5KNe 🏦", "8vwwCL", "DMxYya", "HQJqjZ 💡", "3R526g", "3kSyhx", "6pkPW9"],
        "Percentage": [49.03, 2.56, 2.51, 2.50, 1.59, 1.03, 1.01]
    }
    df = pd.DataFrame(holder_data)
    st.dataframe(df, hide_index=True, use_container_width=True)

# Main content
tab1, tab2, tab3 = st.tabs(["Dashboard", "Suggestion", "On-Chain Discussion"])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Investments", "$12,450", delta="8%")
    col2.metric("Active Deals", "3", delta="1")
    col3.metric("Potential ROI", "22%", delta="3%")
    style_metric_cards(background_color="#e8e3e3", border_left_color="#FF9900")
    
    create_network_visualization()
    
    if st.session_state.show_recommendation:
        st.info("🚀 New Investment Opportunity: Web3 Social Platform Token Sale")
        st.write("AI Recommendation: This opportunity aligns with your interest in Web3 and has a favorable risk-reward profile.")
        if st.button("View Details"):
            st.session_state.selected_cluster = "Web3 Enthusiasts"
with tab2:
        
    if st.session_state.clicked_suggestion is not None:
        st.subheader(st.session_state.suggestions_name[st.session_state.clicked_suggestion])
        st.write(st.session_state.suggestions_desc[st.session_state.clicked_suggestion])
        
        col1, col2, col3 = st.columns(3)
        col1.metric("AI Confidence", f"{random.randint(70, 99)}%")
        col2.metric("Potential ROI", f"{random.randint(5, 50)}%")
        col3.metric("Risk Level", f"{random.choice(['Low', 'Medium', 'High'])}")
        style_metric_cards(background_color="#e8e3e3", border_left_color="#FF9900")

    # st.subheader("Investor Similarity")
    # similarity_fig = create_similarity_heatmap()
    # st.plotly_chart(similarity_fig, use_container_width=True)
    
    # st.subheader("Investor Clusters")
    # clusters = ["DeFi Experts", "NFT Collectors", "Web3 Enthusiasts", "GameFi Pioneers"]
    # selected_cluster = st.selectbox("Select a cluster to view", clusters)
    
    # if selected_cluster:
    #     st.write(f"Investors in the {selected_cluster} cluster:")
    #     df = pd.DataFrame({
    #         "Investor": [f"Investor {i}" for i in range(1, 6)],
    #         "Similarity Score": np.random.uniform(0.7, 0.99, 5),
    #         "Common Investments": np.random.randint(1, 5, 5)
    #     })
    #     st.dataframe(df)

with tab3:
    st.subheader("On-Chain AI Agent Discussion")
    st.title("Investment Discussion between Two Agents")
try:
    conversation = assets.get_conv(st.session_state.clicked_suggestion)
    
    for speaker, message in conversation:
        if speaker.startswith("User"):
            st.subheader(f"{speaker} Investment Data")
            for key, value in message.items():
                if isinstance(value, list):
                    st.write(f"{key}: {', '.join(value)}")
                else:
                    st.write(f"{key}: {value}")
            st.write("---")
        else:
            st.subheader(speaker)
            st.write(message)
            st.write("---")
except:
    pass
# Footer
st.markdown("---")
st.markdown("dHive - Empowering investors with AI-driven social recommendations and on-chain verification.")

# Remove the rerun and sleep
# time.sleep(1)
# st.rerun()