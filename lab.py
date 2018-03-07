from bot import Bot
from DNA import CleanerDNA
from test import CleanTestPaper
from ftree import FamilyTree

from joblib import Parallel, delayed
import multiprocessing

class Laboratory(object):
    def __init__(self):
        self.sample_id = 0
        self.fmt = FamilyTree()

    def __createbots(self, num):
        bots = [None for x in range(num)]
        for i in range(0, num):
            bots[i] = Bot(self.sample_id)
            self.sample_id += 1
        return bots

    def __injectrandomDNA(self, bots):
        for b in bots:
            dna = CleanerDNA()
            dna.createrandom()
            b.injectDNA(dna)

    def __generatebyseed(self, gens):
        total = gens[0]
        seed = gens[1]
        size = len(gens[2])

        total = int(total * 1.01)  # have 0.1 for DNA random change
        le = seed[0].extractDNA().getDNAlens()

        bots = self.__createbots(size)

        for nb in bots:
            dna = CleanerDNA()
            dna.createempty()
            for b in seed:
                n = int(le * (b.getscore() + 1) / total)
                for i in range(n):
                    p = dna.getrandomemptypos()
                    r = b.extractDNA().getrulebypos(p)
                    dna.setrulebypos(p, r[1])
            dna.fillemptybyrandom()

            nb.injectDNA(dna)

        return bots

    def experitment(self, bots):
        test = CleanTestPaper()
        #num_cores = multiprocessing.cpu_count()
        #Parallel(n_jobs=num_cores, backend="threading")(delayed(b.taketest)(test) for b in bots)
        for b in bots:
            b.taketest(test)

    def __checkresult(self, bots):
        seed = self.__selectgoodbot(bots)
        total = sum(s.getscore() + 1 for s in seed)
        return [total, seed, bots]

    def evalution(self, bots):
        ret = self.__checkresult(bots)
        tail = self.fmt.get()
        if ret[0] >= tail[0]:
            self.fmt.push(ret)
            print('%d accepted' % ret[0])
        else:
            self.fmt.inc()
            print('%d droped' % ret[0])

        ret = self.fmt.get()
        return ret

    def __selectgoodbot(self, bots):
        sbots = sorted(bots, reverse=True)
        return sbots[0:int(len(bots) * 0.1)]

    def revolution(self, gens):
        return self.__generatebyseed(gens)

    def mainprocess(self):
        bots = self.__createbots(200)
        self.__injectrandomDNA(bots)
        for i in range(400):
            self.experitment(bots)
            gens = self.evalution(bots)
            bots = self.revolution(gens)

        self.fmt.show()


l = Laboratory()
l.mainprocess()
