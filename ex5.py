my_name = "Ted"
my_age = 32
my_height = 74  # inches
my_weight = 180  #lbs
my_eyes = 'vrown'
my_teeth = "white"
my_hair = "long"

#OPTION1
print(f"Let's talk about {my_name}")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy")
print("Not too heavy")
print(f"He's fot {my_eyes} eyes and {my_hair} hair")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

#OPTION 2
print('This {food} is {adjective}.'.format(food='spam',
                                           adjective='absolutely horrible'))
print("Let's talk about {name}.".format(name='Python'))
print("He's {height} inches tall.".format(height=my_height))

print("He's {weight} pounds heavy.".format(weight=my_weight))
print("Actually that's not too heavy.")
print("He's got {eye_color} eyes and {hair_color} hair.".format(eye_color= my_eyes, hair_color= my_hair))
print("His teeth are usually {stain_level} depending on the coffee.".format(stain_level=my_teeth))

print("If I add {}, {}, and {} I get {}.".format(my_age, my_height, my_weight, my_age + my_height + my_weight))
