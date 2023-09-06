import numpy as np

#落書きです
'''
class score:
    totalscore = [0]
    point = [0]
    wallpoint = [0]
    zahyo = np.array([
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1]
    ])

    def score(self, structures, height, width, wall):
        self.point,self.totalscore, self.wallpoint = np.zeros((height,width),dtype=int)
        self.point = np.where(structures == 1 and structures == 0, 20, 100)
        for i in range(height):
            for j in range(width):
                if wall[i, j] == 1:
                    for k in range(8):
                        self.wallpoint[score.zahyo[k]]=

'''
