# Section 1 - Your code
from utils import *
set_background("underwater")

s1 = create_sprite("cardinal", 150, 200)
s2 = create_sprite("cardinal", -200, 150)
s2 = create_sprite("cardinal", -200, -150)
s2 = create_sprite("mario", 200, -150)

message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("naoli",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()
