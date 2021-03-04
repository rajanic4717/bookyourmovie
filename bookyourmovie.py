import math


class BookMovie:
    global record
    global seat1
    # noinspection PyRedeclaration
    record = []
    seat1 = []

    def display_seats(self, row, seats_per_row):
        global tickets_booked
        tickets_booked=0
        print('CINEMA:')
        for i in range(row + 1):
            for j in range(seats_per_row + 1):
                if i == 0:
                    if i == j == 0:
                        print(' ', end=" ")
                        continue
                    else:
                        print(j, end=" ")
                else:
                    if i == 1 and j == 0:
                        print(' ')
                    else:
                        count = 1
                        print(i, end=" ")
                        while True:
                            if count <= seats_per_row:
                                seat_no = int(str(i) + str(count))
                                if seat_no in seat1:
                                    print('B', end=" ")
                                    tickets_booked+=1
                                else:
                                    print('S', end=" ")
                                count = count + 1
                            else:
                                print('')
                                break
                        break


    def buy_ticket(self, row, seats_per_row):
        global seat_no
        global ticket_price
        global seat_status
        row1 = int(input('Enter the row number:'))
        col1 = int(input('Enter the column number'))
        seat_no = int(str(row) + str(seats_per_row))
        seat_status = 'Available'
        for i in seat1:
            if seat_no in i:
                print('ticket already booked')
                seat_status = 'Booked'
                break
        if seat_status == 'Available':
            if row1 <= row and col1 <= seats_per_row:
                seat_no = int(str(row1) + str(col1))
                ticket_price = 0
                total_seats = row * seats_per_row
                if total_seats <= 60:
                    ticket_price = 10
                else:
                    calculation = row / 2
                    first_row = math.floor(calculation)
                    if row1 <= first_row:
                        ticket_price = 10
                    else:
                        ticket_price = 8
                print('ticket price is:', ticket_price)
                print('want to buy ticket?')
                ans2 = (input())
                if ans2 == "yes":
                    d = {}
                    name = input('name:')
                    gender = input('gender')
                    age = input('age')
                    mobileno = input('mobileno')
                    d['name'] = name
                    d['gender'] = gender
                    d['age'] = age
                    d['mobileno'] = mobileno
                    d['ticket_price']=ticket_price
                    d['row']=row
                    d['seats_per_row']=seats_per_row
                    record.append(d)
                    if d['name'] in name:
                        seat1.append(seat_no)
                    print('Booked Succesfully')
                else:
                    print('This movie has good reviews Think Again!')

    def statistics(self, row, seats_per_row):
        global total_income
        total_income = 0
        tickets_booked = len(seat1)
        print('number of purchased tickets:', tickets_booked)
        total_seats = row * seats_per_row
        percentage_ticketsbooked = (tickets_booked / total_seats) * 100
        print("Percentage of tickets booked:", str(round(percentage_ticketsbooked, 2)) + "%")

        res = []
        for key in record:
            res.append(key["ticket_price"])
        print("Current Income:", str(sum(res)), '$')
        x = row * seats_per_row
        if x <= 60:
            total_income = row * seats_per_row * 10
        else:
            x = row / 2
            row_division = math.floor(x)
            first_half_price = 10 * seats_per_row * row_division
            second_half_tickets = row * row_division
            second_half_price = 8 * seats_per_row * second_half_tickets
            total_income = first_half_price + second_half_price
        print('possible total income', "$" + str(total_income))

    def show_buyer_info(self):
        ans = input("Do you want to see the buyer info?\n")
        Ans = ans.lower()
        if Ans == "yes":
            s_row = int(input("Enter row:"))
            s_col = int(input("Enter col:"))
            seatno = int(str(s_row) + str(s_col))
            for customer_info in record:
                if customer_info:
                    print("Name:", customer_info['name'])
                    print("Gender:", customer_info['gender'])
                    print("Age:", customer_info['age'])
                    print("mobile Number:", customer_info['mobileno'])
                else:
                    print("No booking for this seat.3")

