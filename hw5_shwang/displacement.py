def displacement(u_init, t, a):
    """Function that calculates the total displacement of a body during a time intervalt, 
    when the body has initial speedu_init and a constant accelerationa"""
    
    s = (u_init) * t + 0.5 * a * t**2
    
    