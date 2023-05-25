weighted_edges = {}  # Dicionário para armazenar os pesos das arestas

with open('US_airports.net', 'r') as file:
    for line in file:
        node1, node2, weight = line.split()
        node1 = int(node1)
        node2 = int(node2)
        weight = int(weight)
        edge = (node1, node2)
        if edge in weighted_edges:
            weighted_edges[edge] += weight
        else:
            weighted_edges[edge] = weight

# Calcula o fluxo de passageiros total para cada aeroporto
fluxo_total_por_no = [0] * 500
for edge, weight in weighted_edges.items():
    node1, node2 = edge
    fluxo_total_por_no[node1] += weight
    fluxo_total_por_no[node2] += weight

# Calcula o fluxo de passageiros total 
fluxo_total = sum(weighted_edges.values())

# Exibe o fluxo de passageiros de cada aeroporto
for i in range(500):
    print(f"Aeroporto {i}: Fluxo de passageiros = {fluxo_total_por_no[i]}")

# Exibe o fluxo de passageiros total 
print(f"Fluxo de passageiros total (arestas): {fluxo_total}")
