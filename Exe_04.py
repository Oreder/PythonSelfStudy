cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# Upgrade part
my_name = 'Binh D. Nguyen'
my_age = 22
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

#print "Let's talk about %s." % my_name
print(f"Let's talk about {my_name:}.")
#print "He's %d inches tall." % my_height
print("He's {:d} inches tall.".format(my_height))
#print "He's %d pounds heavy." % my_weight
#print "Actually that's not too heavy."
#print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print(f"He's got { my_eyes:} eyes and {my_hair:} hair.")
#print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
#print "If I add %d, %d, and %d I get %d." % (
#    my_age, my_height, my_weight, my_age + my_height + my_weight)
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {my_age + my_height + my_weight}.")
