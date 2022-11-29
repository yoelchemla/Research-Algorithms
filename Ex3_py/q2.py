import queue
INF = 100000000000


def min_distance(dist, queue):
    min = float(INF)
    min_index = -1

    for i in range(len(dist)):
        if dist[i] < min and i in queue:
            # update
            min = dist[i]
            min_index = i
    return min_index


# credit:  https://en.wikipedia.org/wiki/Floyd–Warshall_algorithm
def floyd_warshall(arr):
    n = len(arr)
    dist = list(map(lambda i: list(map(lambda j: j, i)), arr))

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[k][j] + dist[i][k] < dist[i][j]:
                    dist[i][j] = dist[k][j] + dist[i][k]
    return dist


# dijkstra algorithm
# credit:  https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm


def dijkstra(graph, src):
    row = len(graph)
    col = len(graph[0])
    dist = [INF] * row
    dist[src] = 0
    q = []
    for i in range(row):
        q.append(i)

    # the shortest path from src to all vertex
    while q:
        v = min_distance(dist, q)
        q.remove(v)
        for i in range(col):
            if graph[v][i] and i in q:
                # update
                if dist[i] > dist[v] + graph[v][i]:
                    dist[i] = dist[v] + graph[v][i]
    return dist


def shortest_path(arr, start: int = INF):
    if start == INF:
        return floyd_warshall(arr)
    return dijkstra(arr, (start - 1))


if __name__ == "__main__":

    mat = [[0, 17, 5, 3],
           [13, 0, 1, 9],
           [4, 2, 0, INF],
           [INF, 6, 6, 0]]

    ans = shortest_path(mat)
    for i in ans:
        print(i)
    print()
    print("all the path of node number 3")
    print(shortest_path(mat, 3))
    print("all the path of node number 2")
    print(shortest_path(mat, 2))
