import matplotlib.pyplot as plt

def ROUND(a):
    return int(a + 0.5)

def DrawDDA(x1, y1, x2, y2):
    # xs and ys record every coordinate of the points
    xs = []
    ys = []

    # initial cordinate
    x, y = x1, y1
    xs.append(ROUND(x))
    ys.append(ROUND(y))

    # if k > 1, yInc = 1, else XInc =1.
    dx = int(x2 - x1)
    dy = int(y2 - y1)
    # determine ε
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    xInc = float(dx) / float(steps)
    yInc = float(dy) / float(steps)
    # record remaining points
    for i in range(steps):
        x += xInc
        y += yInc
        xs.append(ROUND(x))
        ys.append(ROUND(y))

    
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


# DrawDDA(-3, 1, -8, 20)
