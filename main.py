import operations
print('')
print('')
print('********** Gym Membership Application **********')
x = True
obj = operations.op()
while x:
    print('')
    print('1. Login As Superuser')
    print('2. Login As Member')
    print('3. Exit')
    ch1 = input('Enter Your Choice: ')
    print('********************')
    if ch1 == '1':
        y = True
        while y:
            print('')
            print('1. Create Member')
            print('2. View Member')
            print('3. Delete Member')
            print('4. Update Member')
            print('5. Create Regimen')
            print('6. View Regimen')
            print('7. Delete Regimen')
            print('8. Update Regimen')
            print('9. Exit')
            ch2 = input('Enter Your Choice: ')
            print('********************')
            print('')
            if ch2 == '1':
                obj.create_member()
            elif ch2 == '2':
                obj.view_member()
            elif ch2 == '3':
                obj.delete_member()
            elif ch2 == '4':
                obj.update_member()
            elif ch2 == '5':
                obj.create_reg()
            elif ch2 == '6':
                obj.view_reg()
            elif ch2 == '7':
                obj.delete_reg()
            elif ch2 == '8':
                 obj.update_reg()
            elif ch2 == '9':
                y = False
            else:
                print('Invalid Choice!!!')

    elif ch1 == '2':
        z = True
        while z:
            print('')
            print('1. My Regimen')
            print('2. My Profile')
            print('3. Exit')
            ch3 = input('Enter Your Choice: ')
            print('********************')
            if ch3 == '1':
                obj.my_reg()
            elif ch3 == '2':
                obj.my_profile()
            elif ch3 == '3':
                z = False
            else:
                print('Invalid Choice!!!')
    elif ch1 == '3':
        x = False
    else:
        print('Invalid Choice!!!')

