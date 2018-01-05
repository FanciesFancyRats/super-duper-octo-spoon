#assigns int 100 to variable named cars
cars = 100
#assigns float 4.0 to variable named space_in_a_car
space_in_a_car = 4.0
#assigns int 30 to variable named drivers
drivers = 30
#assigns int 90 to variable named passengers
passengers = 90
#assigns the diffrence in the variable cars(100) and the variable drivers(30) to the variable cars_not_driven(70)
cars_not_driven = cars - drivers
#assigns the value of drives to the variable named cars_driven
cars_driven = drivers
#assigns the product of cars_driven(30) and space_in_a_car(4.0) to the variable carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
#assigns 
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carool today."
print "We need to put about", average_passengers_per_car, "in each car."
