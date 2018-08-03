import random
from sklearn.cluster import KMeans
import numpy

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        hash = 3
        hash = 69 * hash + self.x
        hash = 69 * hash + self.y
        return hash

    def __eq__(self, o: object) -> bool:
        return (self.x == o.x and self.y == o.y)

    def __arr__(self):
        return [[self.x, self.y]]

if __name__ == '__main__':
    result = [[0, 0]]
    list_point = set()
    count = 0
    result = numpy.delete(result, 0, 0)
    while count < 1000:
        p = point(random.randint(0, 1000), random.randint(0, 1000))
        if p not in list_point:
            result = numpy.concatenate((result,p.__arr__()), axis=0)
            list_point.add(p)
            count += 1

    kmeans = KMeans(n_clusters=5).fit(result)
    print(kmeans.predict([result[0]]))
    with open("output.txt","w") as file:
        for i in result:
            file.write("(%d %d) in cluster %d\n" % (i[0], i[1], kmeans.predict([i])))
        file.close()