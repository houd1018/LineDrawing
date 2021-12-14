import time
from Expression import DrawExp
from dda import DrawDDA
from midpoint import DrawMid
from Bresenham import DrawBre


f=open("data.txt","w")

for i in range(5000, 21000, 1000):
    data = []
    data.append(i)

    start = time.time()
    for j in range(i):
        DrawBre(-3, 1, -8, 20)
    end = time.time()
    data.append(end - start)

    start = time.time()
    for j in range(i):
        DrawExp(-3, 1, -8, 20)
    end = time.time()
    data.append(end - start)

    start = time.time()
    for j in range(i):
        DrawMid(-3, 1, -8, 20)
    end = time.time()
    data.append(end - start)

    start = time.time()
    for j in range(i):
        DrawDDA(-3, 1, -8, 20)
    end = time.time()
    data.append(end - start)

    f.write(str(data)+'\n')

f.close()

