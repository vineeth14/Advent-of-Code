from dataclasses import dataclass


@dataclass
class question:
    xA: int
    yA: int
    xB: int
    yB: int
    xPrize: int
    yPrize: int


def get_input():
    with open(
        "/Users/vineethrajesh/Projects/Advent-of-Code/2024/day13/INPUT.txt"
    ) as file:
        f = file.read().strip()

        sections = f.split("\n\n")
    queries = []
    for section in sections:
        lines = section.split("\n")
        stringA = lines[0]
        stringB = lines[1]
        stringC = lines[2]
        xA = stringA.find("X+")
        commaA = stringA.find(",")
        yA = stringA.find("Y+")
        xB = stringB.find("X+")
        commaB = stringB.find(",")
        yB = stringB.find("Y+")
        pX = stringC.find("X=")
        commaC = stringC.find(",")
        pY = stringC.find("Y=")

        queries.append(
            question(
                xA=int(stringA[xA + 2: commaA]),
                yA=int(stringA[yA + 2: len(stringA)]),
                xB=int(stringB[xB + 2: commaB]),
                yB=int(stringB[yB + 2: len(stringB)]),
                xPrize=10000000000000 + int(stringC[pX + 2: commaC]),
                yPrize=10000000000000 + int(stringC[pY + 2: len(stringC)]),
            )
        )

    return queries


get_input()
