def soon(i, k):                             # soon 함수는 순열 리스트를 돌려
    if i == k:                              # 리스트의 첫인덱스값이 0이 아닐 경우
        global maxNum                       # 이를 정수화하고 B보다 작고 기존 maxNum보다 크면
        if aList[0] == '0':                 # maxList에 담아줌
            return
        else:
            tmp = ''.join(s for s in aList)
            tmpN = int(tmp)
            if tmpN > maxNum and tmpN < B:
                maxList.append(tmpN)
                maxNum = tmpN
    else:
        for j in range(i, k):
            aList[i], aList[j] = aList[j], aList[i]
            soon(i+1, k)
            aList[i], aList[j] = aList[j], aList[i]

A, B = map(str, input().split())            # A, B를 문자열로 받음
B = int(B)                                  # B는 정수로 바꿔둠
maxList = []                                # 순열을 담을 리스트 선언
maxNum = 0                                  # 순열에 담기전 크기를 대조할 변수 선언
aList = [None] * len(A)                     # A의 숫자들을 담을 리스트 선언
for i in range(len(A)):                     # 라인23, 라인24: A의 숫자를 리스트에 담음
    aList[i] = A[i]
S = len(aList)                              # A의 크기를 나타내줄 변수 선언 및 초기화
soon(0, S)                                  # soon함수 가동

if len(maxList) == 0:                       # maxList에 아무것도 담긴게 없다면
    print('-1')                             # -1 출력
else:
    print(max(maxList))                     # maxList에서 가장 큰 값 출력
# a를 조합하여 만드는 수 중 b보다 작은 것들을 비교
