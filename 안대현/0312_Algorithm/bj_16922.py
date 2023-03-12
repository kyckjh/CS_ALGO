def recur(swchr, start):
    global swch
    if swchr == N:
        arr[swch] = 1
        return
    for i in range(start, 4):
        swch += romNum[i]
        recur(swchr + 1, i)
        swch -= romNum[i]

N = int(input())
romNum = [1, 5, 10, 50]
arr = [0] * (50 * 20 + 1)
swch = 0
recur(0, 0)
print(sum(arr))