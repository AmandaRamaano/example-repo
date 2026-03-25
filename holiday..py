print ("List of available cities")

print("Johannesburg")
print("Bloemfontein")
print("Durban")


city_flight = input("Please enter the city you would like to fly to: ").capitalize()
num_night = int(input("Number of nights: "))
rental_days = int(input("Number of days for car rental: "))

#Define the costs of the different components for the trip

def hotel_cost(num_night):
    hotel_cost = 1500
    return(hotel_cost * num_night)

def plane_cost(city_flight):
    if city_flight == "Johannesburg":
        plane_cost = 2000 
        return(plane_cost)
    elif city_flight == "Bloemfontein":
        plane_cost = 3000
        return(plane_cost)
    elif city_flight == "Durban":
        plane_cost = 1500
        return(plane_cost)
    else:
        return 0
def rental_cost(rental_days):
    rental_cost = 800
    return(rental_cost * rental_days)

#Define holiday total cost

def holiday_cost(city_flight, num_night, rental_days):
    hotel_total = hotel_cost(num_night)
    plane_total = plane_cost(city_flight)
    rental_total = rental_cost(rental_days)
    return hotel_total + plane_total + rental_total

# Cost 

hotel = hotel_cost(num_night)
plane = plane_cost(city_flight)
rental = rental_cost(rental_days)
total_cost = holiday_cost(city_flight, num_night, rental_days)


print("Trip Itenerary")

print(f" Your are flying to {city_flight}")
print(f"Your number of nights is {num_night}")
print(f"Your car rental days are {rental_days}")
print(" ")
print("Summary cost" "\n")


print(f"The cost of your hotel is R{hotel}")
print(f"The cost of your flight is R{plane}")
print(f"The cost of your car rental is R{rental}")

print("\n")

print(f"The total cost of your trip is R{total_cost}")

# Reference - I completed this assignement with the help of a friend.