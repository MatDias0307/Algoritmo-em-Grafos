import networkx as nx
import matplotlib.pyplot as plt

# Le a base de dados
G = nx.read_weighted_edgelist('US_airports.net')

# Calcula a centralidade de grau 
degree_centrality = nx.degree_centrality(G)

# Exibe a centralidade de grau em ordem decrescente
for node, centrality in sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True):
    print(f'Aeroporto {node}: {centrality}')

# Calcula o número de nós centrais a serem destacados
num_nodes = len(G.nodes)
num_central_nodes = int(num_nodes * 0.02)

# Obtém os nós centrais com maior centralidade de grau
central_nodes = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:num_central_nodes]

# Cria um conjunto com os nós a serem destacados
highlight_nodes = set(node for node, _ in central_nodes)

# Plota o grafo
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, with_labels=True, alpha=0.7)
nx.draw_networkx_nodes(G, pos=pos, nodelist=highlight_nodes, node_color='red', alpha=0.7)
plt.axis('off')
plt.show()
