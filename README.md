# std_googleAssistant
This repository .... [describe what this repo. is for..]

# Project Guide Lines
### 1- Prepare the RaspberryPi (RPi). We will use RPi 3:
 - Instruction for installing Raspbian on the SD Card can be found [here](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).
 - Raspbain image can be download from [here](https://www.raspberrypi.org/downloads/raspbian/).
 - Raspbian already comes bundled with Python 2.7 and Python 3. No need to install Python 🎉 . 
 - ⚠️We will use Python 2.7. Python 3 has the same syntax except with minor differences. For now, it's safe to assume the only difference that matters is the print function :
 
 
 python 2.7:
```python
print "hello world!"
```

 python 3:
```python
print ("hello world!")
```

### 2- Instruction for installing Google Assistant on RPi
- Follow [this tutorial](https://developers.google.com/assistant/sdk/guides/library/python/) on how to install Google Assistant on RPi.

######  If you have time sync problems, you can use the htpdate tool which retrieves time from a given website.
- First, install htpdate using apt-get:
```bash
sudo apt-get install htpdate 
```

- Next, type this commnad everytime you open a terminal:
```bash
sudo  htpdate -q -d -s www.raspberrypi.org
```

- If you don't want to write it everytime. You can put this command in the '.bashrc' file. The '.bashrc' file is a bash script that runs everytime you open a terminal. To add the command to the basrc file, open it with the "nano" text editor as follows (with sudo for root privilege-equivelent to admin rights in windows PC):
```bash
 sudo nano ~/.bashrc
```
Once opened, add the command to the last line of the file. Save it with <kbd>ctrl</kbd>+<kbd>X</kbd>, press <kbd>y</kbd> (yes), then <kbd>Enter</kbd>.
### 3- Learn Python:
- Python tutorial [here](https://www.tutorialspoint.com/python/index.htm). Topics needed are:
    - Python - Home
    - Python - Overview
    - Python - Environment Setup
    - Python - Basic Syntax
    - Python - Variable Types
    - Python - Basic Operators
    - Python - Decision Making
    - Python - Loops
    - Python - Numbers
    - Python - Strings
    - Python - Lists
    - Python - Tuples
    - Python - Dictionary
    - Python - Functions
    - Python - Modules
    - Python - Exceptions
    - Python - Classes/Objects


### 4- Extend Google Assistant capabilities by defining custom actions.

### 5- Integrate with your device.
