from sklearn import linear_model
from sklearn.externals import joblib
import numpy as np

def run(modi_file, result_file):
	X = np.loadtxt(modi_file)

	clf = joblib.load("model/svm.pkl")

	Y_p = clf.predict(X[:,:])

	
	Y_pp = process_Y_p(Y_p)

	# cut point
	last = Y_pp[0]
	cut_point=[0]
	sample_size = len(Y_pp)
	for i in range(0, sample_size):
		d = Y_pp[i]
		if d != last:
			print i , d
			cut_point.append(i)
		last = d

	np.savetxt(result_file, Y_pp) 
	
	return cut_point

def process_Y_p(Y_p):
	time_window = 60
	percent = 27
	sample_size = len(Y_p)
	print sample_size
	Y_pp = np.ones((sample_size),dtype=np.int)

	for i in range(0, sample_size):
		d = Y_p[np.max([0, i - time_window]): np.min([i + time_window, sample_size])]
		if (np.sum(d) < percent):
			Y_pp[i] = 0

	# for songs it should be longger than 1.5 min and the gap of two songs is longger than 1.5 min

	last = Y_pp[0]
	last_step = 0
	last_step_value = 0
	delta_s = 150
	for i in range(0, sample_size):
		d = Y_pp[i]
		if d != last:
			delta = i - last_step
			if delta < delta_s:
				Y_pp[last_step:i] = d
			else:
				last_step = i
				last_step_value = d
		last = d

	return Y_pp