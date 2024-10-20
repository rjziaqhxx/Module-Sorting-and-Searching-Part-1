def Retake_exam(list):
    user_input = int(input('Which number of grade do you want to change? - '))
    user_input_grade = int(input('On which grade you want to change? - '))
    list[user_input-1] = user_input_grade

def Whether_the_student(list):
    average = sum(list)/len(list)
    if average > 10.7:
        print('The student WILL get a scholarship.')
    else:
        print('The student WILL NOT get a scholarship.')

def Output_a_sorted(list):
    nlist = list.copy()
    print('Do you want to in?','\n',
          '1. Ascending.','\n',
          '2. Descending.')
    user_input = int(input("Choose - "))
    if user_input == 1:
        n = len(nlist)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if nlist[j] > nlist[j + 1]:
                    nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                    swapped = True

            if not swapped:
                break
        print(nlist)
    if user_input == 2:
        n = len(nlist)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if nlist[j] < nlist[j + 1]:
                    nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                    swapped = True
                    
            if not swapped:
                break
        print(nlist)

def menu(list):
    print('MENU','\n',
          '1. Output grades.','\n',
          '2. Retake Exam.', '\n',
          '3. Whether the student will get a scholarship.','\n',
          '4. Output a sorted list of grades','\n',
          '5. Exit the program.')
    user_input = int(input("Choose - "))
    if user_input == 1:
        print('Your grades are - ', list)
    elif user_input == 2:
        Retake_exam(list)
    elif user_input == 3:
        Whether_the_student(list)
    elif user_input == 4:
        Output_a_sorted(list)
    elif user_input == 5:
        user_input_exit = input('Are you sure? Yes/No - ')
        if user_input_exit == 'Yes' or user_input_exit == 'yes':
            exit()
        else:
            pass

list_of_grades = []

while True:
    print("For end write 0.")
    grade = int(input('Input grade - '))
    if grade == 0:
        break
    elif grade <= 12:
        list_of_grades.append(grade)
    else:
        print('You wrote wrong number!')



while True:
    menu(list_of_grades)