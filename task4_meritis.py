import itertools

# Task 1: Read and Parse Data
def read_data(file_name):
    with open(file_name, 'r', encoding='utf-8-sig') as file:  # Specify UTF-8 encoding with BOM skip
        lines = file.readlines()
        athletes = [(int(line.split(',')[0]), float(line.split(',')[1])) for line in lines]
    return athletes

data1 = read_data("d2_equipe_de_4.txt")

# Task 2: Calculate Relay Transmission Time
def relay_time(time1, time2):
    return (time2 - time1) ** 2

# Task 3: Generate Team Combinations
def generate_teams(data, team_size):
    combinations = list(itertools.combinations(data, team_size))
    print("Type of combinations:", type(combinations[0]))
    return combinations


teams1 = generate_teams(data1, 4)

# Task 4: Calculate Total Time for Each Team
def total_time(team, relay_times):
    print("Type of team:", type(team))
    print("Value of team:", team)
    total = sum(athlete[1] for athlete in team)
    for i in range(len(team) - 1):
        total += relay_times[team[i][0], team[i + 1][0]]
    return total

# Task 5: Find Best Combination of Teams
def find_best_combination(teams, relay_times):
    best_score = float('-inf')
    best_teams = None
    for combination in teams:
        total = sum(total_time(team, relay_times) for team in combination)
        score = -abs(total)  # Negative of difference between best and worst time
        if score > best_score:
            best_score = score
            best_teams = combination
    return best_teams


# Generate relay times dictionary for the first data set
def generate_relay_times(data):
    relay_times = {}
    for athlete1 in data:
        for athlete2 in data:
            relay_times[athlete1[0], athlete2[0]] = relay_time(athlete1[1], athlete2[1])
    return relay_times

relay_times1 = generate_relay_times(data1)

# Find the best combination of teams for the first data set
best_teams = find_best_combination(teams1, relay_times1)
print(best_teams)


