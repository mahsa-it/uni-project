def create_list(x):
    score_list=[]
    for i in range(x):
        while True:
            try:
                score=float(input(f"enter score number {i+1}: "))
                if score >= 0:
                    score_list.append(score)
                    break
                else:
                    print("enter a vaild score not negetive.")
            
            except ValueError:
                print("please enter a number like 0, 1 ... .")
    return score_list
def average(score_list,x):
    res=0
    for num in score_list:
        res += num
    res /= x
    return res
def main():
    while True:
        try:
            x=int(input("how many grades do you have?"))
            if x > 0:
                break
            else:
                print("enter a vaild number not negetive or 0.")
        except ValueError:
                print("please enter a number like 1 ... .")
    score_list=create_list(x)
    result=average(score_list,x)
    if result >=10 :
        print(f"your average is: {result}, you pass.")
    else:
        print(f"your average is: {result}, you fail.")

main()