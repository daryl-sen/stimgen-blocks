import random

################################################################################
# global variables
################################################################################

# PARAMETERS
colors = ("red", "green", "blue", "yellow")

# IMAGE LEVEL
image_width = 1280
image_height = 1024
divisions_h = 4
divisions_v = 4

margin_top = 25
margin_bot = 25
margin_left = 10
margin_right = 10

# SECTOR LEVEL
sector_width = int(image_width / divisions_h)
sector_height = int(image_height / divisions_v)

# OBJECT LEVEL
obj_width = 74
obj_height = 74




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

# evaluates the need for margin. Use in selection_range() function only.
def eval_margins(sector_name, position, plane):
    sector_coords = sector_name_to_int(sector_name)
    if (position == "start" and plane == "x"):
        if sector_coords[0] == 1:
            return margin_left
        else:
            return 0
    if (position == "end" and plane == "x"):
        if sector_coords[0] == divisions_h:
            return margin_right + obj_width
        else:
            return obj_width

    if (position == "start" and plane == "y"):
        if sector_coords[1] == 1:
            return margin_top
        else:
            return 0
    if (position == "end" and plane == "y"):
        if sector_coords[1] == divisions_v:
            return margin_bot + obj_height
        else:
            return 0

def find_margins(sector_name, plane):
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


def selection_range(sector_name):
    sector_coords = sector_name_to_int(sector_name)
    sel_x_start = (sector_coords[0]-1) * sector_width + eval_margins(sector_name, "start", "x")
    sel_x_end = (sector_coords[0]) * sector_width - eval_margins(sector_name, "end", "x")
    sel_y_start = (sector_coords[1]-1) * sector_height + eval_margins(sector_name, "start", "y")
    sel_y_end = (sector_coords[1]) * sector_height - eval_margins(sector_name, "end", "y") - obj_height
    return {"x_start": sel_x_start, "y_start": sel_y_start, "x_end": sel_x_end, "y_end": sel_y_end}


def generate_obj_properties(sector_name):

    # generate coordinates for 2 half-objects
    limits = selection_range(sector_name)
    half_width = int(obj_width/2)
    obj1_x_pos = random.randint(limits['x_start'],limits['x_end'])
    obj1_y_pos = random.randint(limits['y_start'],limits['y_end'])
    obj2_x_pos = int(obj1_x_pos + half_width)

    # pick 2 colors
    color_indices = random.sample(range(0,4),2)

    # return properties for 2 subobjects
    return {
        # stimulus A
        "obj1_x_pos": obj1_x_pos,
        "obj1_y_pos": obj1_y_pos,
        "obj1_width": half_width,
        "obj1_height": obj_height,
        "obj1_color": colors[color_indices[0]],
        "obj2_x_pos": obj2_x_pos,
        "obj2_y_pos": obj1_y_pos,
        "obj2_width": half_width,
        "obj2_height": obj_height,
        "obj2_color": colors[color_indices[1]],

        # stimulus B for flipped
        "obj1_color_B": colors[color_indices[1]],
        "obj2_color_B": colors[color_indices[0]],

        # stimulus C for changed color
        "obj1_color_C": colors[random.randint(0,3)],
        "obj2_color_C": colors[random.randint(0,3)],
        }
