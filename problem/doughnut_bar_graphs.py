# https://school.programmers.co.kr/learn/courses/30/lessons/258711
from collections import defaultdict

graph = defaultdict(list)
in_degree = dict()
out_degree = dict()


def setup_graph_structure(edges):
    global graph, in_degree, out_degree
    for start, end in edges:
        graph[start].append(end)
        if start not in in_degree:
            in_degree[start] = 0
        if end not in out_degree:
            out_degree[end] = 0
        in_degree[end] = in_degree.get(end, 0) + 1
        out_degree[start] = out_degree.get(start, 0) + 1


def solution(edges):
    result = [0 for _ in range(4)]
    visited = set()
    setup_graph_structure(edges)
    source_node = [node for node in in_degree if (in_degree[node] == 0 and out_degree[node] >= 2)].pop()

    result[0] = source_node
    for node in graph[source_node]:
        while node:
            if out_degree[node] == 0:
                result[2] += 1
                break
            elif out_degree[node] == 2:
                result[3] += 1
                break
            elif node in visited and out_degree[node] == 1:
                result[1] += 1
                break
            visited.add(node)
            node = graph[node][0]

    return result


input_edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
print(solution(input_edges))