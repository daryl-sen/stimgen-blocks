################################################################################
# global variables
################################################################################

# IMAGE LEVEL
image_width = 900
image_height = 500
divisions_h = 3
divisions_v = 5

margin_top = 5
margin_bot = 15
margin_left = 10
margin_right = 20

# SECTOR LEVEL
sector_width = int(image_width / divisions_h)
sector_height = int(image_height / divisions_v)

# OBJECT LEVEL
obj_width = 100
obj_height = 25


################################################################################
# functions
################################################################################

def sector_name_to_int(sector_name):
    if type(sector_name) == str:
        sector_coords = sector_name.split(",")
        sector_coords = [int(coord) for coord in sector_coords]
        return sector_coords
    else:
        return sector_name

# calculate margins associated with the sector at start point
def calc_margins(sector_name, plane):
    sector_coords = sector_name_to_int(sector_name)
    if plane == "x":
        if sector_coords[0] == 1:
            return margin_left
        elif sector_coords[0] == divisions_h:
            return margin_right
        else:
            return 0
    if plane == "y":
        if sector_coords[1] == 1:
            return margin_top
        elif sector_coords[1] == divisions_v:
            return margin_bot
        else:
            return 0

# evaluates the need for margin at end point. Use in selection_range() function only.
def eval_margins(sector_name, position, plane):
    if (position = "start" && plane == )

    if position = "start":
        if sector_coords[0] = 1:
            return calc_margins(sector_coords, "x")
        elif sector_coords[0] = divisions_h:
            return 0


def selection_range(sector_name):
    sector_coords = sector_name_to_int(sector_name)
    sel_x_start = (sector_coords[0]-1) * sector_width + calc_margins(sector_name, "x")
    sel_x_end = (sector_coords[0]) * sector_width - calc_margins(sector_name, "x")
    sel_y_start = (sector_coords[1]-1) * sector_height + calc_margins(sector_name, "y")
    sel_y_end = (sector_coords[1]) * sector_height - calc_margins(sector_name, "y")
    return {"x_start": sel_x_start, "x_end": sel_x_end, "y_start": sel_y_start, "y_end": sel_y_end}






print(selection_range("1,3"))
