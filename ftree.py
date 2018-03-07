import matplotlib.pyplot as plt

class FamilyTree(object):
    def __init__(self):
        """
        ft[0] total score of good seeds
        ft[1] good seeds
        ft[2] whole bots
        ft[3] sample times
        """
        self.ft = []
        self.ge = 0

    def inc(self):
        self.ge += 1

    def push(self, gen):
        gen.append(self.ge)
        self.ft.append(gen)
        self.inc()

    def pop(self):
        self.ft.remove(-1)

    def get(self):
        if len(self.ft) == 0:
            return [0, None, None]
        return self.ft[-1]

    def show(self):
        cys = len(self.ft)
        gle = len(self.ft[1])
        maxs = self.ft[-1][0]
        s = "max %d, average %f cycle %d" % (maxs, maxs / gle, cys)
        print(s)

        w = [x[0] for x in self.ft]
        v = [x[3] for x in self.ft]

        fig, ax = plt.subplots()
        ax.plot(v, w, '-o', ms=20, lw=2, alpha=0.7, mfc='orange')
        ax.grid()

        fig.text(0.95, 0.05, s,
                 fontsize=30,
                 color='gray',
                 ha='right',
                 va='bottom',
                 alpha=0.5)

        plt.show()

        input("press any keys to continue...")
