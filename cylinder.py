# Pulled in and imported Math Library. Will be needed for Pi variable.
import math

# Establish variables as floats for the inputs.
radius = float(input('Enter the radius of the right cylinder: '))
height = float(input('Enter the height of the right cylinder: '))

# Locked Pi to a variable for ease of use.
pi = math.pi

# Created formula for Surface Area Calculator. With two parameters for the radius and height. I used slightly different identifiers as using the same as the main variables can sometimes
# make it confusing.
def surface_area_calculator(rad, ht):
    surface_area = (2 * pi * rad * ht) + (2 * pi * pow(rad, 2))  # Created based on formula provided by assigment. Used parentheses to ensure order of operations is respected.
    return surface_area  # Return the value from the above calculation.

# Created formula for Volume with the same parameters as the formula above (radius and height)
def volume_right_cylinder(rad, ht):
    volume_cylinder = (pi * pow(rad, 2) * ht)  # Utilizing parentheses to keep Order Of Operations respected. Probably not needed, but makes me feel better.
    return volume_cylinder  # Return value from calculation above.

calculated_surface_area = surface_area_calculator(radius, height)  # Run formula for Surface Area and bind to a new variable. Will make it easier to put together f string later.
calculated_volume_cylinder = volume_right_cylinder(radius, height)  # Same as above, but for Volume Cylinder.

print(f'The surface area of the right cylinder is {calculated_surface_area:.4f}')  # Run f string with static text and the variable established above with the calculated surface area. 
print(f'The volume of the right cylinder is {calculated_volume_cylinder:.4f}')  # Same as above but for the Cylinder Volume.

# Jose Salazar
# PA 3