# START LAB EXERCISE 01
print('Lab Exercise 01 \n')

# PROBLEM 1 (3 points)
sonic = "Sonic Lunch Event"
# coffee hour = "Coffee Hour with MLC"
central_tour = "Central Campus Tour"
# tour-aa = "Tour of AA"
north_tour = "North Campus Tour"
# @ArbHiking = "Hiking in the Arb"
kerry_town = "Kerrytown District Tour "


# PROBLEM 2 (2 points)
events = [sonic, central_tour, north_tour, kerry_town]

print(f"\nThe valid variables are: {events}")


# PROBLEM 3 (3 points)
num_events = len(events)

print(f"\nThe length of the valid variable list is {num_events}")

# PROBLEM 4 (3 points)
data_type = type(num_events)

print(f"\nThe data type of the num_of_events is {data_type}")

# PROBLEM 5 (3 points points)
sonic_attended = 31
central_tour_attended = 35
north_tour_attended = 48
kerry_town_attended = 20

total_students = sonic_attended + central_tour_attended + north_tour_attended + kerry_town_attended

print(f"\nThe total number of students joined the events is {total_students}")

# PROBLEM 6 (3 points)
avg_event_size = total_students//num_events
# avg_event_size = total_students//num_events # also accepted

print(f"\nThe average number of students per event is {avg_event_size}")

# PROBLEM 7 (3 points)
free_gifts = "water_bottles ice_cream pens"
gifts = free_gifts.split()

print(f"\nThe variable free_gifts has been split into a list: {gifts}")


# END LAB EXERCISE