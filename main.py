from bookyourmovie import BookMovie
global row
global seats_per_row
print('enter the no of rows:')
if __name__ == '__main__':
    row = int(input())
print('enter the number of seats per row')
if __name__ == '__main__':
    seats_per_row = int(input())
while True:
    print('options')
    print('1:show me seats')
    print('2:buy a ticket')
    print("3:statistics")
    print('4:show booked ticket user info')
    print('0: Exit')
    ans = int(input())

    obj = BookMovie()

    if ans == 1:
        obj.display_seats(row, seats_per_row)
    elif ans == 2:
        obj.buy_ticket(row, seats_per_row)
    elif ans == 3:
        obj.statistics(row, seats_per_row)
    elif ans == 4:
        obj.show_buyer_info()
    elif ans == 0:
        print('Thanks For Visiting')
        break
