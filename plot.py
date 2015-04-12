import matplotlib.pyplot as plt
import numpy as np
import os
import sh
import classify_predict
import classify_train


if __name__ == '__main__':
	modi_file = "feature/0324_modi.txt"
	X, Y = classify_train.load_data(modi_file)

	result_file = "result/tran.txt"
	classify_predict.run(modi_file, result_file)
	Y_p = np.loadtxt(result_file)

	plt.figure()
	plt.plot(-0.2)
	plt.plot(1.2)
	plt.plot(Y,'b')
	plt.plot(Y_p,'r')

	plt.show()

	# mfcc_dir = "feature/0324"
	# mfcc_feat_list = os.listdir(mfcc_dir)

	# modi_feat = []
	# i = 0
	# for file_name in mfcc_feat_list:
	# 	if i > 5: break 
	# 	i+=1
	# 	print mfcc_dir + "/" + file_name
	# 	d = np.loadtxt(mfcc_dir + "/" + file_name)
	# 	if len(modi_feat) == 0:
	# 		modi_feat = d
	# 	else:
	# 		modi_feat = np.concatenate((modi_feat,d))


	# modi_feat = np.loadtxt("feature/0324_modi.txt")[0:2700,:]

	# print np.shape(modi_feat)

	# plt.figure()
	# plt.subplot(3,1,1)
	# plt.plot(modi_feat[:,1])
	# plt.subplot(3,1,2)
	# plt.plot(modi_feat[:,2])
	# plt.subplot(3,1,3)
	# plt.plot(modi_feat[:,3])
	
	# plt.show()


