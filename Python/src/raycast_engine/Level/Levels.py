class Level:
    def __init__(self):
        pass

    def getLevel(self, level):
        # not hit
        levels = [
            [
                [0, 0, 1550, 10],
                [0, 0, 10, 800],
                [790, 0, 800, 1550],
                [0, 1540, 800, 1550],
            ]
        ]

        return levels[level]
