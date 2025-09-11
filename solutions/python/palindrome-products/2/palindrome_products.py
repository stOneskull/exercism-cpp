def get_pals(fmin, fmax, size='small'):
    if size == 'small':
        therange = range(fmin**2, fmax**2+1)
    else:
        therange = range(fmax**2, fmin**2-1, -1)
        
    for num in therange:
        strum = str(num)
        if strum == strum[::-1] and any(
            fmin <= num // num2 <= fmax
                for num2 in range(fmin, fmax+1)
                    if not num % num2):
                        
            return num, ((num2, num//num2) 
                for num2 in range(fmin, fmax+1)
                    if not num % num2 and
                        fmin <= num2 <= num // num2 <= fmax)
                     
    raise ValueError('No can do')
        
        
def smallest_palindrome(max_factor, min_factor):
    return get_pals(min_factor, max_factor, 'small')


def largest_palindrome(max_factor, min_factor):
    return get_pals(min_factor, max_factor, 'large')
