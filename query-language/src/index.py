from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, HasFewerThan, PlaysIn, Not

def osa2():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)


    print("\nHasAtLeast(1, 'goals')\n")
    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )
    print("----------------------\n")
    for player in stats.matches(matcher):
        print(player)

    print("\nHasFewerThan(1, 'goals')\n")

    matcher = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )
    print("----------------------\n")
    for player in stats.matches(matcher):
        print(player)


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)


if __name__ == "__main__":
    main()
