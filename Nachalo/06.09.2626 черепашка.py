import turtle

##for i in range (4):
##  turtle. forward (100)
##  turtle. left (90)

##turtle. forward (100)
##turtle. left (90)
##turtle. forward (100)
##turtle. left (90)
##turtle. forward (100)
##turtle. left (90)


Ugol= input ('Bведите количество углов ')
Ugol= int(Ugol)
Col= input ('Bведите цвет на английском ')
turtle. color(Col)
turtle.begin_fill()
for i in range (Ugol):
  turtle. forward (80)
  turtle. left (360/Ugol)
turtle.end_fill()
