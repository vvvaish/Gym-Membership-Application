class op:
    def __init__(self):
        self.dict1 = {}
        self.dict2 = {}
        self.dict2['bmi<18.5'] = ['Chest','Biceps','Rest','Back','Triceps','Rest','Rest']
        self.dict2['bmi<25'] = ['Chest','Biceps','Cardio/Abs','Back','Triceps','Legs','Rest']
        self.dict2['bmi<30'] = ['Chest','Biceps','Abs/Cardio','Back','Triceps','Legs','Cardio']
        self.dict2['bmi>30'] = ['Chest','Biceps','Cardio','Back','Triceps','Cardio','Cardio']
    def create_member(self):
        self.dict1 = {}
        x = {}
        a = input('Enter Full Name: ')
        b = input('Enter Age: ')
        c = input('Enter Gender: ')
        d = input('Enter Mob No: ')
        e = input('Enter Email: ')
        f = input('Enter BMI: ')
        g = input('Enter Membership Duration: ')
        x['name'] = a
        x['age'] = b
        x['gender'] = c
        x['mob_no'] = d
        x['email'] = e
        x['bmi'] = f
        x['duration'] = g
        self.dict1[d] = x
    def view_member(self):
        x = input('Enter Mob No: ')
        y = ['Name: ','Age: ','Gender: ','Mob No: ','Email: ','BMI: ','Membership Duration: ']
        z = 0
        if x not in self.dict1 or len(self.dict1) == 0:
            print('Member Not Present!')
            return
        for i in self.dict1[x]:
            print(y[z],self.dict1[x][i])
            z += 1
    def delete_member(self):
        x = input('Enter Mob No: ')
        if x not in self.dict1 or len(self.dict1) == 0:
            print('No Member with ',x,' Mob no in Gym')
            return
        self.dict1.pop(x)
        print('Member Successfully Deleted... ')
    def update_member(self):
        x = input('Enter Mob No: ')
        if x not in self.dict1 or len(self.dict1) == 0:
            print('Member not Present!')
            return
        y = input('Enter Duration to Update: ')
        self.dict1[x]['duration'] = y
        print('Membership Successfully Updated...')
    def create_reg(self):
        print('1. Create Regimen for BMI < 18.5')
        print('2. Create Regimen for BMI < 25')
        print('3. Create Regimen for BMI < 30')
        print('4. Create Regimen for BMI > 30')
        x = input('Enter Your Choice: ')

        if x == '1':
            y = []
            a = input('Mon: ')
            b = input('Tue: ')
            c = input('Wed: ')
            d = input('Thu: ')
            e = input('Fri: ')
            f = input('Sat: ')
            g = input('Sun: ')
            y.append(a)
            y.append(b)
            y.append(c)
            y.append(e)
            y.append(f)
            y.append(g)
            self.dict2['bmi<18.5'] = y
            print('')
            print('Regimen Created Successfully...')
        elif x == '2':
            y1 = []
            a1 = input('Mon: ')
            b1 = input('Tue: ')
            c1 = input('Wed: ')
            d1 = input('Thu: ')
            e1 = input('Fri: ')
            f1 = input('Sat: ')
            g1 = input('Sun: ')
            y1.append(a1)
            y1.append(b1)
            y1.append(c1)
            y1.append(e1)
            y1.append(f1)
            y1.append(g1)
            self.dict2['bmi<25'] = y1
            print('')
            print('Regimen Created Successfully...')
        elif x == '3':
            y2 = []
            a2 = input('Mon: ')
            b2 = input('Tue: ')
            c2 = input('Wed: ')
            d2 = input('Thu: ')
            e2 = input('Fri: ')
            f2 = input('Sat: ')
            g2 = input('Sun: ')
            y2.append(a2)
            y2.append(b2)
            y2.append(c2)
            y2.append(e2)
            y2.append(f2)
            y2.append(g2)
            self.dict2['bmi<30'] = y2
            print('')
            print('Regimen Created Successfully...')
        elif x == '4':
            y3 = []
            a3 = input('Mon: ')
            b3 = input('Tue: ')
            c3 = input('Wed: ')
            d3 = input('Thu: ')
            e3 = input('Fri: ')
            f3 = input('Sat: ')
            g3 = input('Sun: ')
            y3.append(a3)
            y3.append(b3)
            y3.append(c3)
            y3.append(e3)
            y3.append(f3)
            y3.append(g3)
            self.dict2['bmi>30'] = y3
            print('')
            print('Regimen Created Successfully...')
        else:
            print('Invalid Choice!!!')

    def view_reg(self):
        print('1. View Regimen for BMI < 18.5')
        print('2. View Regimen for BMI < 25')
        print('3. View Regimen for BMI < 30')
        print('4. View Regimen for BMI > 30')
        x = input('Enter Your Choice: ')
        y = ['Mon: ','Tue: ','Wed: ','Thu: ','Fri: ','Sat: ','Sun: ']
        z = 0
        print('')
        if x == '1':
            if 'bmi<18.5' not in self.dict2:
                print('Regimen Not Present!')
                return
            print('Regimen for BMI < 18.5 ')
            for i in self.dict2['bmi<18.5']:
                print(y[z],i)
                z += 1
        elif x == '2':
            if 'bmi<25' not in self.dict2:
                print('Regimen Not Present!')
                return
            print('Regimen for BMI < 25 ')
            for i in self.dict2['bmi<25']:
                print(y[z],i)
                z += 1
        elif x == '3':
            if 'bmi<30' not in self.dict2:
                print('Regimen Not Present!')
                return
            print('Regimen for BMI < 30 ')
            for i in self.dict2['bmi<30']:
                print(y[z],i)
                z += 1
        elif x == '4':
            if 'bmi>30' not in self.dict2:
                print('Regimen Not Present!')
                return
            print('Regimen for BMI > 30 ')
            for i in self.dict2['bmi>30']:
                print(y[z],i)
                z += 1
        else:
            print('Invalid Choice!!!')


    def delete_reg(self):
        print('1. Delete Regimen for BMI < 18.5')
        print('2. Delete Regimen for BMI < 25')
        print('3. Delete Regimen for BMI < 30')
        print('4. Delete Regimen for BMI > 30')
        x = input('Enter Your Choice: ')

        if x == '1':
            if 'bmi<18.5' not in self.dict2:
                print('Regimen Not Present!')
                return
            self.dict2.pop('bmi<18.5')
            print('Regimen Deleted Successfully...')
        elif x == '2':
            if 'bmi<25' not in self.dict2:
                print('Regimen Not Present!')
                return
            self.dict2.pop('bmi<25')
            print('Regimen Deleted Successfully...')
        elif x == '3':
            if 'bmi<30' not in self.dict2:
                print('Regimen Not Present!')
                return
            self.dict2.pop('bmi<30')
            print('Regimen Deleted Successfully...')
        elif x == '4':
            if 'bmi>30' not in self.dict2:
                print('Regimen Not Present!')
                return
            self.dict2.pop('bmi>30')
            print('Regimen Deleted Successfully...')
        else:
            print('Invalid Choice!!!')
    def update_reg(self):
        print('1. Update Regimen for BMI < 18.5')
        print('2. Update Regimen for BMI < 25')
        print('3. Update Regimen for BMI < 30')
        print('4. Update Regimen for BMI > 30')
        x = input('Enter Your Choice: ')
        y = int(input('Enter DayCount: '))
        z = input('Regimen for DayCount: ')
        print('')
        if x == '1':
            if 'bmi<18.5' not in self.dict2:
                print('Regimen Not Present!')
                return
            self.dict2['bmi<18.5'][y] = z
            print('Regimen Updated Successfully...')
        elif x == '2':
            if 'bmi<25' not in self.dict2:
                print('Regimen Not Present!')
                return
            self.dict2['bmi<25'][y] = z
            print('Regimen Updated Successfully...')
        elif x == '3':
            if 'bmi<30' not in self.dict2:
                print('Regimen Not Present!')
                return
            self.dict2['bmi<30'][y] = z
            print('Regimen Updated Successfully...')
        elif x == '4':
            if 'bmi>30' not in self.dict2:
                print('Regimen Not Present!')
                return
            self.dict2['bmi>30'][y] = z
            print('Regimen Updated Successfully...')
        else:
            print('Invalid Choice!!!')



    def my_reg(self):
        x = input('Enter Mob No: ')
        if x not in self.dict1 or len(self.dict1) == 0:
            print('Member Having Mob No', x, 'Is Not Present!!!')
            return
        y1 = float(self.dict1[x]['bmi'])
        y = ['Mon: ', 'Tue: ', 'Wed: ', 'Thu: ', 'Fri: ', 'Sat: ', 'Sun: ']
        z = 0
        if y1 < 18.5:
            for i in self.dict2['bmi<18.5']:
                print(y[z], i)
                z += 1
        elif y1 < 25:
            for i in self.dict2['bmi<25']:
                print(y[z], i)
                z += 1
        elif y1 < 30:
            for i in self.dict2['bmi<30']:
                print(y[z], i)
                z += 1
        else:
            for i in self.dict2['bmi>30']:
                print(y[z], i)
                z += 1

    def my_profile(self):

        x = input('Enter Your Mob No: ')
        if x not in self.dict1:
            print('Member Having Mob No',x,'Is Not Present!!! ')
            return
        y = ['Name:', 'Age:', 'Gender:', 'Mob No:', 'Email:', 'BMI:', 'Membership Duration:']
        z = 0
        for i in self.dict1[x]:
            print(y[z], self.dict1[x][i])
            z += 1




