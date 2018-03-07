import random


class DNA(object):
    def __init__(self):
        self.l = []
        self.empty = []

    def createrandom(self):
        return NotImplementedError


class CleanerDNA(DNA):
    def __init__(self):
        super(CleanerDNA, self).__init__()
        self.t = [1,
                  3,
                  3 * 3,
                  3 * 3 * 3,
                  3 * 3 * 3 * 3,
                  3 * 3 * 3 * 3 * 3]

    def __getindexstr(self, n):
        """
        index[0] current position
        index[1] left cube
        index[2] right cube
        index[3] up cube
        index[4] down cube

        value of index[x]
        0 means empty
        1 means have dirs
        2 means is wall

        :param n:
        :return:
        """
        if n >= self.t[5]:
            print("n should less 242")
            return None

        d = []
        for i in range(5):
            d.append(n % 3)
            n = int(n / 3)
        d.reverse()
        index = ''.join(str(x) for x in d)

        return index

    def getDNAlens(self):
        return self.t[5]

    def getemptylen(self):
        return len(self.empty)

    def getrandomemptypos(self):
        if len(self.empty) <= 0:
            return -1
        return random.choice(self.empty)

    def getrulebypos(self, pos):
        return self.l[pos]

    def setrulebypos(self, pos, act):
        if self.l[pos][1] == -1:
            self.empty.remove(pos)
        self.l[pos][1] = act

    def fillemptybyrandom(self):
        for i in self.empty:
            index = self.l[i][0]
            act = self.__getrandomaction(index)
            self.l[i][1] = act
        self.empty = []

    def createempty(self):
        """
        act 0 clean current position
        act 1 move left
        act 2 move right
        act 3 move up
        act 4 mvoe down
        :return:
        """
        for i in range(0, self.t[5]):
            index = self.__getindexstr(i)
            act = -1
            self.l.append([index, act])
            self.empty.append(i)

    def createrandom(self):
        """
        act 0 clean current position
        act 1 move left
        act 2 move right
        act 3 move up
        act 4 mvoe down
        :return:
        """
        for i in range(0, self.t[5]):
            index = self.__getindexstr(i)
            act = self.__getrandomaction(index)
            self.l.append([index, act])

    def getaction(self, env):

        for e in env:
            if e > 2 or e < 0:
                print("number should within 0-2")
                return None

        ins = 0
        for i in range(0, 5):
            ins += env[i] * self.t[4-i]

        return self.l[ins]

    def __getrandomaction(self, index):
        act = random.randint(0, 4)
        if index[0] == '0' and act == 0:
            # avoid do clean empty cube things
            act = random.randint(1, 4)
        return act
