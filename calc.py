pi = 3.141592653589793238462643383279502884197169399375105820

size = int(input("Enter the size of the circle: "))

rnd = (input("Do you want it to be rounded? Y/N: "))

if rnd == "N":
  print("The area of the circle is: " + str(pi * (size * size)))
else:
  rounded_area = round(pi * (size * size))
  print("The rounded area of the circle is: " + str(rounded_area))
