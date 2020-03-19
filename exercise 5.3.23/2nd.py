import turtle
tess=turtle.Turtle()
alex=tess
alex.color("hotpink")

print(alex == tess)
print(alex is tess)

#it duplicates the turtle, alex and tess is same in this instance, so the fragment creates just one turtle.
#changing the color of alex also changes the color of tess.