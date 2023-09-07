OPERATIONS = ["+", "-", "*", "/", "%"]

def check_operation(math_operation: str) -> bool:
    if math_operation not in OPERATIONS:
        return True
    return False


def calculate(num_a, num_b, operation):
    result = eval(str(num_a) + operation + str(num_b))
    print(result)


def main():
    num_a = int(input("First number: "))
    num_b = int(input("Second number: "))
    is_valid_operation = True
    while is_valid_operation:
        operator = input(f"Select valid operation from the list: {OPERATIONS}")
        is_valid_operation = check_operation(operator)

    calculate(num_a, num_b, operator)


if __name__ == "__main__":
    main()
