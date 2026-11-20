def avg(scors):
    result=0
    for i in range(5):
        result += scors[i]
    avg=result/5
    return avg

def status(avg):
    if avg > 17:
        res="aaliii"
    elif avg >= 12 and avg <= 17 :
        res="ghabol"
    else:
        res="mardood"
    return res
def main():
    scors=[]
    for i in range(5):
        num=float(input(f"enter score number{i+1}:"))
        scors.append(num)
    average=avg(scors)
    final_grade=status(average)
    print(f"youre average is {average},you are :{final_grade}")
main()