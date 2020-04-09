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
test_img = read_img('files/2000_test.jpg')
# resizing must be dynamic
original = resize_img(test_img, 0.4)
display('original', original)

# keypoints and descriptors
# (kp1, des1) = orb.detectAndCompute(test_img, None)
(kp1, des1) = orb.detectAndCompute(test_img, None)

training_set = ['500_1.jpg', '500.5.jpg', '500.3.jpg', 'test_20_1.jpg', '10.5.jpg', '2000.6.jpg', '10.6.jpg', '2000.3.jpg', '50.jpg', 'test_100_3.jpg', '20.1.jpg', 'test_50_2.jpg', '20.5.jpg', '100.2.jpg', '50_newback.jpg', '100_3.jpg', '500_2.jpg', '100_2.jpg', '100.5.jpg', '2000back.jpg', '10.2.jpg', '50.5.jpg', '10test.jpg', '20back.jpg', '20.4.jpg', '100.jpg', '500.4.jpg', '2000.5.jpg', 'test500.jpeg', 'test20.jpeg', '500.6.jpg', '50.3.jpg', '200.jpg', '100.4.jpg', '500.2.jpg', '50.4.jpg', 'test_20_4.jpg', '2000.2.jpg', '200.5.jpg', '500back.jpg', '20_newback.jpg', 'test50.jpeg', 'test_50_1.jpg', '10.1.jpg', '100.1.jpg', '500.1.jpg', '10.3.jpg', '10.jpg', '100.3.jpg', '200.4.jpg', '200.3.jpg', '50.6.jpg', '100back.jpg', '20.2.jpg', 'test_20_2.jpg', 'test_100_2.jpg', '50.1.jpg', '10_new.jpg', '2000.jpg', 'test_20_3.jpg', '10.4.jpg', '200.2.jpg', '20.jpg', '500test.jpg', '200.6.jpg', '2000.4.jpg', '20.3.jpg', '500.jpg', '10_newback.jpg', '10back.jpg', '100_newback.jpg', '200.1.jpg', '100.6.jpg', '10_1.jpeg', '50_new.jpg', 'test_500_2.jpg', 'test_100_1.jpg', '50.2.jpg', '20.6.jpg', '2000.1.jpg']

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
