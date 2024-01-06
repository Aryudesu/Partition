def partition(num, mem):
    result = 0
    for i in range(1, num + 1):
        gokaku1, gokaku2 = [i * (3 * i - 1) // 2, i * (3 * i + 1) // 2]
        if num < gokaku1 and num < gokaku2:
            break
        if num >= gokaku1:
            result += mem[num - gokaku1] if i % 2 else -mem[num - gokaku1]

        if num >= gokaku2:
            result += mem[num - gokaku2] if i % 2 else -mem[num - gokaku2]
    return result


def calcPartition(num):
    result = [1]
    for i in range(1, num + 1):
        result.append(partition(i, result))
    return result


def inputNum(mes="InputNum > "):
    while True:
        try:
            print(mes, end="")
            return int(input())
        except:
            print('Input "Num" Please')


def exportResult(result, filename):
    with open(filename, "w", encoding="UTF-8") as f:
        for i in range(len(result)):
            mes = f"p({i}) = {result[i]}\n"
            f.write(mes)


num = inputNum()
exportResult(calcPartition(num), "partition.txt")
