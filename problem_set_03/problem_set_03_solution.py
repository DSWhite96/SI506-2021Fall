# SI 506 Problem Set 03

# PART 1
print('\nPART 1')

day_1 = [
    'Kennedy & Company Education Strategies, LLC',
    'Congressional Research Service',
    'M&T Bank',
    'MassMutual Michigan Metro',
    'Alliance for Catholic Eduation (ACE Teaching Fellows)',
    'enFocus',
    'Buckle',
    'Defense Finance and Accounting Services (DFAS)',
    'AllianceBernstein',
    "Domino's",
    'Epic',
    'Fisher Investments',
    'goPuff dba GoBrands Inc.',
    'Govern For America',
    'Guidehouse',
    'Maxim Integrated Now Part of Analog Devices',
    'Equitable Advisors',
    'Exelon Corporation'
    ]


# PROBLEM 1
print('\nPROBLEM 1')

# 1.1
day_1.sort()
print(f'\nSorted Day 1 List: {day_1}.')

# 1.2
a_companies = day_1[:2]
print(f"\nThe companies that start with 'A' are {a_companies}.")

# 1.3
num_a_companies = len(a_companies)
print(f"\nThere are {num_a_companies} companies that start with the letter 'A'.")


# PROBLEM 2
print('\nPROBLEM 2')

# 2.1
e_companies = []

for company in day_1:
    if company.lower().startswith('e'):
        e_companies.append(company)
print(f"\nThe companies that start with 'e' or 'E' are {e_companies}.")

# 2.2
num_e_lower = 0

for e_company in e_companies:
    if e_company[0][0].islower():
        num_e_lower += 1
print(f"\nThere is {num_e_lower} company that starts with lower case 'E'.")


# PART 2

salaries = """Domino's|Graphic Designer|39000
Fisher Investments|Analyst|95916
Department of Health & Human Services|Technical Writing Specialist|76703
Splunk|Front-End Engineer|139554
Domino's|Senior Technical Writer|98000
Department of Health & Human Services|Analyst|71754
Domino's|Digital Specialist|93000
Splunk|Product Manager|134633
Dimensional Insight|Consultant|69359
Splunk|Customer Success Manager|125720
Edgeworth Economics|Consultant|80190
Edgeworth Economics|Economic Consultant|80645
Edgeworth Economics|Computer Systems Engineer|98495
Domino's|Analyst|77937
Fisher Investments|Research Associate|79141
Splunk|Data Analyst|117652
"""


# PROBLEM 3
print('\nPROBLEM 3')

# 3.1
sal_strings = salaries.splitlines()
print(f'\nsal_strings: {sal_strings}')

# 3.2
sal_lists = []

for s in sal_strings:
    s_split = s.split('|')
    sal_lists.append(s_split)
print(f'\nsal_lists: {sal_lists}')


# PROBLEM 4
print('\nPROBLEM 4')

sal_num = len(sal_lists)
n = 0
dom_sals = []
dom_idx = []

while n < sal_num:
    s = sal_lists[n]
    if "domino's" in s[0].lower():
        dom_sals.append(s)
        dom_idx.append(n)
    n += 1

print(f'\nThere are {sal_num} salaries.')
print(f'\nThe counter went to {n}.')
print(f"\nThe salary lists for Domino's are {dom_sals}.")
print(f"\nThe indices of the Domino's salaries in sal_lists are {dom_idx}.")


# PROBLEM 5
print('\nPROBLEM 5')

consultant_sals = []
analyst_sals = []

for row in sal_lists:
    if 'consultant' in row[1].lower():
        consultant_sals.append(row)
    elif row[1].lower() == 'analyst':
        analyst_sals.append(row)

print(f'\nThe consultant salaries are {consultant_sals}.')
print(f'\nThe analyst salaries are {analyst_sals}.')


# PROBLEM 6
print('\nPROBLEM 6')

max_analyst_sal = 0
max_analyst_company = ''

for sal in analyst_sals:
    current_sal = int(sal[2])
    if max_analyst_sal < current_sal:
        max_analyst_sal = current_sal
        max_analyst_company = sal[0]

print(f'\nThe highest analyst salary is {max_analyst_sal}.')
print(f'\nThe company with the highest analyst salary is {max_analyst_company}.')


# PROBLEM 7
print('\nPROBLEM 7')

sal_great = []
sal_too_low = []

for i in range(10):
    row = sal_lists[i]
    sal = int(row[-1])
    if sal > 50000:
        sal_great.append(row)
    else:
        sal_too_low.append(row)

print(f'\nGreat salaries: {sal_great}.')
print(f'\nToo low salaries: {sal_too_low}.')