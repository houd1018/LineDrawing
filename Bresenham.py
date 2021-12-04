import matplotlib.pyplot as plt


def DrawBre(x1, y1, x2, y2):
    # sx = 1 sy = 1: first quadrant
    # sx = -1 sy = 1: second quadrant
    # sx = -1 sy = -1: third quadrant
    # sx = 1 sy = -1: forth quadrant

    k = 0   # k < 1 as default

    # get the quadrant it points at 
    dx = abs(x2 - x1)
    if (x2 - x1) > 0: sx = 1 # moving forward
    else: sx = -1 # moving backward
    dy = abs(y2 - y1)
    if (y2 - y1) > 0: sy = 1
    else: sy = -1

    # if k > 1, swap all x and y.
    if dy > dx:  # k > 1
        k = 1
        x1, y1 = y1, x1
        dx, dy = dy, dx
        sx, sy = sy, sx
    
    # decision maker Integer e
    # if e < 0, y++
    # else maintain the same
    e = (2 * dy) - dx
    xs = []
    ys = []
    x = x1
    y = y1

    # record remaining points   
    for i in range(0, dx):
        if k:
            xs.append(y)
            ys.append(x)
        else:
            xs.append(x)
            ys.append(y)
        while e >= 0:
            y = y + sy
            e = e - (2 * dx)
        x = x + sx
        e = e + (2 * dy)
    xs.append(x2)
    ys.append(y2)



###########################ploting part##################

    plt.axvline(x=0, linewidth=1, color='k')  #x axis
    plt.axhline(y=0, linewidth=1, color='k')  #y axis
    plt.axis([-50, 50, -50, 50])
    plt.axis('equal')
    plt.xlabel('x')
    plt.ylabel('y')
    for i in range(len(xs)):
        plt.scatter(xs[i], ys[i], color='k', s=1)
        plt.pause(0.1)
        plt.draw()
    plt.show()


# DrawBre(-3, 1, -8, 20)
