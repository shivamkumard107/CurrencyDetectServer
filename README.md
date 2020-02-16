# Indian Currency Detection using opencv and brute force matching

This code is based on opencv orb feature detection. SURF and SIFT features can also be used to extract the notes features. 
You can change the value of number of features detected by changing n_features in detect.py. Further brute force matching is used for matching the templates with existing notes. 

An audio file with the note detected is executed.


https://drive.google.com/open?id=1W3xMiVxuCWw58PRCZ3p8IOqROrXe0Y66 
This is the dataset link and just copy the audio and files folder in the same folder of github repo


To run do
```python3 detect.py```

To set a different image modify the ```testing_image``` in detect.py

The failed parts are in try.py

To get better results increase the number of images of each note type covering different image conditions like background lightning and angle. Concurrently change the dictionary in detect.py or if the dataset is very large you can use a for loop for creating dictionary using glob. 

