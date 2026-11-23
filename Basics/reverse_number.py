
def rev_number(number):
    res = 0

    while number > 0:
        digit = number % 10
        res = res * 10 + digit
        number //= 10

    return res


def main():
    number = int(input("Enter number:"))

    print(f"Input: {number}")
    print(f"Output: {rev_number(number)}")


main()