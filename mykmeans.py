import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import datetime
from sklearn.datasets.samples_generator import make_blobs

def __init_panal__(df):

#   for i in centroids.keys():
#      plt.scatter(*centroids[i], color=colmap[i], s=80)

    plt.figure(figsize=(5, 5))
    plt.scatter(df['x'], df['y'], color='black')
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.show()

    pass

# assign the points to centroids
def assignment(df, centroids, colmap):
    for i in centroids.keys():
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['x'] - centroids[i][0]) ** 2
                + (df['y'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])


    print(df.head())

    plt.figure(figsize=(5, 5))
    plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
    for i in centroids.keys():
        plt.scatter(*centroids[i], color=colmap[i], s=80)
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.show()
    print('assignment: ', datetime.datetime.now().time())
    return df
    pass

# relocate the centroids to the center of each group
def update(centroids, df, colmap):
    for i in centroids.keys():
        centroids[i] = [np.mean(df.loc[df['closest'] == i]['x']), np.mean(df.loc[df['closest'] == i]['y'])]

    plt.figure(figsize=(5,5))
    plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
    for i in centroids.keys():
        plt.scatter(*centroids[i], color=colmap[i], s=80)
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.show()
    print('update: ', datetime.datetime.now().time())
    return centroids
    pass


class kmeans:
    def __init__(self, n_clusters=3):
        self.k = n_clusters

    def fit(self, data):
        self.k
        while True:
            assignment()
            update()
        return label

    def assignment(self):
        pass

    def update(self):
        pass

def main():

    df = pd.DataFrame({'x': [random.random() * 100.0 for _ in range(100)],
                       'y': [random.random() * 100.0 for _ in range(100)]
                       })

    centroids = {
        i + 1: [np.random.randint(0, 80), np.random.randint(0, 80)]
        for i in range(5)
    }

    colmap = {1: 'r', 2: 'g', 3: 'b', 4: 'y', 5: 'm'}



    label = kmeans().fit(data=df, k=3)
    plt.scatter(data[:, 0], data[:, 1], c=label)

    __init_panal__(df)
    df = assignment(df, centroids, colmap)
    centroids = update(centroids, df, colmap)

    # repeat assignment, until all assigned categories don't change anymore
    while True:
        check_change = df['closest']
        df = assignment(df, centroids, colmap)
        centroids = update(centroids, df, colmap)
        if check_change.equals(df['closest']):
            break

    print("Kmeans clustering ready! :)")






if __name__ == "__main__":
    main()


