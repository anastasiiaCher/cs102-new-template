import math

while True:

    def check_int(num1, num2):
        num1 = str(num1)
        num2 = str(num2)
        if num1[-1] == "0" and num2[-1] == "0" and num1[-2] == "." and num2[-2] == ".":
            return 1


    def del2(num1, num2):
        return int(str(num1)[:-2]), int(str(num2)[:-2])

    def convert(num1, num2):
        s = ""
        while num1 > 0:
            s += str(num1 % num2)
            num1 //= num2
        return int(s[::-1])

    def calc_case(com: str, num1, num2: float):
        match com:
            case "+":
                return (lambda a, b: a + b)(num1, num2)
            case "-":
                return (lambda a, b: a - b)(num1, num2)
            case "*":
                return (lambda a, b: a * b)(num1, num2)
            case "/" if num2 == 0:
                return "На ноль делить нельзя"
            case "/":
                return (lambda a, b: a / b)(num1, num2)
            case "^y":
                return (lambda a, b: a**b)(num1, num2)
            case "#" if num2 > 9:
                return "Основание СС не должно превышать 9"
            case "#" if check_int(num1, num2) is None:
                return "Число и основание СС должны быть целыми"
            case "#":
                num1, num2 = del2(num1, num2)
                return convert(num1, num2)
            case "sin":
                return (lambda a: math.sin(a))(num1)
            case "cos":
                return (lambda a: math.cos(a))(num1)
            case "tg":
                return (lambda a: math.tan(a))(num1)
            case "^2":
                return (lambda a: a**2)(num1)
            case "lg":
                return (lambda a: math.log10(a))(num1)
            case "ln":
                return (lambda a: math.log(a))(num1)
            case _:
                return "Нет такой операции"

    def chain(a):
        a = a.replace(" ", "")
        a = a.replace("**", "^")
        if a == "":
            print("Некорректный ввод")
            return chain(input("Введите цепочку > "))
        flag = 0
        k = 0
        c = 0
        for i in range(len(a)):
            if a[i] not in numbers + symbols:
                flag = 1
        s = a
        if s[0] == "(" and a.count("(") != a.count(")"):
            flag = 1
        if s[len(s) - 1] == "(" and a.count("(") != a.count(")"):
            flag = 1
        if s[0] == "+" or s[0] == "*" or s[0] == "/" or s[0] == "^" or s[0] == ")" or s[0] == "-":
            flag = 1
        if (s[len(s) - 1] in z) or (s[len(s) - 1] == "(") or (s[len(s) - 1] == "."):
            flag = 1
        s = s + " "
        for i in range(1, len(s) - 1):
            if s[i] in numbers and s[i - 1] == ")":
                flag = 1
            elif s[i] in numbers and s[i - 1] != ")":
                if s[i + 1] not in numbers:
                    if s[i] == ".":
                        flag = 1
                    for j in range(i, 0, -1):
                        if s[j] in numbers:
                            if s[j] == ".":
                                k += 1
                                if k > 1:
                                    flag = 1
                        else:
                            break
            elif s[i] in z and s[i - 1] not in numbers:
                flag = 1
            elif s[i] == "(" and (s[i - 1] == ")" or s[i - 1] in nums or a.count("(") != a.count(")")):
                flag = 1
            elif s[i] == ")" and (s[i - 1] == "(" or s[i - 1] in zn or s.count("(") != s.count(")")):
                flag = 1
        if flag == 0:
            return a
        else:
            print("Некорректный ввод")
            return chain(input("Введите цепочку > "))

    def iter(i: int, a: str):
        k1 = 0
        k2 = 0
        a1 = ""
        a2 = ""
        for j in range(i - 1, 0, -1):
            if a[j] in numbers:
                a1 += a[j]
                k1 += 1
            else:
                break
        a1 = a1[::-1]
        for j in range(i + 1, len(a)):
            if a[j] in numbers:
                a2 += a[j]
                k2 += 1
            else:
                break
        a = a[: (i - k1)] + "r" + a[(i + k2 + 1) :]
        return a1, a2, a

    def bracket(a: str, c1, c2: int):
        f = 0
        for i in range(c1 + 1, c2):
            if a[i] == "^":
                a1, a2, a = iter(i, a)
                d = str(float(a1) ** float(a2))
                a = a.replace("r", d, 1)
                f = 1
                break
        if f == 1:
            return bracket(a, 0, len(a))
        else:
            for i in range(c1 + 1, c2):
                if a[i] == "*" or a[i] == "/":
                    if a[i] == "*":
                        a1, a2, a = iter(i, a)
                        d = str(float(a1) * float(a2))
                        a = a.replace("r", d, 1)
                        f = 1
                        break
                    else:
                        a1, a2, a = iter(i, a)
                        d = str(float(a1) / float(a2))
                        a = a.replace("r", d, 1)
                        f = 1
                        break
        if f == 1:
            return bracket(a, 0, len(a))
        else:
            for i in range(c1 + 1, c2):
                if a[i] == "+" or a[i] == "-":
                    if a[i] == "+":
                        a1, a2, a = iter(i, a)
                        d = str(float(a1) + float(a2))
                        a = a.replace("r", d, 1)
                        f = 1
                        break
                    else:
                        a1, a2, a = iter(i, a)
                        d = str(float(a1) - float(a2))
                        a = a.replace("r", d, 1)
                        f = 1
                        break
        if f == 1:
            return bracket(a, 0, len(a))
        else:
            return a

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    symbols = ["(", ")", "+", "-", "*", "/", "^"]
    z = ["+", "-", "*", "/", "^"]
    c1 = ["sin", "cos", "tg", "^2", "ln", "lg"]
    c2 = ["+", "*", "/", "-", "^y", "#"]
    com = input("Введите операцию > ")
    if com == "0":
        break
    elif com in c1:
        try:
            num1 = float(input("Введите число > "))
            num2 = 0
            res = calc_case(com, num1, num2)
            print(" > ", res)
        except ValueError:
            print("Неккоректный ввод")
            continue
    elif com in c2:
        try:
            num3 = float(input("Введите число 1 > "))
            num4 = float(input("Введите число 2 > "))
            res = calc_case(com, num3, num4)
            print(" > ", res)
        except ValueError:
            print("Неккоректный ввод")
            continue
    elif com == "chain":
        s = chain(input("Введите цепочку > "))
        s = " " + s
        print(" > ", bracket(s, 0, len(s)))
    else:
        print("Нет такой операции")
        continue
