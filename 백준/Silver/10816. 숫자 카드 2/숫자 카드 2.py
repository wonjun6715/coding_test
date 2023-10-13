N = int(input())
cards = list(map(int, input().split()))
M = int(input())
candidate = list(map(int, input().split()))
cards.sort()
count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

def binarySearch(arr, target, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return count.get(target)
    elif arr[mid] < target:
        return binarySearch(arr, target, mid+1, end)
    else:
        return binarySearch(arr, target, start, mid-1)
    
for target in candidate:
    print(binarySearch(cards, target, 0, len(cards)-1), end=" ")