from visualize_seating import visualize_seating
from draw_seating import draw_seating

occupied = 0
passenger_number = 30

def aisle_seat_occupy():
    global occupied
    row = 0
    is_occupied = -1
    while occupied < passenger_number and occupied != is_occupied:
        is_occupied = occupied
        for i in range(seating_length):
            if seatings_array[i][1] > row:
                if i == 0:
                    occupied += 1
                    # filling seats from left
                    aisle_col = seatings_array[i][0] - 1
                    # modifying seatings for output
                    seatings[i][row][aisle_col] = occupied
                    if occupied >= passenger_number:
                        break
                elif i == seating_length - 1:
                    occupied += 1
                    aisle_col = 0
                    # opposite aisle seats
                    seatings[i][row][aisle_col] = occupied
                    if occupied >= passenger_number:
                        break
                else:
                    occupied += 1
                    aisle_col = 0
                    seatings[i][row][aisle_col] = occupied
                    # fills left over aisle seats
                    if occupied >= passenger_number:
                        break
                    if seatings_array[i][0] > 1:
                        occupied += 1
                        aisle_col = seatings_array[i][0] - 1
                        seatings[i][row][aisle_col] = occupied
                        if occupied >= passenger_number:
                            break
        row += 1


def window_seat_occupy():
    row = 0
    global occupied
    global passenger_number
    is_occupied = 0
    while occupied < passenger_number and occupied != is_occupied:
        is_occupied = occupied
        # filling window seats
        if seatings_array[0][1] > row:
            occupied += 1
            window_seat = 0
            seatings[0][row][window_seat] = occupied
            if occupied >= passenger_number:
                break
        if seatings_array[seating_length-1][1] > row:
            occupied += 1
            window_seat = seatings_array[seating_length-1][0] - 1
            seatings[seating_length-1][row][window_seat] = occupied
            if occupied >= passenger_number:
                break
        row += 1

def middle_seat_occupy():
    row = 0
    is_occupied = 0
    global occupied
    while occupied < passenger_number and occupied != is_occupied:
        is_occupied = occupied
        for i in range(seating_length):
            if seatings_array[i][1] > row:
                if seatings_array[i][0] > 2:
                    for col in range(1, seatings_array[i][0] - 1):
                        occupied += 1
                        seatings[i][row][col] = occupied
                        if occupied >= passenger_number:
                            break
        row += 1





#seatings_array = [[3,2], [4,3], [2,3], [3,4]]
seatings_array = [[3,4], [4,5], [2,3], [3,4]]

seatings = visualize_seating(seatings_array)
seating_length = len(seatings_array)
aisle_seat_occupy()
window_seat_occupy()
middle_seat_occupy()
draw_seating(seatings, seating_length, passenger_number, seatings_array)