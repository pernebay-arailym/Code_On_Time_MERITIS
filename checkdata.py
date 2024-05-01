import itertools

# Function to calculate relay transmission time between two athletes
def relay_transmission_time(time1, time2):
    return (time1 - time2) ** 2

# Function to calculate total team time
def total_team_time(team, athlete_data):
    total_time = 0
    for i in range(len(team) - 1):
        athlete1 = team[i]
        athlete2 = team[i + 1]
        total_time += athlete_data[athlete1]  # Add individual athlete time
        total_time += relay_transmission_time(athlete_data[athlete1], athlete_data[athlete2])  # Add relay transmission time
    total_time += athlete_data[team[-1]]  # Add last athlete's time
    return total_time

# Read athlete data from file
def read_athlete_data(filename):
    athlete_data = {}
    with open(filename, 'r') as file:
        for line in file:
            bib_id, time = map(float, line.strip().split(','))  # Update split delimiter
            athlete_data[int(bib_id)] = time
    return athlete_data


# Function to find optimal teams
def find_optimal_teams(athlete_data):
    athletes = list(athlete_data.keys())
    best_score = float('-inf')
    best_teams = []

    # Generate all possible team combinations
    for team_combination in itertools.combinations(athletes, 4):
        remaining_athletes = [athlete for athlete in athletes if athlete not in team_combination]
        team1_time = total_team_time(team_combination, athlete_data)
        team2_time = total_team_time(remaining_athletes, athlete_data)
        score = team1_time - team2_time
        if score > best_score:
            best_score = score
            best_teams = [team_combination, remaining_athletes]

    return best_teams

# Main function
def main():
    filenames = ["d1_equipe_de_4.txt", "d2_equipe_de_4.txt", "d3_equipe_de_4.txt", "d4_equipe_de_4.txt", "d5_equipe_de_128_1.txt"]

    for filename in filenames:
        athlete_data = read_athlete_data(filename)
        teams = find_optimal_teams(athlete_data)
        team1, team2 = teams
        print("Teams for", filename)
        print("Team 1:", " ".join(map(str, team1)))
        print("Team 2:", " ".join(map(str, team2)))
        print()

if __name__ == "__main__":
    main()
