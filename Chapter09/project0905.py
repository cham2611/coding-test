# 9-5 전보
import heapq
import sys
input = sys.stdin.readline
INF = int(10**9)

# 노드, 간선, 시작노드
N, M, C = map(int, input().split()) 
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(N+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (N+1)

for i in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))



def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        #가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)

# 도달할 수 있는 노드의 개수
city = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0

for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        city += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 city - 1을 출력
print(city - 1, max_distance)