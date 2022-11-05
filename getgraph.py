from rad import partition
from partition import calcPartition
import matplotlib.pyplot as plt


def exportResult(y1, y2, N, K, filename):
    with open(filename, "w", encoding="UTF-8") as f:
        for i in range(N, K):
            mes = f"p({i}) = {y2[i]} ({y1[i]})\n"
            f.write(mes)


def exportResult_y1(y1, N, K, filename):
    with open(filename, "w", encoding="UTF-8") as f:
        for i in range(N, K):
            mes = f"p({i}) = {y1[i]}\n"
            f.write(mes)


N = 1
K = 20000
ans1 = calcPartition(K+1)

exportResult_y1(ans1, N, K+1, "pnrad.txt")

# x = []
# y1 = []
# y2 = []
# y3 = []
# y4 = []
# s = 0
# for i in range(N, K + 1):
#     x.append(i)
#     y1.append(ans1[i])
#     ans2 = partition(i)
#     y2.append(ans2)
#     err = abs(ans1[i] - ans2)
#     y3.append(err)
#     s += err
#     y4.append(s)


# exportResult(y1, y2, N, K, "pnrad.txt")

# for i in range(N, K + 1):
#     print(y1[i], y2[i])

# width = 0.3

# plt.plot(x, y1, marker="o", color="orangered", label="Correct value")
# plt.bar(x, y2)
# plt.plot(x, y3, label="Error")
# plt.plot(x, y4, label="Accumulated error")
# plt.legend(loc='upper left')
# plt.show()
# err = sum(y3)
# print(err)
