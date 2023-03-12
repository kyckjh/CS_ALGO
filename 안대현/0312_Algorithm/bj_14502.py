import copy

N, M = map(int, input().split())
oriMap = [list(map(int, input().split())) for _ in range(N)]
route = [(-1,0), (1,0), (0,-1), (0,1)]
maxSafe = 0                                                     # 벽을 치는 케이스 중 가장 안전지역이 많을 때의 안전지역 수
coList = []                                                     # 벽을 칠 수 있는 좌표를 담을 리스트
for i in range(N):
    for j in range(M):
        if oriMap[i][j] == 0:
            coList.append((i,j))                                # 해당 리스트에 벽을 칠 수 있는 좌표를 모두 담아줌
for i in range(len(coList)-2):                                  # 라인12~14: 3중 반복문을 통해 이하 코드에서
    for j in range(i+1, len(coList)-1):                         # 벽3개를 치는 모든 케이스를 순회할 수 있도록 해줌
        for k in range(j+1, len(coList)):
            infected = []                                       # 감염된 좌표를 담아줄 리스트 선언
            queue = []                                          # 감염확산을 위한 큐 선언
            for l in range(N):                                  # 라인17~라인21: 기존 감염좌표를 리스트와 큐에 넣어줌
                for m in range(M):
                    if oriMap[l][m] == 2:
                        infected.append((l,m))
                        queue.append((l,m))
            labMap = copy.deepcopy(oriMap)                      # 케이스를 순회하기 위해 복사된 실험실맵을 생성
            labMap[coList[i][0]][coList[i][1]] = 3              # 라인23~라인25: 벽 세곳을 침
            labMap[coList[j][0]][coList[j][1]] = 4
            labMap[coList[k][0]][coList[k][1]] = 5

            while queue:                                        # 라인27~라인35: 감염좌표 리스트, 큐를 사용하여
                current = queue[0]                              # 벽으로 막히지않은 곳들의 좌표에 감염 확산
                for l in route:                                 # 즉, 막히지않은 곳은 모두 2로 만듦
                    ni, nj = current[0]+l[0], current[1]+l[1]
                    if 0 <= ni < N and 0<= nj < M and (ni, nj) not in infected and labMap[ni][nj] == 0:
                        infected.append((ni, nj))
                        labMap[ni][nj] = 2
                        queue.append((ni, nj))
                queue.pop(0)
            safeCnt = 0                                         # 라인36~라인40: 실험실맵에서 0인 곳의 개수를 파악
            for l in labMap:
                for m in l:
                    if m == 0:
                        safeCnt += 1
            if safeCnt > maxSafe:                               # 라인41,라인42: 본 케이스의 안전좌표가 역대 최대로
                maxSafe = safeCnt                               # 많은지 여부 확인
print(maxSafe)