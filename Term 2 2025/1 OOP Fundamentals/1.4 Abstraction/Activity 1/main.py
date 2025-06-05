from shapey import Circle, Rectangle, Square

circle = Circle(3)
rectangle = Rectangle(1, 2, 3)
square = Square(2)


print(f'circle perimeter: {circle.perimeter()}\ncircle area: {circle.area()}\nsphere volume: {circle.volume()}\n')

print(f'rectangle perimeter: {rectangle.perimeter()}\nrectangle area: {rectangle.area()}\nprism volume: {rectangle.volume()}\n')

print(f'square perimeter: {square.perimeter()}\nsquare area: {square.area()}\ncube volume: {square.volume()}\n')