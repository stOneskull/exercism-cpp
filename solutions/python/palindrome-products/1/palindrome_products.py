def largest_palindrome(max_factor, min_factor):
    return get_pals(max_factor, min_factor, 'lrg')
    

def smallest_palindrome(max_factor, min_factor):
    return get_pals(max_factor, min_factor, 'sml')


def get_pals(high, low, measure):
    therange = range(low, high+1)
    if measure == 'lrg':
        therange = range(high, low, -1)
    for one in therange:
        for two in therange:
            print(one, two)
            prod = one * two
            if is_pal(prod):
                return facts(prod)
    raise ValueError('Eeejit')
    
    
def is_pal(num):
    num = str(num)
    return num == num[::-1]


def facts(num):
    theset = set()
    for one in range(num):
        for two in range(num):
            if one * two == num:
                theset.add((one, two))
    return num, theset
