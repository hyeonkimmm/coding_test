from collections import deque


def solution(n, paths, gates, summits):
    gates = set(gates)
    summits = set(summits)
    result = []

    route = [[] for _ in range(n + 1)]

    for path in paths:
        route[path[0]].append((path[1], path[2]))
        route[path[1]].append((path[0], path[2]))

    for start_gate in gates:
        q = deque()
        for path in route[start_gate]:
            # 이전 목적지, 다음 목적지, 등산이 가장 오래 걸린 시간, 출발지, 산봉우리 도착 했는지 여부
            q.append((start_gate, path[0], path[1], start_gate, None))
        while q:
            prev, cur, max_time, start, summit = q.popleft()
            for path in route[cur]:
                next_node, hiking_time = path
                # 산봉우리 도착 했고, 다음 목적지에 출발지가 있다면
                if summit is not None and next_node == start:
                    result.append((max(max_time, hiking_time), summit))
                # 현재 위치가 산봉우리라면
                if cur in summits:
                    # 다음 목적지가 다른 산봉우리, 출발지가 아니면 큐에 추가
                    if next_node not in summits and next_node not in gates:
                        q.append((cur, next_node, max(max_time, hiking_time), start, cur))
                else:
                    # 산봉우리 먼저 도착한 경우
                    if summit is not None:
                        # 다음 목적지가 다른 산봉우리, 출발지, 이전 지점이 아니면 큐에 추가
                        if next_node not in summits and next_node not in gates and next_node != prev:
                            q.append((cur, next_node, max(max_time, hiking_time), start, summit))
                    else:
                        # 다음 목적지가 출발지, 이전 지점이 아니면 큐에 추가
                        if next_node not in gates and next_node != prev:
                            q.append((cur, next_node, max(max_time, hiking_time), start, summit))

    max_time, summit = sorted(result)[0]
    return [summit, max_time]

n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]

print(solution(n, paths, gates, summits))


a = 'abc'
id(a)
a = '456'
id(a)