from seatmod import seat
class cinema:

    def __init__(self,rows,columns):
        self.trows = rows
        self.tcolumns = columns
        self.current_income = 0
        self.total_income = 0
        self.tickets_sold = 0
        self.seat_grid = {}
        for i in range(1,rows+1):
            for j in range(1,columns+1):
                self.seat_grid[(100*i)+j]=seat(rows,columns,i,j)        # multiplying row number by 100 so that more than 9 columns can be given unique key in seat_grid dictionary
                self.total_income+=self.seat_grid[(100 * i) + j].Price

    def show_seats(self):
        print(' ',end='  ')
        for k in range(1, self.tcolumns + 1):
            print(k,end='  ')
        print()
        for i in range(1,self.trows+1):
            print(i,end='  ')
            for j in range(1,self.tcolumns+1):
                if self.seat_grid[(100*i)+j].Availability==True:
                    print('S',end='  ')
                else:
                    print('B',end='  ')
            print()

    def buy_a_ticket(self):
        print('enter row number and column no. of ticket you are booking')
        while True:
            br = input()
            bc = input()
            if br.isnumeric() and bc.isnumeric():
                br = int(br)
                bc = int(bc)
                if br > 0 and bc > 0 and br<=self.trows and bc<=self.tcolumns:
                    break
                else:
                    print('invalid choice \n try again ')
            else:
                print('invalid choice \n try again ')

        if self.seat_grid[(100 * br) + bc].Availability==False:
            print('seat is already reserved')
            return

        print('cost of slected seat is $',self.seat_grid[(100 * br) + bc].Price)
        print('press 1 to continue booking the selected seat')
        choice=int(input())
        if choice==1:
            self.seat_grid[(100 * br) + bc].bookseat(br,bc)
            self.current_income+=self.seat_grid[(100 * br) + bc].Price
            self.tickets_sold+=1
            print('Booked Successfully')
        else:
            return

    @staticmethod
    def percent(a,b):
        return (a/b)*100


    def statistics(self):
        print('Number of purchased tickets:',self.tickets_sold)
        percnt=cinema.percent(self.tickets_sold,len(self.seat_grid))
        print('Percentage:',percnt)
        print('Current income:$',self.current_income)
        print('Total income:$',self.total_income)

    def booked_ticket_user_info(self):
        print('enter row number and column no. of ticket you are booking')
        while True:
            r = input()
            c = input()
            if r.isnumeric() and c.isnumeric():
                r = int(r)
                c = int(c)
                if r > 0 and c > 0 and r <= self.trows and c <= self.tcolumns:
                    break
            else:
                print('invalid choice \n try again ')
        if self.seat_grid[(100 * r) + c].Availability==False:
            infod=self.seat_grid[(100 * r) + c].user_list[(r * 100) + c].get_user_info()
            print('Name:',infod['Name'])
            print('Gender:',infod['Gender'])
            print('Age:',infod['Age'])
            print('Price:',self.seat_grid[(100 * r) + c].Price)
            print('Phone No.:',infod['Mob'])
        else:
            print("Seat isn't booked yet")
            return

