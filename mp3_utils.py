import sh

def cut(mp3_file, cut_point, wav_dir):
	for i in range(0, len(cut_point)):
		if i < len(cut_point) - 1:
			duration = cut_point[i+1] - cut_point[i]
		else:
			cmd = """./ffmpeg -i """ + mp3_file + """ 2>&1 | grep "Duration"| cut -d ' ' -f 4 | sed s/,// | awk '{ split($1, A, ":"); print 3600*A[1] + 60*A[2] + A[3] }'"""
			rs = sh.run(cmd, True)
			duration_in_s = rs.stdout()
			duration = int(float(duration_in_s)) - cut_point[i]

		cmd = "./ffmpeg -ss " + str(cut_point[i]) + " -t " + str(duration)+ " -i " + mp3_file + " " + wav_dir  + "/" + str(i) + ".wav"
		sh.run(cmd)


def concat(cut_point, wav_dir, mp3_dir):
	part_0 = ""
	part_1 = ""
	size_0 = 0
	size_1 = 0
	for i in range(0, len(cut_point),2):
		part_0 += "-i " + wav_dir + "/" + str(i) + ".wav "
		size_0+=1
		if i + 1 < len(cut_point) - 1:
			part_1 += "-i " + wav_dir + "/" + str(i+1) + ".wav "
			size_1+=1

	cmd = "./ffmpeg  " + part_0 + " -filter_complex '[0:0][1:0][2:0][3:0]concat=n=" + str(size_0) + ":v=0:a=1[out]' -map '[out]' " + wav_dir + "/concat_0.wav"
	sh.run(cmd)
	cmd = "./ffmpeg  " + part_1 + " -filter_complex '[0:0][1:0][2:0][3:0]concat=n=" + str(size_1) + ":v=0:a=1[out]' -map '[out]' " + wav_dir + "/concat_1.wav"
	sh.run(cmd)

	# to mp3
	cmd = "./ffmpeg -i " + wav_dir + "/concat_0.wav" + " -q:a 8 " + mp3_dir + "/rs_0.mp3"
	sh.run(cmd)
	cmd = "./ffmpeg -i " + wav_dir + "/concat_1.wav" + " -q:a 8 " + mp3_dir + "/rs_1.mp3"
	sh.run(cmd)