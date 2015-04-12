import mfcc_feat
import modi_feat
import classify_predict
import sh

import matplotlib.pyplot as plt
import numpy as np
import mp3_utils


def main():
	mp3_file = "mp3/ezm150324.mp3"
	wav_dir = "wav"
	mfcc_dir = "feature/0324"
	sh.run("mkdir -p " + mfcc_dir)
	modi_file = "feature/0324_modi.txt"
	result_file = "result/0324.txt"
	mfcc_feat.run(mp3_file, wav_dir, mfcc_dir)
	modi_feat.run(mfcc_dir, modi_file)
	# cut_point = classify_predict.run(modi_file, result_file)
	# print cut_point


	# tmp = "tmp"
	# mp3_utils.cut(mp3_file, cut_point, tmp)
	# mp3_utils.concat(cut_point, tmp, "mp3")


	# xx = np.loadtxt(modi_file)
	# rs = np.loadtxt(result_file)
	# plt.figure()
	# plt.plot(rs)

	# plt.show()



if __name__ == '__main__':
	main()