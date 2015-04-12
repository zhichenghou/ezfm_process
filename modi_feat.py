import os
import numpy as np
import sh
import matplotlib.pyplot as plt


def modify_feat(input_mfcc_feat):
	mfcc_feat = np.loadtxt(input_mfcc_feat)

	sample_size = len(mfcc_feat)
	time_in_s = 600
	size_per_s = sample_size / time_in_s

	time_window = 1
	modi_feat = []
	for j in range(0, len(mfcc_feat[0])):
		xx = []
		for i in range(0, time_in_s, time_window):
			# max_a = np.max(mfcc_feat[i*size_per_s: (i+time_window)*size_per_s, j])
			# min_a = np.min(mfcc_feat[i*size_per_s: (i+time_window)*size_per_s, j])
			# xx.append(max_a - min_a)
			xx.append(np.std(mfcc_feat[i*size_per_s: (i+time_window)*size_per_s, j]))
		modi_feat.append(xx)

	print np.shape(modi_feat)

	return np.transpose(modi_feat)
	# np.savetxt(output_modi_feat, np.transpose(mode_feat))

def run(mfcc_dir, modi_feat_file):
	mfcc_feat_list = os.listdir(mfcc_dir)

	modi_feat = []
	for file_name in mfcc_feat_list:
		print mfcc_dir + "/" + file_name
		d = modify_feat(mfcc_dir + "/" + file_name)
		if len(modi_feat) == 0:
			modi_feat = d
		else:
			modi_feat = np.concatenate((modi_feat,d))

	print np.shape(modi_feat)

	np.savetxt(modi_feat_file, modi_feat)

# def modi_modi(modi_feat_file, modi_modi_file):
# 	modi_feat = np.loadtxt(modi_feat_file)

# 	sample_size = len(modi_feat)
# 	size_per_s = 1
# 	time_in_s = sample_size * size_per_s

# 	time_window = 5
# 	modi_modi = []
# 	for j in range(0, len(modi_feat[0])):
# 		xx = []
# 		for i in range(0, time_in_s, time_window):
# 			# max_a = np.max(mfcc_feat[i*size_per_s: (i+time_window)*size_per_s, j])
# 			# min_a = np.min(mfcc_feat[i*size_per_s: (i+time_window)*size_per_s, j])
# 			# xx.append(max_a - min_a)
# 			xx.append(np.mean(modi_feat[i*size_per_s: (i+time_window)*size_per_s, j]))
# 		modi_modi.append(xx)

# 	print np.shape(modi_modi)

# 	np.savetxt(modi_modi_file, np.transpose(modi_modi))

# 	return np.transpose(modi_modi)

# def plot(X, subplot_cnt):

# 	mp3_file = 'mp3/ezm150324.mp3'
# 	cmd = """./ffmpeg -i """ + mp3_file + """ 2>&1 | grep "Duration"| cut -d ' ' -f 4 | sed s/,// | awk '{ split($1, A, ":"); print 3600*A[1] + 60*A[2] + A[3] }'"""
# 	rs = sh.run(cmd, True)
# 	duration_in_s = rs.stdout()
# 	print "total duration is " + duration_in_s + "s"

# 	t = np.linspace(0, int(float(duration_in_s)), len(X))

# 	plt.figure()
# 	for i in range(1, subplot_cnt + 1):
# 		plt.subplot(subplot_cnt, 1, i)
# 		plt.plot(t, X[:,i])

# 	plt.show()

if __name__ == '__main__':
	mfcc_dir = "feature/mfcc"
	modi_file = "feature/modi_feat.txt"
	
	modi_all(mfcc_dir, modi_file)

	# modi_feat = np.loadtxt(modi_file)
	# plot(modi_feat, 12)
	# modi_modi = modi_modi(modi_file, modi2_file)
	# plot(modi_modi,12)

	
