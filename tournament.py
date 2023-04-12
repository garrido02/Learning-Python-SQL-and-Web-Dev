# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # Read teams into memory from file
    with open(sys.argv[1]) as file:
        # read file as dictionary
        reader = csv.DictReader(file)
        for team in reader:
            # turn every column of rating (value) to int
            team["rating"] = int(team["rating"])
            teams.append(team)

    counts = {}
    # Loop through the number of simulations
    i = 0
    for i in range(N):
        # store winner in variable
        winner = simulate_tournament(teams)
        # if the winner which is a name is in counts dictionary add 1 victory
        if winner in counts:
            counts[winner] += 1
        # if not add 1
        else:
            counts[winner] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])
    # return a new list with only the winning teams
    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # we want to loop the simulation until we only get one team left
    while len(teams) > 1:
        teams = simulate_round(teams)
    # 0 will be the only team remaining on the list of teams and the name is acessivel like a struct
    return teams[0]["team"]


if __name__ == "__main__":
    main()