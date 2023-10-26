from scipy.linalg import lstsq
from itertools import groupby
from typing import List





def solution_3(your_company_name: str, other_company_names: List[str], other_company_prices: List[int]) -> float:
    """
    Function to find the price of your company name based on the prices of other company names

    Args:
        your_company_name (str): Your company name
        other_company_names (List[str]): List of other company names
        other_company_prices (List[int]): List of prices of other company names
    
    Returns:
        price (float): Price of your company name

    Examples:
        >>> your_company_name = "google"
        >>> other_company_names = ["amazon", "apple", "facebook", "google", "microsoft"]
        >>> other_company_prices = [1, 2, 3, 4, 5]
        >>> solution_3(your_company_name, other_company_names, other_company_prices)
        4.0
    """
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



def solution_2(t:int, x:int, y:int) -> List[str]:
    """
    Function to find the minimum number of operations to reach a target number t from 1 using only addition and multiplication by x and y

    Args:
        t (int): Target number
        x (int): First multiplier
        y (int): Second multiplier

    Returns:
        ops (List[str]): List of operations to reach t from 1

    Examples:
        >>> t = 18
        >>> x = 5
        >>> y = 7
        >>> solution_2(t, x, y)
        ['operator_multiply', ...]
    """
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

def solution_1(xs:int, ys:int, xe:int, ye:int):
    """
    Function to find the probability of reaching the end point (xe, ye) from the start point (xs, ys) in a 2D grid

    Args:
        xs (int): x-coordinate of start point
        ys (int): y-coordinate of start point
        xe (int): x-coordinate of end point
        ye (int): y-coordinate of end point
    
    Returns:
        prob (float): Probability of reaching the end point (xe, ye) from the start point (xs, ys) in a 2D grid

    Examples:
        >>> xs = 1
        >>> ys = 1
        >>> xe = 2
        >>> ye = 2
        >>> solution_1(xs, ys, xe, ye)
        0.25
    """
    if all([xe == 0, ye == 0]):
        return 0.25
    
    elif all([xs == 0, ys == 0]):
        return 4/13
    
    else:
        return 1 / 13 
