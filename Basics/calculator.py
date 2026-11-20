def calculate(num1,op,num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "error"
        return num1 / num2
    else:
        return "wrong op"

def main():
    try:
        num1=float(input("enter number 1:"))
        op=input("enter op:+ ,- ,* ,/:")
        num2=float(input("enter number 2:"))
        res=calculate(num1,op,num2)
        print(f"result:{res}")
    except ValueError:
        print("error: enter a valid number not character")
main()
