# display.py
import matplotlib.pyplot as plt
# from mpl_toolkits  import mplot3d


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
    (x_lst, y_lst, z_lst, t_lst) = xyzt_tuple

    # Error checking
    if(len(x_lst) != len(y_lst) != len(z_lst) != len(t_lst)):
        raise Exception("x, y, z and t lists must be the same size")

    # Creating figure and axes
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Plotting the points
    ax.scatter(x,y,z,cmap="jet")
    # for x, y, z, t in zip(x_lst, y_lst, z_lst, t_lst):
    #     ax.scatter(x, y, z, marker='o', c=t)

    # Setting Axes
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    plt.show()


def add_xyzt_plt(fig, xyzt_tuple, pos):
    (x_lst, y_lst, z_lst, t_lst) = xyzt_tuple

    # Error checking
    if(len(x_lst) != len(y_lst) != len(z_lst) != len(t_lst)):
        raise Exception("x, y, z and t lists must be the same size")

    # Creating figure and axes
    ax = fig.add_subplot(1, 2, pos + 1, projection='3d')

    # Plotting the points
    for x, y, z, t in zip(x_lst, y_lst, z_lst, t_lst):
        ax.scatter(x, y, z, marker='o', c=t)

    # Setting Axes
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    ax.set_box_aspect([1, 1, 1])
    # ax.set_xlim3d(-.5,.5)
    # ax.set_ylim3d(-.5,.5)
    # ax.set_zlim3d(-.5,.5)


def mult_xyzt_plt(lst_of_tups):
    fig = plt.figure(figsize=plt.figaspect(1/len(lst_of_tups)))
    
    for pos, xyzt_tuple in enumerate(lst_of_tups):
        add_xyzt_plt(fig, xyzt_tuple, pos)

    plt.show()

def plot_2d(xlst, ylst, zlst, tlst, color="blue"):
    at = plt.figure()
    tnew = []
    zeros=[]
    for t in tlst:
        tnew.append(t - tlst[0])
        zeros.append(0)

    xnew = []
    ynew = []
    znew = []
    for x, y, z in zip(xlst, ylst, zlst):
        xnew.append(x - xlst[0])
        ynew.append(y - ylst[0])
        znew.append(z - zlst[0])

    plt.plot(tnew, zeros, c="black")
    # plt.scatter(tnew, xnew, c=color, s=2)
    # plt.scatter(tnew, ynew, c="red", s=2)
    # plt.scatter(tnew, znew, c="green", s=2)
    # plt.plot(tnew, xnew, c=color)
    # plt.plot(tnew, ynew, c="red")
    # plt.plot(tnew, znew, c="green")

    plt.scatter(tnew, xlst, c=color, s=2)
    plt.scatter(tnew, ylst, c="red", s=2)
    plt.scatter(tnew, zlst, c="green", s=2)
    ln1 = plt.plot(tnew, xlst, c=color)
    ln2 = plt.plot(tnew, ylst, c="red")
    ln3 = plt.plot(tnew, zlst, c="green")


    # plt.ylim(-1,1)
    # plt.ylim(-1,1)

    # for x, y in zip(xlst,ylst):
    #     ax.scatter(x - xref, y)
    plt.legend(["zero", "x", "y", "z"])
    plt.show()


if __name__ == "__main__":
    test_tuple = (
            [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0],
            [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0],
            [3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0],
            [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
            # [0, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        )

    # display_xyzt(test_tuple)
    mult_xyzt_plt([test_tuple, test_tuple])# , test_tuple])
