# START PROBLEM SET 02
print('Problem Set 02')

# PROBLEM 1
print('\nProblem 1')

gme_prices = [15.84, 35.50, 65.01, 325.00, 63.77]

price_max = max(gme_prices)
print(price_max)

price_max_index = gme_prices.index(price_max)
print(price_max_index)

gme_prices.append(52.40)
print(gme_prices)

gme_prices[0] = 17.69
print(gme_prices)

# PROBLEM 2
print('\nProblem 2')

# amc_prices = [33.47, 34.41, 40.84, 44.02, 50.16]

amc_prices = []
amc_prices.append(33.47)
amc_prices.append(34.41)
amc_prices.append(40.84)
amc_prices.append(44.02)
amc_prices.append(50.16)

print(amc_prices)

amc_prices_latest = amc_prices[-1]
print(amc_prices_latest)

amc_prices_last_three = amc_prices[2:]
print(amc_prices_last_three)

# PROBLEM 3
print('\nProblem 3')

pltr_prices = ' 21.82-24.90-24.01-25.71-26.64-26.28 '
pltr_prices_list = pltr_prices.strip().split('-')
print(pltr_prices_list)


# PROBLEM 4
print('\nProblem 4')

dates = ['September 10th', 'September 3rd', 'August 27th', 'August 20th', 'August 13th', 'August 6th']
dates.reverse()
dates_str = '|'.join(dates)
print(dates_str)


# PROBLEM 5
print('\nProblem 5')

pltr_highest = f"In the week ending on {dates[-2]}, Palantir closed with a price of ${pltr_prices_list[-2]} and AMC closed with a price of ${amc_prices[-2]}."
print(pltr_highest)

amc_highest = f"In the week ending on {dates[-1]}, Palantir closed with a price of ${pltr_prices_list[-1]} and AMC closed with a price of ${amc_prices[-1]}."
print(amc_highest)

# PROBLEM 6
print('\nProblem 6')

dates_reversed = dates[::-1]
print(dates_reversed)

# PROBLEM 7
print('\nProblem 7')

every_other_date = dates_reversed[::2]
print(every_other_date)