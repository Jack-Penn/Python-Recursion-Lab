def collatz_sequence(n):
    print(n, end=" ")
    if n == 1:
        return
    elif n % 2 == 0:
        collatz_sequence(n // 2)
    else:
        collatz_sequence(n * 3 + 1)

def print_backwards(s):
    print(s[-1:], end="")
    if(len(s) != 1):
        print_backwards(s[:-1])

def hammer_profit(cost, prices):
    if len(prices) == 0:
        return 0
    return hammer_profit(cost, prices[1:]) + prices[0] - cost

def format_names(names):
    arr = []
    if("," in names[0]):
        arr.append(names[0])
    else:
        arr.append(", ".join(names[0].split(" ")))
    if (len(names) == 1):
        return arr
    else:
        return arr + format_names(names[1:])


if(__name__ == "__main__"):
    collatz_sequence(13)
    print()
    print_backwards("Hello, world!")
    print()
    print(hammer_profit(15.00, [14.00, 15.00, 17.00]))
    print(hammer_profit(20.00, [19.00, 18.00, 23.00, 22.50, 15.00, 25.00]))
    print(format_names(["Allen Anderson", "Bruce Baker", "Cook, Claire", "Dunn, David"]))