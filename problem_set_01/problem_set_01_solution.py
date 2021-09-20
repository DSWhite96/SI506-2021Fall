# START PROBLEM SET 01
print('Problem Set 01')

# PROBLEM 01 (15 points)
print('\nProblem 01')

#michigan theater = 'Michigan Theater'
michigan_theater = 'Michigan Theater'
state_theater = 'State Theater'
#state_theater = State Theater

ann_arbor_theaters = [michigan_theater, state_theater]

michigan_theater_type = type(michigan_theater)
state_theater_type = type(state_theater)
ann_arbor_theaters_type = type(ann_arbor_theaters)

print(f'michigan_theater is a {michigan_theater_type}.')
print(f'state_theater is a {state_theater_type}.')
print(f'ann_arbor_theaters is a {ann_arbor_theaters_type}.')


# PROBLEM 02 (20 points)
print('\nProblem 02')

movies_str_1 = 'Coda, On Broadway, Raiders of the Lost Ark, Selma, Let Them Lead, Rope, Star Wars: Return of the Jedi, Follies'

michigan_theater_movies = movies_str_1.split(', ')

movie_str_2 = 'The Green Knight, Respect, Free Guy, Together, Shang-Chi and the Legend of the Ten Rings, The Alpinist, The Lost Leondardo'

state_theater_movies = movie_str_2.split(', ')

print(michigan_theater_movies)
print(state_theater_movies)

# PROBLEM 03 (10 points)
print('\nProblem 03')

num_movies_michigan = len(michigan_theater_movies)
num_movies_state = len(state_theater_movies)

print(f'The Michigan Theater is showing {num_movies_michigan} movies this week.')
print(f'The State Theater is showing {num_movies_state} movies this week.')

# PROBLEM 04 (25 points)
print('\nProblem 04')
theater_1_seats = 140
theater_2_seats = 100
theater_3_seats = 80
theater_4_seats = 50

total_seats_state = theater_1_seats + theater_2_seats + theater_3_seats + theater_4_seats
avg_seats_state = total_seats_state // 4

print(f'The average theater at the State Theater has {avg_seats_state} seats.')

# PROBLEM 05 (30 points)
print('\nProblem 05')

main_auditorium_seats = 1610
screening_room_seats = 200

total_seats_michigan = main_auditorium_seats + screening_room_seats
avg_seats_michigan = total_seats_michigan // 2

print(f'The average theater at the Michigan Theater has {avg_seats_michigan} seats.')
