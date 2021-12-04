import matplotlib.pyplot as plt


def Drawcircle(x_off, y_off, r):
    xs = []
    ys = []

    # initial cordinate
    x = 0
    y = r

    # decision maker Integer e
    # if e < 0, y++
    # else maintain the same
    e = 1 - r

    # put initial cordinate
    xs.append(x)
    ys.append(y)

    # record remaining points   
    while x < y:
        if e < 0:
            x += 1
            e += 2 * x + 3
        else:
            x += 1
            y -= 1
            e += 2 * (x - y) + 5
        xs.append(x)
        ys.append(y)



###########################ploting part##################
    plt.axis('equal')
    plt.axvline(x=0, linewidth=1, color='k')  # x axis
    plt.axhline(y=0, linewidth=1, color='k')  # y axis
    plt.axis([-50, 50, -50, 50])
    plt.xlabel('x')
    plt.ylabel('y')
    for i in range(0, len(xs)):
        # making up other 7 parts
        if i == 0:
            plt.scatter(xs[i] + x_off, ys[i] + y_off, color='k', s=1)
            plt.scatter(xs[i] + x_off, -ys[i] + y_off, color='k', s=1)
            plt.scatter(ys[i] + x_off, xs[i] + y_off, color='k', s=1)
            plt.scatter(ys[i] + x_off, -xs[i] + y_off, color='k', s=1)
            plt.pause(0.1)
        else:
            plt.scatter(xs[i] + x_off, ys[i] + y_off, color='k', s=1)
            plt.scatter(-xs[i] + x_off, ys[i] + y_off, color='k', s=1)
            plt.scatter(xs[i] + x_off, -ys[i] + y_off, color='k', s=1)
            plt.scatter(-xs[i] + x_off, -ys[i] + y_off, color='k', s=1)
            plt.scatter(ys[i] + x_off, xs[i] + y_off, color='k', s=1)
            plt.scatter(-ys[i] + x_off, xs[i] + y_off, color='k', s=1)
            plt.scatter(ys[i] + x_off, -xs[i] + y_off, color='k', s=1)
            plt.scatter(-ys[i] + x_off, -xs[i] + y_off, color='k', s=1)
            plt.pause(0.1)
            plt.draw()
    plt.show()


# Drawcircle(10, 8, 50)
