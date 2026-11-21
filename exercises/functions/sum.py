def create_list(x):
    num_list=[]
    for i in range(x):
        while True:
            try:
                num=float(input(f"enter number {i+1}:"))
                num_list.append(num)
                break
            except ValueError:
                print("please enter a number like (1,2,..)")
    return num_list

def total(num_list,x):
    total=0
    for i in range(x):
            total += num_list[i]
    return total

def main():

    x=int(input("enter how many numbers you want to sum:"))
    num_list=create_list(x)
    result=total(num_list,x)
    print(f"result is: {result}")

main()