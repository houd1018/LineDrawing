import matplotlib.pyplot as plt

# Midpoint algorithm can only be applied when dx > 0 && dy > 0 && 0< k < 1

def DrawMid(x1, y1, x2, y2):
    # xs and ys record every coordinate of the points
    xs = []
    ys = []

    # initial cordinate
    x, y = x1, y1
    xs.append(round(x))
    ys.append(round(y))

    dx = int(x2 - x1)
    dy = int(y2 - y1)

    # decision maker Integer e
    # if e < 0, y++
    # else maintain the same
    e = dx - 2 * dy
    upInc = 2 * dx - 2 * dy
    downInc = -2 *dy

    # record remaining points
    for i in range(dx):
        x += 1
        if(e < 0):
            y += 1
            e += upInc
        else:
            e += downInc
        xs.append(round(x))
        ys.append(round(y))


###########################ploting part##################

    plt.axvline(x=0, linewidth=1, color='k')  # x axis
    plt.axhline(y=0, linewidth=1, color='k')  # y axis
    plt.axis([-50, 50, -50, 50]) 
    plt.axis('equal')
    plt.xlabel('x')
    plt.ylabel('y')
    for i in range(0, len(xs)):
        plt.scatter(xs[i], ys[i], color='k', s=1)
        # print a point in each 0.1 second
        plt.pause(0.1)
        plt.draw()
    plt.show()


# DrawMid(3, 1, 9, 20)