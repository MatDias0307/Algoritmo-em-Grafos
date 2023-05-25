import networkx as nx
import matplotlib.pyplot as plt

# Le a base de dados
graph = nx.read_weighted_edgelist('US_airports.net', nodetype=int)

# Calcula a centralidade de grau 
degree_centrality = nx.degree_centrality(graph)

# Ordena os nós por centralidade de grau em ordem decrescente
sorted_nodes = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)

# Define a porcentagem de nós centrais a serem removidos
removal_percentage = 0.01

# Calcula o número de nós a serem removidos
num_nodes_to_remove = int(len(graph) * removal_percentage)

# Remove os nós centrais
removed_nodes = [node for node, centrality in sorted_nodes[:num_nodes_to_remove]]
graph.remove_nodes_from(removed_nodes)

# Calcula o número de arestas do novo grafo
num_edges = graph.number_of_edges()

# Calcula o fluxo total de passageiros do novo grafo
total_weighted_degree = sum(weight for _, _, weight in graph.edges(data='weight'))

print(f'Número de arestas do novo grafo: {num_edges}')
print(f'Fluxo total de passageiros do novo grafo: {total_weighted_degree}')

# Plota o grafo
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos=pos, with_labels=True, alpha=0.7)
plt.axis('off')
plt.show()
