import matplotlib.pyplot as plt

# Expression method can only be applied when dx > 0 && dy > 0 && 0< k < 1
def DrawExp(x1, y1, x2, y2):
    # xs and ys record every coordinate of the points
    xs = []
    ys = []

    # initial cordinate
    x, y = x1, y1
    xs.append(round(x))
    ys.append(round(y))

    # length
    dx = abs(x2 - x1)

    # parameter in the expression
    k = float(y1 - y2) / float(x1 - x2)
    b = float(y1 - k * x1)

    # record remaining points
    for i in range(0, dx):
        x += 1
        y = k * x + b
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


# DrawExp(3, 1, 9, 20)
