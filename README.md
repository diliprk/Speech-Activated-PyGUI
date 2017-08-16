# Speech - Activated GUI
![alt text](https://github.com/thunderkatzen/Speech-Activated-PyGUI/raw/master/GUI%20MockUp.png)
Implemented using Python 2.7.11 using packages like pygame, sys, speech_recognition.
 In this project we activate GUI elements like light blinking and fan rotation using speech commands. To run this ( SAGUI.py ) python script first you have to install Python version 2.7.11 (on PC or Mac) with a built-in mic or working external microphone. The following libraries need to installed using Python's Package Installer.
- pip install pygame
- pip install pyaudio
- pip install SpeechRecognition

## Project Setup & Execution Instructions:
The instructions which appear in the GUI window which opens when you run the SAGUI.py file should be self-explanatory. Some other miscellaneous tips:
- There must be no background noise when speaking the hotwords
Press SpaceBar and speak the hot words slowly, clearly, and close to the microphone
- Wait for some 20-30 secs to see if the action is triggered by your speech.
- If your spoken hotword is successfully detected you will see it printed in the command line, If not repeat the hotword (above steps) again.
