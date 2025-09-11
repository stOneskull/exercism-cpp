def find(numlist, numseek):
    if not numlist:
        raise ValueError('no nums')

    left, right = 0, len(numlist)-1

    while left < right:
        mid = (left + right + 1) // 2
        
        if numlist[mid] > numseek:
            right = mid - 1
        else:
            left = mid

    if numlist[left] != numseek:
        raise ValueError('no num')

    return left
