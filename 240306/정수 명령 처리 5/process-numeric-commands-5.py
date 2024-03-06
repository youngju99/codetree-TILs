N = int(input())
res = []

for _ in range(N):
    tmp = input().split()
    command = tmp[0]
    if len(tmp) == 2:
        n = int(tmp[1])

    if command == "push_back":
        res.append(n)
    elif command == "pop_back":
        res.pop() # 맨 뒤의 요소 삭제
    elif command == "size":
        print(len(res))
    elif command == "get":
        print(res[n-1])