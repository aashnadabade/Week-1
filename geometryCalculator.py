import math
# to access math functions and constants like math.pi

# --- Functions ---
def areaRectangle(length, width):
  #area = length * width 
  #return area
  return length * width

def areaTriangle(base, height): 
  #area = 0.5 * base * height
  #return area
  return 0.5 * base * height
  
def areaCircle(radius):
  #area = math.pi * (radius * radius)
  #return area
  return math.pi * (radius * radius)

# --- Main Program ---

print("Welcome to the Shape Area Calculator!")
print("Enter 'R' for Rectangle, 'T' for Triangle, or 'C' for Circle.")

shape = input("Your choice: ").strip().lower()

if shape == "r":
  length = float(input("Enter the length: "))
  width = float(input("Enter the width: "))
  area = areaRectangle(length, width)
  print(f"The area of the rectangle is: {area:.2f}")
  #1 print("The area of shape is: " + str(area))

elif shape == "t":
  base = float(input("Enter the base: "))
  height = float(input("Enter the height: "))
  area = areaTriangle(base, height)
  print(f"The area of the triangle is: {area:.2f}")

elif shape == "c":
  radius = float(input("Enter the radius: "))
  area = areaCircle(radius)
  print(f"The area of the circle is: {area:.2f}")

else:
    print("Invalid shape choice. Please run the program again and choose R, T, or C.")
