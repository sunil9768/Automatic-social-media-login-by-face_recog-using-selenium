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
 
    
    
    
    
    
    










