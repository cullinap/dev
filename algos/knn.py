import numpy as np
from collections import Counter


def kNearestNeighbors(data, predict, k=3):
    
    distances = []
    for i in data.keys():
        for j in data[i]:
            dist = np.linalg.norm(np.array(j) - np.array(predict))
            distances.append([dist,i])

    votes = [i[1] for i in sorted(distances)[:k]]
    return Counter(votes).most_common(1)[0][0]

if __name__ == '__main__':
    data = {'1':[[1,2],[2,3]], '2':[[8,7],[7,5]]}
    print(kNearestNeighbors(data, [3,4]))

