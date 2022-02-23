def calculate_square_area(side):
    try:
        int_side = int(side)
    except ValueError:
        return -1
    return int_side*int_side