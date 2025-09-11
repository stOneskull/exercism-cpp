def find(numlist, numseek):
    if not numlist:
        raise ValueError('value not in array')

    left, right = 0, len(numlist)-1

    while left <= right:
        mid = (left + right) // 2
        
        if numlist[mid] == numseek:
            return mid
        elif numlist[mid] > numseek:
            right = mid - 1
        else:
            left = mid + 1

    raise ValueError('value not in array')
