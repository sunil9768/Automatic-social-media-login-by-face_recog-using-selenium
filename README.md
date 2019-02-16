**Project Title**






Automatic-social-media-login-by-face_recog-using-selenium



**Installing**(in Ubntu 18.04)



1. **Install Anaconda3 in terminal:**
    >wget https://repo.anaconda.com/archive/Anaconda3-5.0.1-Linux-x86_64.sh  
    >[See Screenshort](https://github.com/sunil9768/Automatic-social-media-login-by-face_recog-using-selenium/blob/master/install-anaconda-ubuntu003.png)
    
    
    Next, we need to download Anaconda. First, we change into the Temp directory:
    > cd /tmp/
    
    
    
    >[See Screenshort](https://github.com/sunil9768/Automatic-social-media-login-by-face_recog-using-selenium/blob/master/install-anaconda-ubuntu002.png)
    
    >Install Anaconda
    
    >[See Screenshort](https://github.com/sunil9768/Automatic-social-media-login-by-face_recog-using-selenium/blob/master/install-anaconda-ubuntu005-300x57.png)   
    
    
2. **After install Anaconda3 then we go to terminal there.we write**


   >anaconda-navigator


   >[you see](https://github.com/sunil9768/Automatic-social-media-login-by-face_recog-using-selenium/blob/master/Screenshot%20from%202019-02-16%2016-44-43.png)
    
    
    
    > Successfully Installed:+1:
    
    
  3.**Necessary module will  be installed in terminal**
 
 >sudo apt-get install python3.6
 
 Use the following command to install pip for Python 3:
 
 
 >sudo apt install python3-pip
 
 
 Once the installation is complete, verify the installation by checking the pip version:
 
 
 
 
 >pip3 --version
 
 
 To install this package with conda run:
 
 
 
 
 >conda install -c anaconda anaconda 
 
 
 Now, let’s install NumPy:
 
 
 
 >sudo apt install python3-numpy
 
 
 
 
 If you need OpenCV, you can install it with:
 
 
 
 >sudo apt install python3-opencv
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 **Description**
 
 
 1.**Face Recognition**
 
 
 
 >Recognize and manipulate faces from Python or from the command line with the world's simplest face recognition library.

>Built using dlib's state-of-the-art face recognition built with deep learning. The model has an accuracy of 99.38% on the Labeled Faces in the Wild benchmark.

>This also provides a simple face_recognition command line tool that lets you do face recognition on a folder of images from the command line!


To install dlib before Face Recognition, run this command in your terminal:

 First, dlib installed with Python bindings:
 
 
 >git clone https://github.com/davisking/dlib.git
 
 
 Build the main dlib library (optional if you just want to use Python):
 
 
 
 >cd dlib
 >mkdir build; cd build; cmake ..; cmake --build .
 
 
 Build and install the Python extensions
 
 
 
 >cd ..
 >python3 setup.py install
 
 
 
 At this point, you should be able to run python3 and type import dlib successfully.:+1:
 
 
 After install Face_recognition
 
 
 

 > pip3 install face_recognition
 
 
 
**How Face Recognition Works**

If you want to learn how face location and recognition work instead of depending on a black box library, [read](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78)


2.**Selenium**
> This is a quick introduction to [Selenium](https://www.seleniumhq.org/) [WebDrive](http://www.aosabook.org/en/selenium.html) in Python on Ubuntu/Debian systems.

>WebDriver (part of Selenium 2) is a library for automating browsers, and can be used from a variety of language >bindings. It allows you to programmatically drive a browser and interact with web elements. It is most often used for >test automation, but can be adapted to a variety of web scraping or automation tasks.

>To use the WebDriver API in Python, you must first install the Selenium Python bindings. This will give you access to >your browser from Python code. The easiest way to install the bindings is via [pip](https://pip.pypa.io/en/stable/).

>On Ubuntu/Debian systems, this will install pip (and dependencies) and then install the Selenium Python bindings from [PyPI](https://pypi.org/project/selenium/): 


>sudo apt-get install python-pip
>sudo pip install selenium

After the installation, the following code should work: 


>#!/usr/bin/env python

>from selenium import webdriver

>browser = webdriver.Chrome([path of drive](https://github.com/sunil9768/Automatic-social-media-login-by-face_recog-using-selenium/tree/master/chromedriver_linux64(1)))





>browser.get('http://www.ubuntu.com/')

**Note**This small piece of code will log-in an account automatically like facebook,instagram,github,linkedin. 


**How to run this program in terminal**


>python3 face.py



After face_recognition Automatic open social media(instagram,facebook,linkedin,github) according to your choice
 

    
    
    
    
    










