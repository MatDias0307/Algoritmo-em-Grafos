import networkx as nx

# Le a base de dados
graph = nx.read_weighted_edgelist('US_airports.net', nodetype=int)

# Calcula o grau de cada nó
degree = dict(graph.degree())

# Ordena os nós por grau em ordem decrescente
sorted_nodes = sorted(degree.items(), key=lambda x: x[1], reverse=True)

# Imprime o grau de cada nó em ordem decrescente
for node, degree_value in sorted_nodes:
    print(f'Aeroporto: {node} - Conexões: {degree_value}')
