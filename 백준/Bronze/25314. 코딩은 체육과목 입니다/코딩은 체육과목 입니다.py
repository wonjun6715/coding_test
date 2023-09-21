N = int(input())

answer = ''
a = N // 4

for i in range(a):
    answer += 'long '
    
print(answer + 'int')