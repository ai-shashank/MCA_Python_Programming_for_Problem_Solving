# Absolute imports
from shapee.circle import goll
from shapee.rectangle import Rectangle
from shapee.point import A

# Create objects
p = A(0, 0)
c = goll(p, 5)
r = Rectangle(10, 4)

print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())
print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())


