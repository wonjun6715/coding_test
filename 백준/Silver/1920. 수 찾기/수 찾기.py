n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
# B의 정수들이 A에 들어가는지 확인하면 되는 문제

A.sort() # 이진탐색은 오름차순 정렬해야됨
def binary_search(target, A):
   
    left = 0
    right = n - 1
    
    while left <= right:
        mid = (left + right) // 2
        if target == A[mid]:
            return 1
        elif target > A[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return 0
for i in B:
    result = binary_search(i, A)
    print(result)     


        

