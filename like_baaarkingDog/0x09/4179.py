import sys
from collections import deque

r, c = map(int,sys.stdin.readline().split())
graph = []

q_j = deque()
q_f = deque()

visited_j = [[0]*c for _ in range(r)]
visited_f = [[0]*c for _ in range(r)]

move = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(r):
    temp = list(input())
    # F, j check
    for j in range(len(temp)):
        if temp[j] == 'J':
            q_j.append((i,j))
            visited_j[i][j] = 1
        elif temp[j] == "F":
            q_f.append((i,j))
            visited_f[i][j] = 1
    graph.append(temp)

def bfs():
    # 사람과 불 두가지 나눠 진행
    while q_f:
        x, y = q_f.popleft()

        for i in range(4):
            nx, ny = x+move[i][0], y+move[i][1]

            if 0<=nx<r and 0<=ny<c:
                if not visited_f[nx][ny] and graph[nx][ny] != "#":
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    q_f.append((nx,ny))
    while q_j:
        x, y = q_j.popleft()

        for i in range(4):
            nx, ny = x+move[i][0], y+move[i][1]

            if 0<=nx<r and 0<=ny<c:
                if graph[nx][ny] != "#" and not visited_j[nx][ny]:
                    # 아직 방문하지 않았거나, 방문하려고하는데 현재 차수가 불의 방문 차수보다 낮으면 가능 -> 빨리 방문 후 지나가야해서
                    if not visited_f[nx][ny] or visited_f[nx][ny] > visited_j[x][y] + 1:
                        visited_j[nx][ny] = visited_j[x][y]+1
                        q_j.append((nx,ny))
            else:
                return visited_j[x][y]

    return "IMPOSSIBLE"

print(bfs())