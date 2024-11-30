def floyd_warshall(graph):
    # Количество вершин в графе
    num_vertices = len(graph)

    # Инициализация матрицы расстояний
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    # Заполнение начальной матрицы расстояний
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    # Основной цикл алгоритма Флойда-Уоршелла
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
# Пример использования
if __name__ == "__main__":
    # Матрица смежности графа (0 означает отсутствие ребра)
    graph = [
        [0, 3, float('inf'), 5],
        [2, 0, float('inf'), 4],
        [float('inf'), 1, 0, float('inf')],
        [float('inf'), float('inf'), 2, 0]
    ]

    shortest_paths = floyd_warshall(graph)

    print("Матрица кратчайших путей:")
    for row in shortest_paths:
        print(row)