def visualize_seating(seatingsArray):
    seatings = []
    for i in seatingsArray:
        rows = i[1]
        cols = i[0]
        mat = []
        for i in range(rows):
            mat.append([0] * cols)
        seatings.append(mat)
    return seatings