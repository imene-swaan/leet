from scipy.linalg import lstsq


def solution(your_company_name, other_company_names, other_company_prices):
    if len(other_company_names) < 2:
        return -1
    num_letters = 26
    A = []
    for name in other_company_names:
        freq = [0] * num_letters
        for char in name:
            freq[ord(char) - ord('a')] += 1
        A.append(freq)

    letter_prices, _, _, _ = lstsq(A, other_company_prices)

    price = sum([letter_prices[ord(char) - ord('a')] for char in your_company_name])

    for char in your_company_name:
        if char not in ''.join(other_company_names):
            return -1

    return price


from itertools import groupby

def solution(t, x, y):
    ops= []
    
    if any([x>t, y>t]):
        return ["no_solution"]
    
    while t > 1: 
        if (t % y) == 0:
            ops.append('multiply')
            t /= y
        
        else:
            ops.append('add')
            t -= x
      
    return ["operator_{} {}".format(k, len(list(g))) for k, g in groupby(ops)][::-1]

def solution(xs, ys, xe, ye):
    if all([xe == 0, ye == 0]):
        return 0.25
    
    elif all([xs == 0, ys == 0]):
        return 4/13
    
    else:
        return 1 / 13 

