if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort(reverse=True)
    i=1
    while i<n:
        if arr[i]!=arr[i-1]:
            break
        i=i+1
    print(arr[i])
    
