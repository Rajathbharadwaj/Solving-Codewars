import math as m

def find_next_square(sq):
    if int(m.sqrt(sq))**2==sq:
        success = False
        while not success:
            next_perfect_square = sq+1
            if int(m.sqrt(next_perfect_square))**2==next_perfect_square:
                success = True
                return next_perfect_square
            else:
                sq = next_perfect_square
                
    else:
        return -1
