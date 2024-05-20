from turtle import Turtle, Screen
from prettytable import PrettyTable

timmy = Turtle()
print(timmy)

timmy.shape('turtle')
timmy.color('gold')
timmy.forward(200)
timmy.left(90)
timmy.forward(200)
timmy.left(90)
timmy.forward(200)
timmy.left(90)
timmy.forward(200)

my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()


table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column('Type', ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)
