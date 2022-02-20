

def integrate(x, t):
    """
    Integrte x with respect to t

    Integrate works by doing a rectangular approx at each point in time.
    The equation is (x_i + x_{i+1})/ti + previous integrated value

    ----------
    x : list of floats

    t: list of flaots

    Returns
    -------
    An integrated list of points
    """

    return None
    

def integrate_xyzt(xyzt_tuple):
    """
    Integrates an entire xyzt tuple and returns it
    """

    return None


if __name__ == "__main__":
    # Put testing code in here
    print("Hello world")



    #-------------
    # TEST CASE:
    #-------------

    # x = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    # t = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

    # print(integrate(x,t))