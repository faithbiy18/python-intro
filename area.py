#python functon to return the area of a circle
from math import pi
from math import pow

radius=int(input("enter radius :"))
length = int(input("Enter the length of the cylinder :"))

def area_of_circle(radius):
    area = pi * pow(radius, 2)
    return area

print("area of the circle is :",area_of_circle(radius))

   

#python functon to return the volume of a cylinder

def volume_of_cylinder(radius, length):
    cross_sectional_area = pi * pow(radius,2)
    volume_of_cylinder = cross_sectional_area * length
    return volume_of_cylinder


print("volume_of_cylinder is :",volume_of_cylinder(radius, length))



#python functon to return the volume of a sphere
def volume_of_sphere(radius):
    volume_of_sphere = 4/3 * pi * pow(radius,3)
    return volume_of_sphere

print("volume_of_sphere is :",volume_of_sphere(radius))