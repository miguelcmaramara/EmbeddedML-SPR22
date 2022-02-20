# display.py 
import matplotlib.pyplot as plt
from mpl_toolkits  import mplot3d


def display_xyzt(xyzt_tuple, color="Greens", label='Plot label'):
    """
        Takes a tuple of x, y, z, t(time) lists and plots it as a 3dscatterpot.

        Each dot's point in space is determined by x, y, and z, while the
        color is determined by it's t value

        Parameters
        ----------
        xyzt_tuple: tuple of lists
            x, y, z t tuples
        color: string
            color of the plot
        label: string
            name of the plot

        Returns
        ----------
        None
    """
    (x, y, z, t) = xyzt_tuple

    if(len(x) != len(y) != len(z) != len(t)):
        raise Exception("x, y, z and t lists must be the same size")

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3d(x, y, z, c=t, cmap=color, label=label)





if __name__ == "__main__":
    test_tuple = (
            [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0],
            [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0],
            [3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0],
            [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
        )
    display_xyzt(test_tuple)
