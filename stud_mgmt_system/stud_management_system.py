stud = {}
while True:
    print('\n')
    print('1:Adding the Student')
    print('2:Remove Student')
    print('3:Search Student')
    print('5:Exit')
    print('\n')
    ch = int(input('enter your choice:'))

    # adiing student..........................................................................................................

    if ch == 1:
        n = int(input('How Many No. Of Student To Be Added:'))
        while n > 0:
            roll = int(input('enter student roll number:'))
            stud[roll] = {}
            stud[roll]['name'] = input('enter student name:')
            stud[roll]['marks'] = {}
            stud[roll]['marks']['eng'] = int(input('enter english marks:'))
            n -= 1
        print('\n')
        print('student data:', stud)

    # removing student .........................................................................................................

    elif ch == 2:
        rn = int(input('enter roll_no of student that you want to delete:'))
        del stud[rn]
        print('\n')
        print('dictinary after removing desire student:', stud)

    # searching student and desplaying it........................................................................................

    elif ch == 3:
        rn = int(input('enetr student roll number to be search:'))
        if rn in stud:
            print('\n')
            print('student is present in database:')
            print(stud[rn])
        else:
            print('\n')
            print('student is not present in database!!!!!! PLEASE ADD STUDENT!!!!!!')

    # update student information..................................................................................................

    elif ch == 4:
        rn = int(input('enter stud roll noo.that you want to update:'))
        while True:
            print('\n 1:name \n 2:eng marks')
            print('\n')
            i = int(input('enter your update choice:'))
            if i == 1:
                stud[rn]['name'] = input('enter student new name:')
                break
            else:
                stud[rn]['marks']['eng'] = int(input('enetr student new english marks:'))
                break
        print('\n')
        print('update student info is :', stud[rn])

    # to exit from uotput..............................................................................................................

    elif ch == 5:
        break
    else:
        print('\n')
        print('you have entered invalid choice::::::')


