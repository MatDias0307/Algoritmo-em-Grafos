import networkx as nx
import matplotlib.pyplot as plt
import community

# Carrega o grafo a partir do arquivo
G = nx.read_weighted_edgelist('US_airports.net')

# Executa o algoritmo de detecção de comunidades (Louvain)
partition = community.best_partition(G)

# Obtém o número de comunidades
num_communities = max(partition.values()) + 1

# Define cores para as comunidades
colors = plt.cm.get_cmap('tab10', num_communities)

print("Número de comunidades: ", num_communities)

# Plota o grafo com cores para cada comunidade
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G)
for node in G.nodes():
    community_id = partition[node]
    nx.draw_networkx_nodes(G, pos=pos, nodelist=[node], node_color=colors(community_id), node_size=100)
nx.draw_networkx_edges(G, pos=pos, alpha=0.5)
nx.draw_networkx_labels(G, pos=pos)
plt.axis('off')
plt.show()
