from sklearn import preprocessing
import numpy as np
enc = preprocessing.OneHotEncoder(sparse=False)
a_tmp = [[0],[1], [2], [3],[4]]
onehot = enc.fit_transform(a_tmp)
a_batch = np.array(onehot)
print(a_batch)