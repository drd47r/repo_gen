import random


class minimap(object):
    def __init__(self):
        self.mapw = 0
        self.maph = 0
        self.map = None

        self.posx = 0
        self.posy = 0

    def clean(self):
        if self.map[self.posx][self.posy] == 1:
            self.map[self.posx][self.posy] = 0
            return 1
        return 0

    def __move(self, x, y):
        if self.__isvalid(x, y):
            self.posx = x
            self.posy = y

    def move(self, direction):
        """
        fun = {
            1: lambda x, y: [x-1, y],
            2: lambda x, y: [x+1, y],
            3: lambda x, y: [x, y-1],
            4: lambda x, y: [x, y+1]
        }
        pos = fun.get(direction)(self.posx, self.posy)
        self.__move(pos[0], pos[1])
        """
        return {1: lambda x, y: self.__move(x-1, y),
                2: lambda x, y: self.__move(x+1, y),
                3: lambda x, y: self.__move(x, y-1),
                4: lambda x, y: self.__move(x, y+1)
                }.get(direction)(self.posx, self.posy)


    def getpos(self):
        return [self.posx, self.posy]

    def createmap(self, w, h):
        self.map = [[0 for y in range(h)] for x in range(w)]
        self.mapw = w
        self.maph = h
        dirs = int(w * h * .41)
        while dirs > 0:
            x = random.randint(0, w - 1)
            y = random.randint(0, h - 1)
            if self.map[x][y] != 1:
                self.map[x][y] = 1
                dirs -= 1

        self.posx = random.randint(0, w - 1)
        self.posy = random.randint(0, h - 1)

    def __isvalid(self, x, y):
        if (x < 0 or x >= self.mapw) \
                or (y < 0 or y >= self.maph):
            return False
        return True

    def __getobj(self, x, y):
        """
        :param x:
        :param y:
        :return obj:

        obj:
        0 is empty
        1 is dirty
        2 is wall
        """
        if self.__isvalid(x, y):
            obj = self.map[x][y]
        else:
            obj = 2
        return obj

    def getenv(self):
        """
        slot,
        env[0] position now
        env[1] position left
        env[2] position right
        env[3] position up
        env[4] position down
        """

        if None == self.map:
            print("map of testing is not ready!")
            return

        env = [0 for i in range(5)]
        env[0] = self.__getobj(self.posx, self.posy)
        env[1] = self.__getobj(self.posx - 1, self.posy)
        env[2] = self.__getobj(self.posx + 1, self.posy)
        env[3] = self.__getobj(self.posx, self.posy - 1)
        env[4] = self.__getobj(self.posx, self.posy + 1)

        return env
