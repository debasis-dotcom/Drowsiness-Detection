# Drowsiness-Detection

## Description 📌
In this project we are going to learn how to use computer vision and openCV to detect drowsiness. We first look into eye tracking and then we identify 16 landmarks sorrounding the eye which we will use to calculate the area, inorder to know if the person is drowsing or not. 

Here, each eye is represented by 16 (x, y)-coordinates, starting at the left-corner of the eye, and then working clockwise around the eye. After sucessfully locating the landmarks it then find the area formed by those landmarks. If the eye is completly closed then the area is almost zero and it increases subsequently as the eyes open. 

We have taken a threshold of 50 to detect if the eye is closed or not and this threshold will vary depending where we are deploying this model and needs to be adjusted accordingly.
It checks 10 consecutive frames and if the area formed by those eyes landmarks is less than 0.5, then Alert is generated.

## Mathematics
We have used the famous shoelace formula to calculate the area formed by the eyes andmarks.
The maths behind calculating the area has been shown below,

![](https://github.com/debasis-dotcom/Drowsiness-Detection/blob/main/ShoelaceFormula.PNG)

## Applications 🎯
- This model can be delpoyed in those vehicles where the drivers who tend to drive for a longer period of time may feel drowsy. As such incident may lead to accidents.
- This model can also be used to detect those persons who are in charge of security of particular place or premises.

## Packages Used
- OpenCV
- Mediapipe
- NumPy

## How to use?
Step 1: Clone this repository on your local computer

git clone https://github.com/debasis-dotcom/Drowsiness-Detection

Step 2: Install all the requirements

pip install mediapipe
pip install opencv-python
Or else if you are using pyCharm then you can directly add by going through its setting --> interpreter --> add

Step 3: Run the program

![Demo](https://github.com/debasis-dotcom/Drowsiness-Detection/blob/main/SampleOutputVideo.gif)
