def draw_seating(seats,length,number,seatingsArray):
    space_size = len(str(number))
    col2 = [x[1] for x in seatingsArray]
    col1 = [x[0] for x in seatingsArray]
    maximum = max(col2)

    for i in range(maximum):
        print_row = []
        for j in range(length):
            row = ' '
            if len(seats[j]) <= i:
                for k in range(col1[j]):
                    row += ' ' * space_size
                    row += ' '
            else:
                row = ' '
                for k in seats[j][i]:
                    row += str(k) + (' ' * (space_size - len(str(k))))
                    row += ','

            print_row.append(row)
        print('    '.join(print_row))
