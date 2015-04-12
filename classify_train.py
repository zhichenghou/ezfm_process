from sklearn import linear_model
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
import numpy as np
import matplotlib.pyplot as plt
import os
import classify_predict

def load_Y(sample_size, songs):
	size_per_s = 8400/8270.0
	Y = np.zeros((sample_size),dtype=np.int)

	for i in range(0, len(songs)):
		begin_s = songs[i][0]
		end_s = songs[i][1]
		Y[int(begin_s*size_per_s): int(end_s*size_per_s)] = 1

	return Y

def lgr_train(X, Y):
	logreg = linear_model.LogisticRegression()
	logreg.fit(X, Y)
	return logreg

def svm_train(X, Y):
	clf = svm.SVC()
	clf.fit(X, Y)
	return clf

def knc_train(X, Y):
	knc = KNeighborsClassifier(n_neighbors=3)
	knc.fit(X, Y) 
	return knc



if __name__ == '__main__':

	modi_modi = "feature/0324_modi.txt"
	X_0 = np.loadtxt(modi_modi)
	
	songs = [[710,980],   [1758,1980], [2380,2595],
		 [2690,2955], [3433,3890], [4865,5106],
		 [5420,5688], [6365,6860], [7560,7998]]

	Y_0 = load_Y(len(X_0),songs)


	modi_modi = "feature/0325_modi.txt"
	X_1 = np.loadtxt(modi_modi)

	songs = [[348,590],   [1100,1313], [1605,1783],
		 [2114,2314], [2690,2895], [3384,3850],
		 [4020,4134], [4840,5235], [5420,5700],
		 [6200,6630], [6870,7120], [7650,8096]]

	Y_1 = load_Y(len(X_1),songs)

	X = np.concatenate((X_0, X_1))
	Y = np.concatenate((Y_0, Y_1))

	print np.shape(X[:,:]), np.shape(Y[:])

	# clf = svm_train(X, Y)
	# joblib.dump(clf, "model/svm.pkl")
	clf = joblib.load("model/svm.pkl")

	Y_p = clf.predict(X[:,:])

	Y_pp = classify_predict.process_Y_p(Y_p)


	plt.figure()
	plt.plot(-0.2)
	plt.plot(1.2)
	plt.plot(Y[2800:10000],'b')
	plt.plot(Y_pp[2800:10000],'r')
	plt.show()
