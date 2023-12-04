def main(inputs: str) -> int:
    inputs = inputs.split(" ")

    if len(inputs) != 3 or inputs[1] not in {'+', '-', '*', '/'}:
        raise ValueError

    num1, num2 = is_correct(inputs[0]), is_correct(inputs[2])

    return calc(num1, inputs[1], num2)


def is_correct(num: str) -> int:
    if "." not in num and 0 < int(num) < 10:
        return int(num)
    raise ValueError


def calc(x: int, operator: str, y: int) -> int:
    match operator:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            return int(x / y)


if __name__ == '__main__':

    while True:
        print(main(input()))
