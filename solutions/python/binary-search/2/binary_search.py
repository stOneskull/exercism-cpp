def binary_search(numlist, num):
    if not numlist:
        raise ValueError('no nums')

    left, right = 0, len(numlist)-1

    while left < right:
        mid = (left+right+1)//2
        if numlist[mid] > num:
             right = mid-1
        else:
            left = mid

    if numlist[left] != num:
        raise ValueError('no num')

    return left
