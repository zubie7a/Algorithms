# https://app.codesignal.com/company-challenges/uber/XHNFMPBYsqNyhx9PP
def parkingSpot(car_dimensions, parking_lot, lucky_spot):

    # Check that the lucky spot is empty, otherwise we can't park.
    lucky_x1, lucky_y1, lucky_x2, lucky_y2 = lucky_spot
    for i in range(lucky_x1, lucky_x2 + 1):
        for j in range(lucky_y1, lucky_y2 + 1):
            if parking_lot[i][j] != 0:
                return False
    # If it has gotten to this point, the lucky spot is clear
    # BUT we have to make sure we can reach it. According to the
    # long side of the car, it can move either vertically or 
    # horizontally only.
    orientation = "horizontal"
    width = lucky_y2 - lucky_y1
    height = lucky_x2 - lucky_x1
    if height > width:
        orientation = "vertical"

    # Check that from either side of the lucky spot depending on the
    # orientation, all the cells are free until the other side.
    if orientation == "horizontal":
        # Assume both sides are clear, and then seek to invalidate
        # this assumption by finding one non clear cell on either side.
        all_empty_left = True
        all_empty_right = True
        # Check the left side.
        for i in range(lucky_x1, lucky_x2 + 1):
            for j in range(0, lucky_y1):
                if parking_lot[i][j] != 0:
                    all_empty_left = False

        # Check the right side.
        parking_width = len(parking_lot[0])
        for i in range(lucky_x1, lucky_x2 + 1):
            for j in range(lucky_y2 + 1, parking_width):
                if parking_lot[i][j] != 0:
                    all_empty_right = False

        return (all_empty_left or all_empty_right)

    else:
        # Assume both sides are clear, and then seek to invalidate
        # this assumption by finding one non clear cell on either side.
        all_empty_up = True
        all_empty_down = True

        # Check the up side.
        for i in range(lucky_y1, lucky_y2 + 1):
            for j in range(0, lucky_x1):
                if parking_lot[i][j] != 0:
                    all_empty_up = False

        # Check the down side.
        parking_height = len(parking_lot)
        for i in range(lucky_y1, lucky_y2 + 1):
            for j in range(lucky_x2 + 1, parking_height):
                if parking_lot[i][j] != 0:
                    all_empty_down = False

        return (all_empty_up or all_empty_down)
