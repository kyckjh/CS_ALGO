def reversing():            # 문자열에 R을 받았을 때 수행할 함수
    global result           # result 변수를 전역변수로 받아야하니 글로벌 선언
    global revFlag          # revFlag를 전역변수로 받아야하니 글로벌 선언
    if result == 'error':   # result가 error면 에러.
        result = 'error'
        return
    else:                   # result가 에러 아니면,
        if revFlag:         # revFlag를 뒤집어줌
            revFlag = False
        else:
            revFlag = True
        return

def dropping():             # 문자열에 D를 받았을 때 수행할 함수
    global result
    global revFlag
    if len(numList)==0 or result == 'error':    # 리스트가 비어있으면 에러
        result = 'error'
        return
    else:
        if revFlag:         # revFlag가 참이면 리스트 제일 뒤 인덱스를 팝
            numList.pop()
        else:
            numList.pop(0)  # revFlag가 거짓이면 리스트 첫 인덱스를 팝
            return

T = int(input())
for tc in range(T):
    result = 'initialized'  # 결과값을 담을 변수 선언
    funcStr = input()       # R, D 명령어를 받아서 문자열에 할당
    revFlag = False         # 뒤집을까 말까. 우선 거짓으로 초기화
    N = int(input())
    tmpInput = input()      # 입력받은 배열(처럼 보이는 문자열)은
    tmpInput = tmpInput.replace('[','') # 앞뒤 대괄호를 떼어줌
    tmpInput = tmpInput.replace(']','')
    if N == 0:              # 빈 배열(처럼 보이는 문자열)을 받으면 빈리스트
        numList = []
    else:                   # 그게 아니면 문자열에 있는 숫자들을 리스트로 만듦
        numList = list(map(str, tmpInput.split(',')))
    for i in range(len(funcStr)):   # 명령어문자열을 훑고 위의 함수 실행
        if funcStr[i] == 'R':
            reversing()
        elif funcStr[i] == 'D':
            dropping()
        else:
            pass
    if result == 'error':   # 결과가 에러라면 결과는 에러입니다 (끄덕)
        result = 'error'
    elif result == '[]':    # 결과가 빈배열이면 결과는 빈배열
        pass
    else:
        if revFlag:             # 뒤집플래그가 참이면 리스트를 뒤집자
            numList.reverse()
        else:
            pass                # 결과는 리스트의 요소들을 공백없이 문자열화한 것
        result = '[' + ','.join(numList) + ']'
    print(result)