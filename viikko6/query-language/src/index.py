from statistics import Statistics
from player_reader import PlayerReader
from matchers import All, And, Not, HasAtLeast, HasFewerThan, PlaysIn

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))


if __name__ == "__main__":
    main()
