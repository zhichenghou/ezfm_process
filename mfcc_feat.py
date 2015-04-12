from features import mfcc
from features import logfbank
import scipy.io.wavfile as wav
import numpy as np
import sh 

def mfcc_feat(input_wav, output_txt):
	(rate, sig) = wav.read(input_wav)
	mfcc_feat = mfcc(sig, rate)
	np.savetxt(output_txt, mfcc_feat)

	print len(mfcc_feat)


def run(mp3_file, wav_dir, mfcc_feat_dir):
	cmd = """./ffmpeg -i """ + mp3_file + """ 2>&1 | grep "Duration"| cut -d ' ' -f 4 | sed s/,// | awk '{ split($1, A, ":"); print 3600*A[1] + 60*A[2] + A[3] }'"""
	rs = sh.run(cmd, True)
	duration_in_s = rs.stdout()
	print "total duration is " + duration_in_s + "s"
	step_s = 600

	for i in range(0, int(float(duration_in_s)), step_s):
		wav_file = wav_dir + "/" + str(i) + ".wav"
		mfcc_feat_file = mfcc_feat_dir + "/" + str(i) + ".txt"
		cmd = "./ffmpeg -ss " + str(i) + " -t " + str(step_s) + " -i " + mp3_file + " -f wav " + wav_file
		sh.run(cmd)
		print "convert mp3 to wav finish, " + str(i)
		# extract feature
		mfcc_feat(wav_file, mfcc_feat_file)

		# clean files
		cmd = "rm -rf " + wav_dir  + "/*"
		sh.run(cmd)

