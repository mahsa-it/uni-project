def create_student_list(student_count):
    student_list=[]
    for i in range(student_count):
        name=input(f"enter student name {i+1}: ")
        student_list.append(name)
    return student_list

def create_grades_list(student_count,subject_list):
    grades_list=[[None] * len(subject_list) for _ in range(student_count)]
    return grades_list

def get_grade(student_list,subject_list,grade_list):
    subject_list_lower=[item.lower() for item in subject_list]
    for i in range(len(student_list)):
        print(subject_list)
        add_subject=input(f"please enter subjects name splited with ','.(math,ai,..) for {student_list[i]}: ")
        add_subject=add_subject.strip()
        add_subject=add_subject.split(",")
        add_subject=set(add_subject)
        add_subject=list(add_subject)
        add_subject=[item.lower() for item in add_subject]
        for j in range(len(add_subject)):
            add_subject[j]=add_subject[j].strip()
            if add_subject[j] == "":
                continue
            while True:
                    if add_subject[j] not in subject_list_lower:
                        print("wrong subject name.")
                        add_subject[j]=input(f"please enter correct '{add_subject[j]}'' name again.")
                        add_subject[j]=add_subject[j].strip()
                        add_subject[j]=add_subject[j].lower()
                    else:
                        break
            subject_index=subject_list_lower.index(add_subject[j])
            while True:
                try:
                    grade=float(input(f"enter {add_subject[j]} grade for {student_list[i]}:"))
                    if grade >= 0:
                        break
                    else:
                        print("grade must be 0 or bigger than 0.")
                except ValueError:
                    print("incorrect input.")
            grade_list[i][subject_index]=grade
    return grade_list
def show_student_grade(student_list,subject_list,grade_list):
    for i in range(len(student_list)):
        print(student_list[i])
        for j in range(len(subject_list)):
            print(f"{subject_list[j]} : {grade_list[i][j]}")

def add_grade(student_list,subject_list,grade_list):
        while True:
            ask=input("do you want to add more grades?yes or no.:")
            if ask == "yes":
                break
            elif ask == "no":
                return grade_list
            else:
                print("wrong input.")
        grade_list=get_grade(student_list,subject_list,grade_list)
        return grade_list

def remove_grade(student_list,subject_list,grade_list):
    while True:
            ask=input("do you want to remove any grades?yes or no.:")
            if ask == "yes":
                break
            elif ask == "no":
                return grade_list
            else:
                print("wrong input.")
    subject_list_lower=[item.lower() for item in subject_list]
    for i in range(len(student_list)):
        print(subject_list)
        remove_grade_subject=input(f"please enter subjects name splited with ','.(math,ai,..) for {student_list[i]} to remove: ")
        remove_grade_subject=remove_grade_subject.strip()
        remove_grade_subject=remove_grade_subject.split(",")
        remove_grade_subject=set(remove_grade_subject)
        remove_grade_subject=list(remove_grade_subject)
        remove_grade_subject=[item.lower() for item in remove_grade_subject]
        for j in range(len(remove_grade_subject)):
            remove_grade_subject[j]=remove_grade_subject[j].strip()
            if remove_grade_subject[j] == "":
                continue
            while True:
                    if remove_grade_subject[j] not in subject_list_lower:
                        print("wrong subject name.")
                        remove_grade_subject[j]=input(f"please enter correct '{remove_grade_subject[j]}'' name again.")
                        remove_grade_subject[j]=remove_grade_subject[j].strip()
                        remove_grade_subject[j]=remove_grade_subject[j].lower()
                    else:
                        break
            subject_index=subject_list_lower.index(remove_grade_subject[j])
            grade_list[i][subject_index]=None
    return grade_list
def show_report(student_list,subject_list,grade_list):
    for i in range(len(student_list)):
        print(student_list[i])
        for j in range(len(subject_list)):
            print(f"{subject_list[j]} : {grade_list[i][j]}")
        newlist=[]
        for k in range(len(grade_list[i])):
            if grade_list[i][k] != None:
                newlist.append(grade_list[i][k])
        if len(newlist) > 0:
            print(f"average={((sum(newlist))/(len(newlist)))}")
            print(f"highest grade : {max(newlist)}")
            print(f"lowest grade : {min(newlist)}")
        else:
            print("no grades avalable.")
def main():
    while True:
        try:
            student_count=int(input("how many students you want to add grades for? :"))
            if student_count >=1 :
                break
            else:
                print("incorrect input. it should be 1 or more.")
        except ValueError:
            print("please enter a number.")
    subject_list=["Math", "AI","Data base","Python"]
    student_list=create_student_list(student_count)
    print(f"student list : {student_list}")
    grade_list=create_grades_list(student_count,subject_list)
    grade_list=get_grade(student_list,subject_list,grade_list)
    show_student_grade(student_list,subject_list,grade_list)
    grade_list=add_grade(student_list,subject_list,grade_list)
    show_student_grade(student_list,subject_list,grade_list)
    grade_list=remove_grade(student_list,subject_list,grade_list)
    show_report(student_list,subject_list,grade_list)

main()