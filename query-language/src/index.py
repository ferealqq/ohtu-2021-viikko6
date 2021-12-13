from statistics import Statistics
from QueryBuilder import QueryBuilder
from player_reader import PlayerReader
from matchers import And, HasAtLeast, HasFewerThan, PlaysIn, Not, Or

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


def osa3():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher1 = Or(
        HasAtLeast(30, "goals"),
        HasAtLeast(50, "assists")
    )

    for player in stats.matches(matcher1):
        print(player)
        
    print("----------------------\n")

    matcher = And(
        HasAtLeast(40, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("NYI"),
            PlaysIn("BOS")
        )
    )

    for player in stats.matches(matcher):
        print(player)


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    matcher = query.playsIn("NYR").hasAtLeast(5, "goals").hasFewerThan(10, "goals").build()

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
