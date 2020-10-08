# CS 20 Conditional Branching Example
# Create a circle that changes sizes when a key is pressed

# setting the initial value of the global variable radius
radius = 10


def setup ():
    size (300, 300)


def keyPressed ():
    # we need to say that radius is a global variable in order to
    # change the value
    global radius 
    # when the plus sign is pressed, the radius increases by 5 pixels
    if key == "+":
        radius = radius + 5
    # add code so the radius is decreased by 5 is the minus
    # sign is pressed
    
    # add code so if any other key is pressed, a message is printed
    # telling the user which keys are valid.


def draw ():
    # we need to say that radius is a global variable in order to
    # change the value. We need to do this EVERYTIME we use it.
    global radius
    # a circle with a radius that changes when a key is pressed
    ellipse (150, 150, radius , radius)
