class user:


    def __init__(self):
        self.infodict={'Name': None, 'Age': None, 'Gender':None, 'Mob.':None}

    def set_user_info(self):

        print('Enter your name')
        name=input()
        self.infodict['Name']=name

        print('Enter your age')
        while True:
            age = input()
            if age.isnumeric():
                age=int(age)
                if age>0:
                    self.infodict['Age'] = age
                    break
                else:
                    print('invalid input \t please try again')
            else:
                print('invalid input \t please try again')


        while True:
            print('choose your gender\n1.Female\n2.Male\n3.Other')
            selvalue=input()
            if selvalue.isnumeric():
                selvalue=int(selvalue)
                if selvalue==1:
                    self.infodict['Gender'] ='Female'
                    break
                elif selvalue==2:
                    self.infodict['Gender'] ='Male'
                    break
                elif selvalue==3:
                    self.infodict['Gender'] ='Other'
                    break
                else:
                    print('invalid input \t please try again')

            else:
                print('invalid input \t please try again')



        print('Enter your mob no')
        while True:
            mob = input()
            if mob.isnumeric():
                mob=int(mob)
                if mob>99999:
                    self.infodict['Mob']=mob
                    break
                else:
                    print('Contact no. should have atleast 6 digits\t please try again')
            else:
                print('invalid input \t please try again')


    def get_user_info(self):
        return self.infodict



