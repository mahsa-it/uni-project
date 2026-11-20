def show_and_sum(x):
    total=0
    for i in range(1,x+1):
        print(i)
        total +=i
    return total
def main():
    x=int(input("enter a number:"))
    res=show_and_sum(x)
    print(f"total is:{res}")
main()