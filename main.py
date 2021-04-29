import sys
from cinemamod import cinema

print('enter no. of rows and columns')

while True:
    No_of_rows=input()
    No_of_columns=input()
    if No_of_rows.isnumeric() and No_of_columns.isnumeric():
        No_of_rows=int(No_of_rows)
        No_of_columns = int(No_of_columns)
        if No_of_columns>0 and No_of_rows>0:
            break
        else:
            print('no. of rows and columns must be a positive integer \n try again ')
    else:
        print('no. of rows and columns must be a positive integer \n try again ')

mycinema=cinema(No_of_rows,No_of_columns)

while True:
    print('1. Show seats \n2. Buy a Ticket \n3. Statistics\n4.Show booked ticket user info\n0. exit')
    choice=input()
    if choice.isnumeric():
        choice=int(choice)

        if choice == 1:
            mycinema.show_seats()
        elif choice == 2:
            mycinema.buy_a_ticket()
        elif choice == 3:
            mycinema.statistics()
        elif choice == 4:
            mycinema.booked_ticket_user_info()
        elif choice == 0:
            sys.exit("And the cinema isn't just same without you. Please come back soon")
        else:
            print('inappropriate choice')
    else:
        print('inappropriate choice')

