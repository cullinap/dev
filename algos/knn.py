import numpy as np



def kNearestNeighbors(data, predict, k=3):
    distances = []
    
    for i in data.keys():
        for j in data[i]:
            dist = np.linalg.norm(np.array(j) - np.array(predict))
            print(dist)



if __name__ == '__main__':
    data = {'1':[[1,2],[2,3]]}
    kNearestNeighbors(data, [3,4])

