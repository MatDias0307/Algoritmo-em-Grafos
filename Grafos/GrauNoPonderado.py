import networkx as nx

# Le a base de dados
graph = nx.read_weighted_edgelist('US_airports.net', nodetype=int)

# Calcula o grau ponderado de cada nó
weighted_degree = dict(graph.degree(weight='weight'))

# Ordena os nós por grau ponderado em ordem decrescente
sorted_nodes = sorted(weighted_degree.items(), key=lambda x: x[1], reverse=True)

# Imprime o grau ponderado de cada nó em ordem decrescente
for node, weighted_degree_value in sorted_nodes:
    print(f'Aeroporto: {node} - Grau Ponderado: {weighted_degree_value}')

# Calcula o grau total do grafo
total_degree = sum(weighted_degree.values())
print(f'Grau Total do Grafo: {total_degree}')
