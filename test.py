from map import minimap
#import copy


class TestPaper(object):
    def __init__(self):
        pass

    def test(self, strategy):
        return NotImplementedError


class CleanTestPaper(TestPaper):
    def __init__(self):
        super(CleanTestPaper, self).__init__()
        self.map = minimap()

    def __getact(self, env, strategy):
        act = strategy.getaction(env)
        return act

    def __action(self, act):
        if act == 0:
            return self.map.clean()
        else:
            self.map.move(act)
            return 0

    def __emulate(self, strategy):
        env = self.map.getenv()
        act = self.__getact(env, strategy)

        return self.__action(act[1])

    def test(self, strategy):
        self.map.createmap(10, 20)
        score = 0
        for s in range(200):
            score += self.__emulate(strategy)
        return score
