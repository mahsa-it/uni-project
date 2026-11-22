def multiplication_table(number):
    print("result:")
    for i in range(1,11):
        print(f"{i}*{number}={i*number}")
def main():
    while True:
        try:
            number=int(input("please enter a number:"))
            break
        except ValueError:
            print("please enter a number(like 1,2,...):")
    multiplication_table(number)
main()
