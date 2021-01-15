# coding:gbk
import os

path = 'movie'
dirlist = os.listdir(path)	# movie/dirname*

for dirname in dirlist:	#everyone movie dirname
	i = 1
	os.chdir(path)
	files = os.listdir(dirname) # movie/dirname/filename*
	os.chdir(dirname)
	print(dirname + ':')
	for filename in files:	# everyone movie filename
		if i < 10:
			newname = "00" + str(i) + dirname + ".mp4"
		else:
			newname = "0" + str(i) + dirname + ".mp4"
		print(newname)
		os.rename(filename, newname)
		i += 1
	os.chdir('../../')