### Import built-in libraries
import math
import os
import random
import sys
import time
import turtle


# Define the line variables to be used when printing output
big_line = "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
line = "—————————————————————————————————————————————————————————————————————————————————————————————————————————————————"


### Define functions

def clear_terminal():
    """Clear user terminal after checking their operating system, to make sure the command is correct
    """

    if sys.platform == "linux" or sys.platform == "linux2": # Linux
        os.system("clear")

    elif sys.platform == "darwin": # Apple / Mac
        os.system("clear")

    elif sys.platform == "win32": # Windows
        os.system("cls")

    else:
        os.system("cls")  # Execute "cls" is cannot determine the oeprating system
    
    return


def shuffle_list(lst):
    """Take a list and returned a shuffled version of it.
    """
    lst_indexes = list(range(0, len(lst)))  # Get a list of all indexes of the given list (lst).
    random.shuffle(lst_indexes)  # Shuffle the list of indexes.

    shuffled_list = []  # Initialise the list where the shuffled items will be added to.
    for index in lst_indexes:  # Loop through the list of indexes.
        shuffled_list.append(lst[index])  # Append the item assigned to the random index into the shuffled list.
    
    return shuffled_list


def colour(text, colour):
    """Return an escape-formatted version of a given string, to add colour to it when printed.
    """
    
    # Initialise start and end escape values (to make it easier to change in the future)
    esc_val = "\033"
    esc_val_end = f"{esc_val}[00m"  # the "[00m" at the end ensures that the trailing text (that was not part of the input)
                                    # is reset to the default colour (white)

    text = str(text)
    # Use selection to determine what is the formatted version of the text to be ouputted
    # Format the text using f-string, putting escape value and ANSI value next to the text
    if colour == "red":
        text = f"{esc_val}[1;31m{text}{esc_val_end}"  # ANSI value for light red [1;31m

    elif colour == "green":
        text = f"{esc_val}[1;32m{text}{esc_val_end}"  # ANSI value for light green [1;32m

    elif colour == "blue":
        text = f"{esc_val}[1;34m{text}{esc_val_end}"  # ANSI value for light blue [1;34m

    elif colour == "yellow":
        text = f"{esc_val}[1;33m{text}{esc_val_end}"  # ANSI value for yellow [1;33m

    elif colour == "pink":
        text = f"{esc_val}[38;5;206m{text}{esc_val_end}"  # ANSI value for pink [38;5;206ms

    elif colour == "bold":
        text = f"{esc_val}[1m{text}{esc_val_end}"  # ANSI value to make text bold [1m

    elif colour == "bold_underline":
        text = f"{esc_val}[1;4m{text}{esc_val_end}"  # Combine ANSI value for underline ([4m) and bold ([1m)

    return text


# With the colours() function defined, initiate the end statement for when the program ends
end_statement = f"\n   [{colour('END', 'red')}] Goodbye {colour(':)', 'red')}"  # Print "[END] Goodbye :)", where the 'END' is in red, and the ':)' is in yellow


def convert_colour_to_turtle(colour):
    """Convert human-readable colour names to names which Turtle (from Python) can understand and draw out.
    """

    if colour == "red":
        turtle_colour  = "firebrick1"  # firebrick1 is the shade of red that fits my turtle animation best

    elif colour == "green":
        turtle_colour = "lawngreen"  # lawngreen is the shade of green that fits my turtle animation best

    elif colour == "blue":
        turtle_colour = "DodgerBlue"  # DodgerBlue is the shade of blue that fits my turtle animation best

    elif colour == "yellow":
        turtle_colour = "khaki1"  # khaki1 is the shade of yellow that fits my turtle animation best

    elif colour == "pink":
        turtle_colour = "hotpink"  # hotpink is the shade of pink that fits my turtle animation best

    return turtle_colour



def check_triangle_valid(a, b, c):
    """Return a dict of whether a triangle is valid, when given lengths of sides a, b, c, and why it is or is not valid.
    """ 

    # Initialise a dictionary, where key = the two sides that are summed.
    #                              value = Boolean of whether the sum of the two sides is greater than the third side.
    sum_of_two_sides_greater_than_third = {
        "sideAB" : a + b > c,
        "sideAC" : a + c > b,
        "sideBC" : b + c > a
    }

    # Initialise the dictionary that will be outputted by the function.
    output_dict = {
        "valid" : False not in sum_of_two_sides_greater_than_third.values(),  # Boolean of whether "False" does NOT exist in the sum_of_two_sides_greater_than_third dictionary.
                                                                              # True = valid triangle, False = invalid triangle.
        "reason" : None,  # Initial value set to None.
    }

    # Initiate the output statements in their respective colours to not make the f-string in later outputs too cluttered.
    invalid_text = colour("INVALID", "red")  # Set INVALID to red colour
    valid_text = colour("VALID", "green")  # Set VALID to green colour

    # Store the float and int types in a list.
    acceptable_types = [type(float()), type(int())] 

    # Check if any of the inputs (side A or B or C) is neither a float, nor an int.
    if type(a) not in acceptable_types or type(b) not in acceptable_types or type(c) not in acceptable_types:
        output_dict["valid"] = False  # Set the value of the "valid" key in the dictionary to False
        output_dict["reason"] = f"\n[{invalid_text}] One of the inputs is not a number, please try again.\n\n{line}\n\n"  # Set the value of the "reason" key to the text
        return output_dict  # End the function and return the dictionary
    
    
    # Shuffle the list of valid examples of triangles.
    examples_of_valid_triangle = shuffle_list(["(3, 4, 5)", "(12, 16, 15)", "(52, 50, 65)", "(102, 75, 50)"])

    # If the triangle is valid, provide the reason why
    if output_dict["valid"] == True:
        output_dict["reason"] = f" \n[{valid_text}] The sum of any two sides of a triangle is greater than the third side."
        return output_dict

    else:  # Find which of the two sides does not add up to be greater than the third.
        for equation in sum_of_two_sides_greater_than_third:
            if sum_of_two_sides_greater_than_third[equation] == False:  # Check if the equation was marked invalid.
                if equation == "sideAB":  # If the equation was sideA + sideB, set the reason for invalidity to...
                    output_dict["reason"] = f"\n[{invalid_text}] The sum of Side A and Side B is NOT GREATER than Side C. Example of a valid triangle: {examples_of_valid_triangle[0]}\n\n{line}\n"
                    return output_dict
                
                elif equation == "sideAC":  # If the equation was sideA + sideC, set the reason for invalidity to...
                    output_dict["reason"] = f"\n[{invalid_text}] The sum of Side A and Side C is NOT GREATER than Side B. Example of a valid triangle: {examples_of_valid_triangle[0]}\n\n{line}\n"
                    return output_dict
                
                elif equation == "sideBC":  # If the equation was sideB + sideC, set the reason for invalidity to...
                    output_dict["reason"] = f"\n[{invalid_text}] The sum of Side B and Side C is NOT GREATER than Side A. Example of a valid triangle: {examples_of_valid_triangle[0]}\n\n{line}\n"
                    return output_dict


def get_triangle_sides():
    """Get the user's input on the three sides of the triangle and store it into a dictionary.
    """

    # Initialise the output dictionary
    sides_length_dict = {
      "A" : None,
      "B" : None,
      "C" : None 
    }
    
    print(f"  [{colour('Note', 'bold')}] In order for me to draw your triangle, it has to satisfy the Triangle Inequality Law - which states that")
    print("         the sum of any two sides of a triangle should be greater the third side (a + b > c, a + c > b, b + c > a)\n")

    # Loop through each of the three sides of a triangle
    for side_name in ["A", "B", "C"]:
      # Get input on one side
      triangle_side = input(f"[SIDE {side_name}] Please input the length of side {side_name} of your triangle as a number. Enter in 'q' or 'quit to exit: ")
      
      # Try to convert the input of the user into a float
      try:
        triangle_side = float(triangle_side)
        sides_length_dict[side_name] = triangle_side
    
      # If it doesn't work...
      except:
        # Quit the program
        if triangle_side.lower() == "q" or triangle_side.lower() == "quit":
          print(end_statement)
          return "user_quit"
        
        # If user does not quit, keep looping the input
        while triangle_side.lower() != "q" or triangle_side.lower() == "quit":
          triangle_side = input(f"[SIDE {side_name}] Your previous input was not a number. Please input side {side_name} again, or enter in 'q' or 'quit to exit: ")
          
          # Try to turn the input into a float again, and loop back to the re-input prompt if input is still not a number
          try:
            triangle_side = float(triangle_side)
            sides_length_dict[side_name] = triangle_side
            break  # Break out from the current while loop (not out of the parent for loop) iteration here
          
          # If the user wants to quit, quit the program.
          except:
            if triangle_side.lower() == "q" or triangle_side.lower() == "quit":
              print(end_statement)
              return "user_quit"  # End the function here
      
      # Let user know that their input has been saved
      print(f"> Saved: side {side_name} = {triangle_side}")

    return sides_length_dict


def calculate_triangle_angles(a, b, c):
    """Calculate the angles of a triangle, given its three sides, using the cosine rule.
    """
    angle_BC = math.acos((b**2 + c**2 - a**2) / (2 * b * c))  # Use cosine rule to find angle between side A and B
    angle_AC = math.acos((a**2 + c**2 - b**2) / (2 * a * c))  # Use cosine rule to find angle between side A and C
    angle_AB = math.acos((a**2 + b**2 - c**2) / (2 * a * b))  # Use cosine rule to find angle between side B and C
    
    # Return a list of the angles, (convert the angles from radians into degrees using math.degrees)
    return [math.degrees(angle_AB), math.degrees(angle_BC), math.degrees(angle_AC)]


def determine_triangle_type(side_a, side_b, side_c):
    """Determine what is the type of triangle that was given, by comparing the three sides.
    """

    # Initialise the output dictionary
    output_dict = {
        "triangle_type" : None,
        "reason" : None
    }
    
    # If all sides are equal, save the triangle type as equilateral, and say it is because all sides are the same
    if side_a == side_b == side_c:
        output_dict["triangle_type"] = "an Equilateral"
        output_dict["reason"] = "All sides (and all angles) are the same."
    
    # If only sideA and sideB are equal, save the triangle types as isosceles, and say it is because Side A and Side B are equal
    elif side_a == side_b and side_b != side_c:
        output_dict["triangle_type"] = "an Isosceles"
        output_dict["reason"] = "Side A = Side B"

    # If only sideA and sideC are equal, save the triangle types as isosceles, and say it is because Side A and Side C are equal
    elif side_a == side_c and side_c != side_b:
        output_dict["triangle_type"] = "an Isosceles"
        output_dict["reason"] = "Side A = Side C"

    # If only sideB and sideC are equal, save the triangle types as isosceles, and say it is because Side B and Side C are equal
    elif side_b == side_c and side_c != side_a:
        output_dict["triangle_type"] = "an Isosceles"
        output_dict["reason"] = "Side B = Side C"

    # If none of the sides are equal, save the triangle types as scalene, and say it is because NONE of the sides are equal
    else:
        output_dict["triangle_type"] = "a Scalene"
        output_dict["reason"] = "None of the sides are equal."                

    return output_dict



def show_angle_formulas(side_a, side_b, side_c, colours_used):
    """Show the user what were the formulas used to calculate the angles between the three sides of their triangle.
    """

    # Initialise the variables that store the angle label (e.g. angleAB) in colour, matching with the colour of the side
    coloured_angle_AC = f'angle{colour(f"A", colours_used["side_a"])}{colour(f"C", colours_used["side_c"])}'
    coloured_angle_AB = f'angle{colour(f"A", colours_used["side_a"])}{colour(f"B", colours_used["side_b"])}'
    coloured_angle_BC = f'angle{colour(f"B", colours_used["side_b"])}{colour(f"C", colours_used["side_c"])}'
    
    # Initialise the variables that store the side text (e.g. sideA) in colour, matching with the colour of the side
    coloured_side_a_text = colour("sideA", colours_used["side_a"])
    coloured_side_b_text = colour("sideB", colours_used["side_b"])
    coloured_side_c_text = colour("sideC", colours_used["side_c"])

    # Initialise the variables that store the side number (e.g. 12) in colour, matching with the colour of the side
    coloured_side_a_num = colour(side_a, colours_used["side_a"])
    coloured_side_b_num = colour(side_b, colours_used["side_b"])
    coloured_side_c_num = colour(side_c, colours_used["side_c"])

    # Initialise the variables that store the squared value of all the side lengths
    side_a_squared = side_a ** 2
    side_b_squared = side_b ** 2
    side_c_squared = side_c ** 2

    # Initialise the variables that store the squared value of the side lengths (e.g. 144) in colour, matching with the colour of the side
    coloured_side_a_squared = colour(side_a_squared, colours_used["side_a"])
    coloured_side_b_squared = colour(side_b_squared, colours_used["side_b"])
    coloured_side_c_squared = colour(side_c_squared, colours_used["side_c"])

    ## FORMULAS:
    # angle_AB = math.acos((a**2 + b**2 - c**2) / (2 * a * b))  # Use cosine rule to find angle between side B and C
    # angle_AC = math.acos((a**2 + c**2 - b**2) / (2 * a * c))  # Use cosine rule to find angle between side A and C
    # angle_BC = math.acos((b**2 + c**2 - a**2) / (2 * b * c))  # Use cosine rule to find angle between side A and B

    
    ## Print out the formatted and coloured formula for angle AB, going step by step, algebraically 
    ## Here is what the output would look like for the user (without colour), given sideA, sideB, sideC all equal 1
    # Since cos(angleAB) = (sideA² + sideB ² - sideC²) ÷ (2 x sideA x sideB)
    #       cos(angleAB) = (1² + 1² - 1²) ÷ (2 x 1 x 1)
    #       cos(angleAB) = (1 + 1 - 1) ÷ 2
    #           angleAB  = cos⁻¹(0 ÷ 2)
    #           angleAB  = cos⁻¹(0)
    # therefore angleAB  = 1°
    print(f"""
Since cos({coloured_angle_AB}) = ({coloured_side_a_text}² + {coloured_side_b_text}² - {coloured_side_c_text}²) ÷ (2 x {coloured_side_a_text} x {coloured_side_b_text})
      cos({coloured_angle_AB}) = ({coloured_side_a_num}² + {coloured_side_b_num}² - {coloured_side_c_num}²) ÷ (2 x {coloured_side_a_num} x {coloured_side_b_num})
      cos({coloured_angle_AB}) = ({coloured_side_a_squared} + {coloured_side_b_squared} - {coloured_side_c_squared}) ÷ {2 * side_a * side_b}
          {coloured_angle_AB}  = cos⁻¹({(side_a_squared + side_b_squared - side_c_squared)} ÷ {2 * side_a * side_b})
          {coloured_angle_AB}  = cos⁻¹({(side_a_squared + side_b_squared - side_c_squared) / (2 * side_a * side_b)})
therefore {coloured_angle_AB} = {round(angle_AB, 2)}°""")
    time.sleep(0.75)  # Wait for 0.75 seconds


    ## Print out the formatted and coloured formula for angle AC, going step by step, algebraically
    ## Here is what the output would look like for the user (without colour), given sideA, sideB, sideC all equal 1
    # Since cos(angleAC) = (sideA² + sideC ² - sideC²) ÷ (2 x sideA x sideC)
    #       cos(angleAC) = (1² + 1² - 1²) ÷ (2 x 1 x 1)
    #       cos(angleAC) = (1 + 1 - 1) ÷ 2
    #           angleAC  = cos⁻¹(0 ÷ 2)
    #           angleAC  = cos⁻¹(0)
    # therefore angleAC  = 1°
    print(f"""
Since cos({coloured_angle_AC}) = ({coloured_side_a_text}² + {coloured_side_c_text}² - {coloured_side_b_text}²) ÷ (2 x {coloured_side_a_text} x {coloured_side_c_text})
      cos({coloured_angle_AC}) = ({coloured_side_a_num}² + {coloured_side_c_num}² - {coloured_side_b_num}²) ÷ (2 x {coloured_side_a_num} x {coloured_side_c_num})
      cos({coloured_angle_AC}) = ({coloured_side_a_squared} + {coloured_side_c_squared} - {coloured_side_b_squared}) ÷ {2 * side_a * side_c}
          {coloured_angle_AC}  = cos⁻¹({(side_a_squared + side_c_squared - side_b_squared)} ÷ {2 * side_a * side_c})
          {coloured_angle_AC}  = cos⁻¹({(side_a_squared + side_c_squared - side_b_squared) / (2 * side_a * side_c)})
therefore {coloured_angle_AC}  = {round(angle_AC, 2)}°""")
    time.sleep(0.75)  # Wait for 0.75 seconds


    ## Print out the formatted and coloured formula for angle AC, going step by step, algebraically
    ## Here is what the output would look like for the user (without colour), given sideA, sideB, sideC all equal 1
    # Since cos(angleBC) = (sideB² + sideC ² - sideA²) ÷ (2 x sideB x sideC)
    #       cos(angleBC) = (1² + 1² - 1²) ÷ (2 x 1 x 1)
    #       cos(angleBC) = (1 + 1 - 1) ÷ 2
    #           angleBC  = cos⁻¹(0 ÷ 2)
    #           angleBC  = cos⁻¹(0)
    # therefore angleBC  = 1°
    print(f"""
Since cos({coloured_angle_BC}) = ({coloured_side_b_text}² + {coloured_side_c_text}² - {coloured_side_a_text}²) ÷ (2 x {coloured_side_b_text} x {coloured_side_c_text})
      cos({coloured_angle_BC}) = ({coloured_side_b_num}² + {coloured_side_c_num}² - {coloured_side_a_num}²) ÷ (2 x {coloured_side_b_num} x {coloured_side_c_num})
      cos({coloured_angle_BC}) = ({coloured_side_b_squared} + {coloured_side_c_squared} - {coloured_side_a_squared}) ÷ {2 * side_b * side_c}
          {coloured_angle_BC}  = cos⁻¹({(side_b_squared + side_c_squared - side_a_squared)} ÷ {2 * side_b * side_c})
          {coloured_angle_BC}  = cos⁻¹({(side_b_squared + side_c_squared - side_a_squared) / (2 * side_b * side_c)})
therefore {coloured_angle_BC}  = {round(angle_BC, 2)}°
""")
    
    return  # End the function here



def draw_triangle(list_of_sides, list_of_angles, colours_list, turtle_anim=False, turtle_speed=3, show_angles=True, mode="secondary"):
    """Draw a triangle using Turtle in Python, using given sides and angles.

    Default:
    - turtle_anim, which controls whether or not the animation of the turtle drawing the triangle is played, is set to False.
    - turtle_speed, which controls the speed of the animation of the turtle, is set to 3 by default. The higher the number, the faster the animation is.
    - show_angles, which determines whether the angles will be displayed on the triangle (False for Primary mode, True for Secondary mode)
    """
    
    # Calculate what is the number which the sides need to be multiplied by, to make the triangle scaled to fit the screen better.
    scale_multiplier = random.randint(400, 450) / max(list_of_sides)  # Pick a random number between 400 and 450 for the sides to be scaled to, this
                                                                      # will result in various slight changes in sizes for every triangle generated.
    
    # Read in the sides and angles, assign each item in the list to its respectively variable.
    # (e.g. first item in list_of_sides is assigned to variable side_a)
    side_a, side_b, side_c = list_of_sides
    angle_AB, angle_BC, angle_AC = list_of_angles
    scaled_side_a, scaled_side_b, scaled_side_c = [side * scale_multiplier for side in list_of_sides]  # Use list comprehension to apply the scaling into new scaled_ variables, in just one line.

    # Calculate the height of the triangle, to use to help make the drawing centred in the Turtle output window.
    tri_semiperimeter = (scaled_side_a + scaled_side_b + scaled_side_c) / 2  # Heron's formula to find semiperimeter of triangle, given three sides.
    tri_area = math.sqrt(tri_semiperimeter * (tri_semiperimeter - scaled_side_a) * (tri_semiperimeter - scaled_side_b) * (tri_semiperimeter - scaled_side_c))  # Use the semiperimeter to find the area of the triangle.
    tri_height = (2 * tri_area) / scaled_side_b  # Reverse the equation of Area = 1/2 * B * H to find the height.


    # Initliase the colours_used dictionary to save the colours used in each side of the triangle, for later use in the command-line output.
    colours_used = {
        "side_a" : None,
        "side_b" : None,
        "side_c" : None,
    }

    # Shuffle the colours list (to make the colours different every new triangle).
    colours_list = shuffle_list(colours_list)
    
    # Randomly select a colour from the colours_list, ensuring no duplicates.
    colour_used_index = 0  # Initialise the index at 0.
    for side_name in colours_used.keys():  # for each of the three sides of a triangle.

        # e.g. for Side A (first loop), take the first index (0) of the randomised index list.
        colours_used[side_name] = colours_list[colour_used_index]
        
        # Add one to colour_used_index
        colour_used_index += 1

    ## Print out the sides, and their lengths, in their respective colours.
    # Example of what it looks like when printed (without colour):
    # Side A = 1
    # Side B = 2
    # Side C = 3
    print(f"""
 [Sides] {colour(f"Side A = {triangle_side_a}", colours_used["side_a"])}
         {colour(f"Side B = {triangle_side_b}", colours_used["side_b"])}
         {colour(f"Side C = {triangle_side_c}", colours_used["side_c"])}""")
    
    # If the user selected to draw the triangle in primary mode, determine the triangle type first, then tell the user what is the triangle type, then reveal the reason, then draw.
    if mode.lower() == "primary":
        triangle_type_dict = determine_triangle_type(side_a, side_b, side_c)
        print(f"\n[System] Your triangle is {colour(triangle_type_dict['triangle_type'], 'bold_underline')} triangle, because {colour(str(triangle_type_dict['reason']).lower(), 'bold_underline')}")
        print(f"\n{line}")

    # If the user selected to draw the triangle in seconday mode, print out the angles of the triangles first, then ask if the user wants to view the formulas for the angles, then draw.
    elif mode.lower()== "secondary":
        ## Print out the angles in colour.
        # Example of what it looks like when printed (without colour):
        # angleA = 90°
        # angleB = 45°
        # angleC = 45°
        print(f"""
[Angles] angle{colour(f"A", colours_used["side_a"])}{colour(f"B", colours_used["side_b"])} = {round(angle_AB, 2)}°
(2 d.p.) angle{colour(f"A", colours_used["side_a"])}{colour(f"C", colours_used["side_c"])} = {round(angle_AC, 2)}°
         angle{colour(f"B", colours_used["side_b"])}{colour(f"C", colours_used["side_c"])} = {round(angle_BC, 2)}°

{line}         
""")
        # Ask the user if they want to view the formulas used to calculate the angle between the triangle.
        print("[System] Would you like me to show you how I determined the angles of your triangle?")
        user_show_angles_formulas = input("         'y' (yes) / 'n' (no) / 'q' (quit) | ")
        print("\n")

        # Check if the user quit, if they did, end the function and return "user_quit" so that it can be read by other functions
        if user_show_angles_formulas.lower() in ["quit", "q"]:
            return "user_quit"
        
        # Keep looping the questions until the user quits, or provides a valid answer.
        while user_show_angles_formulas.lower() not in ["quit", "q"]:
            
            # If the user wants to see the formulas, call the function to show the formulas used to calculate the angles, then wait for 1 second before breaking out of the loop and drawing the triangle
            if user_show_angles_formulas.lower() in ["yes", "y"]:
                print(line)  # Print a line as a separator
                show_angle_formulas(side_a, side_b, side_c, colours_used)  # Call the function to show the formulas used to calculate the angles
                print(line)  # Print another line as a separator
                time.sleep(1)  # Wait for 1 second 
                break  # Break out of the While loop

            # If the user does not want to see the formulas used to calculate the angles, print an output saying the input was received, then move on to draw the triangle.
            elif user_show_angles_formulas.lower() in ["no", "n"]:
                print("> Got it, I will draw the triangle now")
                break  # Break out of the While loop

            # If the input of the user was not valid, tell the user that it was not valid, then keep looping the question.
            else:
                print("\n[System] Your last input was not valid. Would you like me to show you how I determined the angles of your triangle?")
                user_show_angles_formulas = input("         'y' (yes) / 'n' (no) / 'q' (quit) | ")
                print("\n")
        


    # Print out some initial outputs for user to read while the drawing is shown.
    time.sleep(0.25)  # Wait for 1/4 of a second
    print("\n[System] A new graphical interface window has opened, please open it to view your drawn triangle.")  # Tell the user to open the Turtle window to view the triangle
    time.sleep(1.5)  # Wait for 1 1/2 seconds
    print("     [*] Please close the window of the drawing when you are done, in order to move on.")  # Let the user know that they should close the window of the Turtle animation in order to move on with the program


    # Initialise the variable which determines whether the program will try to draw the animation,
    # this prevents errors when user closes the animation window before it finishes.
    try_to_draw = True
    while try_to_draw == True:
        try:
            ## Setting up the window for Turtle
            window = turtle.Screen()  # Create window object (for turtle).
            window.title(f"Triangle with side lengths of: A = {side_a}, B = {side_b}, C = {side_c}")  # Set the title for the window.
            window.setup(750, 750)  # Set size to 750x750
            window.tracer(turtle_anim)  # Since the turtle_anim is a Boolean, it works to toggle the tracer (animation) on or off.
            turtle.TurtleScreen._RUNNING = True  # Let Turtle know that it is running (just in case, to prevent any bugs or crashes).

            ## Setting up the Turtle object for drawing
            t = turtle.Turtle()  # Create the Turtle object.
            t.speed(speed=turtle_speed)  # Set the speed of the turtle.
            t.pensize(2)  # Set the thickness of the pen.
            turtle.bgcolor("black")  # Set the background colour of the animation window to black.

            ## Put disclaimer of "Triangle is not drawn to scale"
            t.hideturtle()  # Hide the Turtle object.
            t.penup()  # Prevent the movement from being drawn.
            t.goto(-(750/2) + 35, -(750 / 2) + 35)  # Go to the coordinates of the disclaimer location.
            t.pencolor("azure")  # Set pen colour to a shade of white.
            t.write(f"*Triangle is not drawn to scale.", font=("Helvetica", 10, "normal"))  # Write out the disclaimer in Helvetica font, with size 10.

            ## Move to starting position
            # Determine the x coordinates of the starting position depending on the size of the triangle's base.
            if max(list_of_sides) == side_b or scaled_side_b >= 400:  # If the base is the biggest side of the triangle,
                                                                      # or if it is greater than or equal to 400...
                start_x = -200  # x coordinate = -200
            
            # Do the same for other sizes, decrease the size with each elif condition to
            # make sure that the program does not pass the check in the wrong one.
            elif scaled_side_b >= 350:  # If the scaled version of side B is >= 350, make the starting x coordinate, -185
                start_x = -185
            elif scaled_side_b >= 275:  # If the scaled version of side B is >= 275, make the starting x coordinate, -150
                start_x = -150
            elif scaled_side_b >= 225:  # If the scaled version of side B is >= 225, make the starting x coordinate, -100
                start_x = -100
            else:  # Make the default starting x coordinate -125
                start_x = -125

            # Determine the y coorindates of the starting position depending on the length of the triangle's height.
            if tri_height >= 250:  # If the height is greater than or equal to 250, make the starting y coordinate -80
                start_y = -80 
            else:  # Make the default staring y coordinate -50
                start_y = -50
        
            t.goto(start_x, start_y)  # Move the Turtle to the start position.
            t.pendown()  # Put the pen down to make the movements visible in the animation.
            t.showturtle()  # Unhide the turtle, so the user can see the movements and direction of the turtle.
            
            ## Draw Side B first
            t.pencolor(convert_colour_to_turtle(colours_used["side_b"]))  # Set the colour of side B.
            t.forward(scaled_side_b / 2)  # Go forward for half of side B's length.
            # Label the side (start)
            t.penup()  # Move the pen up.
            t.right(90)  # Turn right 90 degrees.
            t.forward(25)  # Move forward 25 steps.
            t.write(f"B = {side_b}", align="center")  # Label side B, indicating its length.
            t.backward(25)  # Move backward 25 steps.
            t.left(90)  # Turn left 90 degrees.
            t.pendown()  # Put the pen down.
            # Label the side (end)
            t.forward(scaled_side_b / 2)  # Finish drawing the side.
            
            if show_angles == True:  # If the angles need to be shown...
                t.penup()  # Move the pen up.
                t.forward(15)  # Move forward 15 steps.
                t.pencolor("azure")  # Set the pen colour to a shade of white.
                t.write(f"angleAB = {round(angle_AB, 2)}°", align="left")  # Label the angle of the triangle.
                t.backward(15)  # Move backward 15 steps.
                t.pendown()  # Put the pen down.


            ## Draw Side A
            # Refer to the drawing of Side B for comments on code.
            t.pencolor(convert_colour_to_turtle(colours_used["side_a"])) # Go forward for half of side A's length
            t.left(180 - angle_AB)  # Turn left, since the turtle is turning left, subtract the triangle's angle from 180 to use obtuse angle instead
            t.forward(scaled_side_a / 2) # Go forward for half of side A's length
            # Label the side (start)
            t.penup() # Go forward for half of side A's length
            t.right(90) # Go forward for half of side A's length
            t.forward(25) # Go forward for half of side A's length
            t.write(f"A = {side_a}", align="left") # Go forward for half of side A's length
            t.backward(25) # Go forward for half of side A's length
            t.left(90) # Go forward for half of side A's length
            t.pendown() # Go forward for half of side A's length
            # Label the side (end)
            t.forward(scaled_side_a / 2) # Go forward for half of side A's length

            if show_angles == True: # Go forward for half of side A's length
                t.penup() # Go forward for half of side A's length
                t.forward(15) # Go forward for half of side A's length
                t.pencolor("azure") # Go forward for half of side A's length
                t.write(f"angleAC = {round(angle_AC, 2)}°", align="center") # Go forward for half of side A's length
                t.backward(15) # Go forward for half of side A's length
                t.pendown() # Go forward for half of side A's length


            # Draw Side C
            t.pencolor(convert_colour_to_turtle(colours_used["side_c"])) # Go forward for half of side A's length
            t.left(180 - angle_AC)  # Turn left, since the turtle is turning left, subtract the triangle's angle from 180 to use obtuse angle instead
            t.forward(scaled_side_c / 2) # Go forward for half of side A's length
            # Label the side (start)
            t.penup() # Go forward for half of side A's length
            t.right(90) # Go forward for half of side A's length
            t.forward(25) # Go forward for half of side A's length
            t.write(f"C = {side_c}", align="center") # Go forward for half of side A's length
            t.backward(25) # Go forward for half of side A's length
            t.left(90) # Go forward for half of side A's length
            t.pendown() # Go forward for half of side A's length
            # Label the side (start)
            t.forward(scaled_side_c / 2) # Go forward for half of side A's length

            if show_angles == True: # Go forward for half of side A's length
                t.penup() # Go forward for half of side A's length
                t.forward(20) # Go forward for half of side A's length
                t.pencolor("azure") # Go forward for half of side A's length
                t.write(f"angleBC = {round(angle_BC, 2)}°", align="right") # Go forward for half of side A's length
                t.pendown() # Go forward for half of side A's length

            t.hideturtle()  # Hide the turtle cursor, but keep the window open
            window.tracer(True)  # Turn the animation on, to prevent glitches
            turtle.done()  # Finish the drawing to prevent glitches when window is closed
            return  # End the Function

        except:  # If any error is passed... (most likely because the user closed the animation window prematurely)
            
            # Get input on user if they want to restart the drawing
            restart_drawing = input("""\n[System] You have just closed the window of the drawing of your triangle BEFORE the drawing could finish. Would you like to restart the drawing?
         Yes to restart the drawing, No to quit and reinput another three sides for a new triangle. (Y/N): """)
            
            if restart_drawing.lower() in ["no", "n"]:  # If No...
                try_to_draw = False  # set the variable to False
                break  # break out of the While Loop
            
            while restart_drawing.lower() not in ["no", "n"]:  # Keep asking the usre to input a valid answer if their answer is invalid.
            
                if restart_drawing.lower() in ["yes", "y"]: # If the answer to the original question was Yes...
                    # Print out some initial outputs for user to read while the drawing is shown.
                    time.sleep(0.5)
                    print("[System] A new graphical interface window has opened, please open it to view your drawn triangle.")
                    time.sleep(1)
                    print("     [*] Please close the window of the drawing when you are done, in order to move on.")
                    try_to_draw = True  # set the variable to True
                    break  # Finish the current iteration of the while loop, continue on to the next loop.

                else:
                    restart_drawing = input("\n[System] Your last input was not valid. Would you like to restart the drawing? (Y/N) ")

    
    return  # End the Function


### Start the real program

# Initialise the set of colours that can be used
colours_list = ["green", "blue", "yellow", "pink", "red"]  # Colours that can be used for printing any sort of text
banner_colours_list = ["blue", "yellow", "pink"]  # Colours that can be used for the banners of the different modes (e.g. Homepage - "Tri Me", "Seconday Mode", "Primary Mode")

user_running_program = True  # Initialise the variable for the while loop to know that the user is running the program
reinputting_for_valid = False  # Initialise the variable for the program to know that the user is not reinputting side legnth
while user_running_program == True:

    # If the user is not reinputting side lengths, print out the home screen
    if reinputting_for_valid == False:
        random_banner_colour_list = shuffle_list(banner_colours_list)  # Shuffle the list of colours for banners
        colour_main_banner =  random_banner_colour_list[0]  # Pick the colour for the main banner "Tri Me"
        colour_p_banner = random_banner_colour_list[1]  # Pick the colour for the Primary Mode banner
        colour_s_banner = random_banner_colour_list[2]  # Pick the colour for the Secondary Mode banner

        clear_terminal()  # Clear the terminal

        # Print the main banner "Tri Me", along with informatuon on the program such as how it works, etc.
        print(big_line)
        print(colour(
'''
                                ████████╗██████╗ ██╗    ███╗   ███╗███████╗
                                ╚══██╔══╝██╔══██╗██║    ████╗ ████║██╔════╝
                                   ██║   ██████╔╝██║    ██╔████╔██║█████╗
                                   ██║   ██╔══██╗██║    ██║╚██╔╝██║██╔══╝
                                   ██║   ██║  ██║██║    ██║ ╚═╝ ██║███████╗
                                   ╚═╝   ╚═╝  ╚═╝╚═╝    ╚═╝     ╚═╝╚══════╝
    
                            A program to help you with your triangular problems
          Simply input the three sides of your triangle, and I will show you how to draw it out.''', colour_main_banner))

        print(f"""

There are two different modes: {colour('Primary', colour_p_banner)} and {colour('Secondary', colour_s_banner)}

- {colour('Primary Mode', colour_p_banner)} determines what type of triangle it is (Equilateral, Isosceles, or Scalene), and
  features an animation for the triangle to help young users with their drawing.

- {colour('Secondary Mode', colour_s_banner)} calculates and tells you what are the angles between each sides of the triangle,
  featuring the formulas used in the process for older and more knowledgeable users.
""")
        print(f"{big_line}\n")

    # If the user wants to quit, quit the program.
    input_triangle_sides = get_triangle_sides()
    if input_triangle_sides == "user_quit":
        user_running_program = False
        break  # Break out of the while loop
    
    # If the user continues on with the program.
    else:
        triangle_side_a = input_triangle_sides["A"]  # Set the triangle side length A variable accordingly (from input function)
        triangle_side_b = input_triangle_sides["B"]  # Set the triangle side length B variable accordingly (from input function)
        triangle_side_c = input_triangle_sides["C"]  # Set the triangle side length C variable accordingly (from input function)

        triangle_check = check_triangle_valid(triangle_side_a, triangle_side_b, triangle_side_c)  # Use the triangle lengths to check if the triangle is valid
        triangle_valid_reason = triangle_check["reason"]  # Store the reason why the triangle is valid / invalid

        if triangle_check["valid"] == False:  # If the triangle of the user is invalid (based on the sides)...
            print(triangle_valid_reason)  # Tell the user why the triangle was invalid.
            reinputting_for_valid = True
            continue  # End the current loop and move on to the next loop.
        
        elif triangle_check["valid"] == True:  # If the triangle of the user is valid (based on the sides)...
            print(triangle_valid_reason)  # Tell the user why the triangle was valid.
            
            # Get the user input on whether they want the drawing in Primary or Secondary Mode
            pri_or_sec = input(
f"""
{line}

[System] Great! The triangle is valid.
        
         Draw in {colour('Primary Mode', colour_p_banner)}       ('p')
         Draw in {colour('Secondary Mode', colour_s_banner)}     ('s')
         Quit                       ('q' / 'quit')
        
         What would you like to do? """)
            
            pri_or_sec = pri_or_sec.lower()  # Store the user's input as a lowercase variable to make it easier to check

            # If the user wants to quit, quit the program.
            if pri_or_sec == "q" or pri_or_sec == "quit":
                print(end_statement)  # Print the end statement before quitting.
                reinputting_for_valid = False
                break

            # Keep looping the question if the user's answer is not valid, until they want to quit the program
            while pri_or_sec != "q" and pri_or_sec != "q":
                
                # Check if the user's input is valid, by checking if it is in the list of acceptable inputs
                if pri_or_sec not in ["p", "s", "q", "quit"]:
                    
                    # Keep looping the question if the user's answer is not valid
                    pri_or_sec = input(
f"""\n{line}\n\n[System] Your last input was not valid. Please input an available option.
        
         Draw in {colour('Primary Mode', colour_p_banner)}       ('p')
         Draw in {colour('Secondary Mode', colour_s_banner)}     ('s')
         Quit                       ('q' / 'quit')
        
         What would you like to do? """)
                
                # If the user wants the program to run in primary mode, save the primary mode banner
                if pri_or_sec == "p":
                    turtle_anim = True
                    show_angles = False
                    mode_banner = colour("""
██████╗ ██████╗ ██╗███╗   ███╗ █████╗ ██████╗ ██╗   ██╗    ███╗   ███╗ █████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██║████╗ ████║██╔══██╗██╔══██╗╚██╗ ██╔╝    ████╗ ████║██╔══██╗██╔  ██╗██╔════╝
██████╔╝██████╔╝██║██╔████╔██║███████║██████╔╝ ╚████╔╝     ██╔████╔██║██║  ██║██║  ██║█████╗
██╔═══╝ ██╔══██╗██║██║╚██╔╝██║██╔══██║██╔══██╗  ╚██╔╝      ██║╚██╔╝██║██║  ██║██║  ██║██╔══╝
██║     ██║  ██║██║██║ ╚═╝ ██║██║  ██║██║  ██║   ██║       ██║ ╚═╝ ██║╚█████╔╝██████╔╝███████╗
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝ ╚════╝ ╚═════╝ ╚══════╝
""", colour_p_banner) 
                    
                # If the user wants the program to run in secondart mode, save the secondary mode banner
                if pri_or_sec == "s":
                    turtle_anim = False
                    show_angles = True
                    mode_banner = colour("""
 ██████╗███████╗ █████╗  █████╗ ███╗  ██╗██████╗  █████╗ ██████╗ ██╗   ██╗    ███╗   ███╗ █████╗ ██████╗ ███████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗████╗ ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝    ████╗ ████║██╔══██╗██╔══██╗██╔════╝
╚█████╗ █████╗  ██║  ╚═╝██║  ██║██╔██╗██║██║  ██║███████║██████╔╝ ╚████╔╝     ██╔████╔██║██║  ██║██║  ██║█████╗  
 ╚═══██╗██╔══╝  ██║  ██╗██║  ██║██║╚████║██║  ██║██╔══██║██╔══██╗  ╚██╔╝      ██║╚██╔╝██║██║  ██║██║  ██║██╔══╝  
██████╔╝███████╗╚█████╔╝╚█████╔╝██║ ╚███║██████╔╝██║  ██║██║  ██║   ██║       ██║ ╚═╝ ██║╚█████╔╝██████╔╝███████╗
╚═════╝ ╚══════╝ ╚════╝  ╚════╝ ╚═╝  ╚══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝ ╚════╝ ╚═════╝ ╚══════╝
""", colour_s_banner)
                
                # If the user wants to quit, quit the program
                if pri_or_sec == "q" or pri_or_sec == "quit":
                    print(end_statement)  # Print the end statement before quitting

                # If the user wanted either primary or secondary mode...
                if pri_or_sec in ["p", "s"]:
                    clear_terminal()  # Clear the terminal screen
                    print(mode_banner)  # Print out the banner of the mode, e.g. "Primary Mode"
                    print(f"{big_line}\n")  # Print a thick line underneath for separation

                    # Calculate the angles between the sides, and store them into respective variables.
                    angle_AB, angle_BC, angle_AC = calculate_triangle_angles(triangle_side_a, triangle_side_b, triangle_side_c)

                    # If the user is running the program in primary mode, draw the triangles without labelled angles, and tell the user what kind of triangle it is.
                    if pri_or_sec == "p":

                        # Parameters for the draw function: Side Lengths in a list, Angles in a list, the list of printable colours, the converted list of colours into turtle-readable colours, the speed of the turtle drawing, whether the user wants to label the angles, the mode which the user picked
                        draw = draw_triangle([triangle_side_a, triangle_side_b, triangle_side_c], [angle_AB, angle_BC, angle_AC], colours_list=colours_list, turtle_anim=turtle_anim, turtle_speed=3, show_angles=show_angles, mode="primary")
                        
                        # If the user wants to quit, end the loop
                        if draw == "user_quit":
                            user_running_program = False
                        else:  # If the user wants to continue...
                            time.sleep(0.75)  # Wait for 3/4 of a second
                            reinputting_for_valid = False
                        break # Break out of the current While loop
                    

                    elif pri_or_sec == "s":

                        # Parameters for the draw function: Side Lengths in a list, Angles in a list, the list of printable colours, the converted list of colours into turtle-readable colours, the speed of the turtle drawing (in case), whether the user wants to label the angles, the mode which the user picked
                        draw = draw_triangle([triangle_side_a, triangle_side_b, triangle_side_c], [angle_AB, angle_BC, angle_AC], colours_list=colours_list, turtle_anim=turtle_anim, turtle_speed=3, show_angles=show_angles, mode="secondary")
                        
                         # If the user wants to quit, end the loop
                        if draw == "user_quit":
                            user_running_program = False
                        else:  # If the user wants to continue...
                            time.sleep(0.75)  # Wait for 3/4 of a second
                            reinputting_for_valid = False
                        break  # Break out of the current While loop