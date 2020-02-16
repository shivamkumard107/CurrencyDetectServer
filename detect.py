#!/usr/bin/python

# test file
# TODO:
# 	Figure out four point transform
#	Figure out testing data warping
# 	Use webcam as input
# 	Figure out how to use contours
# 		Currently detects inner rect -> detect outermost rectangle
# 	Try using video stream from android phone


from utils import *
from matplotlib import pyplot as plt

import subprocess
from gtts import gTTS
from playsound import playsound



max_val = 8
max_pt = -1
max_kp = 0

orb = cv2.ORB_create(nfeatures=2500)
# orb is an alternative to SIFT

#test_img = read_img('files/test_100_2.jpg')
#test_img = read_img('files/test_50_2.jpg')
#test_img = read_img('files/500test.jpg')
#test_img = read_img('files/test_100_3.jpg')
#test_img = read_img('files/10test.jpg')
test_img = read_img('files/test20.jpeg')
# resizing must be dynamic
original = resize_img(test_img, 0.4)
display('original', original)

# keypoints and descriptors
# (kp1, des1) = orb.detectAndCompute(test_img, None)
(kp1, des1) = orb.detectAndCompute(test_img, None)

training_set = ['files/10.jpg','files/10_1.jpeg','files/10back.jpg','files/10_new.jpg','files/10_newback.jpg','files/20.jpg','files/20back.jpg','files/20_new.jpg' ,'files/20_newback.jpg','files/50.jpg','files/50back.jpg', 'files/50_new.jpg', 'files/50_newback.jpg','files/100.jpg','files/100back.jpg', 'files/100_new.jpg','files/100_newback.jpg','files/200.jpg','files/500.jpg','files/500back.jpg','files/500_1.jpg','files/500_2.jpg']

for i in range(0, len(training_set)):
	# train image
	train_img = cv2.imread(training_set[i])

	(kp2, des2) = orb.detectAndCompute(train_img, None)

	# brute force matcher
	bf = cv2.BFMatcher()
	all_matches = bf.knnMatch(des1, des2, k=2)

	good = []
	# give an arbitrary number -> 0.789
	# if good -> append to list of good matches
	for (m, n) in all_matches:
		if m.distance < 0.789 * n.distance:
			good.append([m])

	if len(good) > max_val:
		max_val = len(good)
		max_pt = i
		max_kp = kp2

	print(i, ' ', training_set[i], ' ', len(good))

if max_val != 8:
	print(training_set[max_pt])
	print('good matches ', max_val)

	train_img = cv2.imread(training_set[max_pt])
	img3 = cv2.drawMatchesKnn(test_img, kp1, train_img, max_kp, good, 4)
	
	note = str(training_set[max_pt])[6:-4]
	print('\nDetected denomination: Rs. ', note)

	audio_file = 'audio/' + note + '.mp3'
	print(audio_file)

	# audio_file = "value.mp3
	# tts = gTTS(text=speech_out, lang="en")
	# tts.save(audio_file)
	
	playsound(audio_file)
	
else:
	print('No Matches')
