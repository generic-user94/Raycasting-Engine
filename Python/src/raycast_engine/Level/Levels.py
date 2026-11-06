


class Level():
    def __init__(self):
        pass

    def getLevel(self, level):
        levels = [
            [
                [0, 0, 1500, 15],
                [0, 0, 15, 750],
                [0, 735, 1510, 760],
                [1485, 0, 1510, 760],
                [300, 200, 1200, 500]
            ]
        ]

        return levels[level]