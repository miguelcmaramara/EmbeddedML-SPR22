# parse-csv.py

def csv_to_xyzt(pathname):
    """
        Converts a csv file to a tuple that contains an
        x, y, z, and t (time) lists of the same size

        Parameters
        ----------
        pathname : string
            path to the csv

        Returns
        -------
        tuple of lists
            (
                [x1,x2,x3, . . . xn],
                [y1,y2,y3, . . . yn],
                [z1,z2,z3, . . . zn],
            )
    """
    # 

    return None
    


if __name__ == "__main__":
    # Put testing code in here
    print("Hello world")



    #-------------
    # TEST CASE:
    #-------------

    # print(csv_to_xyzt("./path-raw-csv/testing.csv"))

    # the output of this should be:
    # (
    #   [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0],
    #   [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0],
    #   [3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0],
    #   [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
    # )