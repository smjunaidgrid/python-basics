#Understanding simple I/O functions
name = input("Enter your Name:")
gender = input("Gender:").lower()

if gender == "m" or gender == "male":
    title = "Mr."
else:
    title = "Mrs."
print(f"Welcome Onboard {title}{name}")

color = input("What color is the sky:")
print ("The sky is",color)

 