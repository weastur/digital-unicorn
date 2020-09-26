a = list(map(int, input().split()))
print(a)
print(list(filter(lambda item: item % 15 == 0, a)))
