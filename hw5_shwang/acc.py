def acceleration( u1, u2, t1, t2 ):
    """Function hat takes the different speeds (u1,u2) of a body at times t1 and t2 and 
    calculates the acceleration of the body"""

    a = (u2 - u1) / (t2 - t1)
    return a

    
    