## Capstone Project: Medical Record Maintenance BOT, T-229
The Project is carried out under the guidance of Dr. T. S. Chandar. This is the entire code repository for the Final Year Project (7th - 8th SEM).

The Project has completed the Phase 1 and now moving into the Phase 2 in which the following domains will be implemented in software.

- [x] Code for NFC Generation
- [ ] Code for Token Generation
- [x] UI Design for Kiosk
- [x] Software Design for Doctor's end

## Libraies for Code
NFC-Gen-Code:
- Refer to NFC-Gen-Code/Libraries folder.

Token-Gen-Code:
- Refer to Token-Gen-Code/Libraries folder. 

UI-Design-Code:
- Install the following for packages,
	```
	pip install pyqt5 pyuic5-tool logging paramiko opencv-python numpy pytesseract pillow gTTS playsound SpeechRecognition
	```
- Also, download and install QT Designer Tool from [here](https://www.qt.io/download-open-source?hsCtaTracking=9f6a2170-a938-42df-a8e2-a9f0b1d6cdce%7C6cb0de4f-9bb5-4778-ab02-bfb62735f3e5).

Software-Design-Code:
- Install the following for packages,
	```
	pip install pyqt5 pyuic5-tool paramiko opencv-python numpy pytesseract pillow pycopy-webbrowser reportlab
	```
- Also, download and install QT Designer Tool.


## Team Members
- Shashank K S
- Srinivas Bhat
- Mahesh M
- Tejas Patil

## Git and GitHub Usage
Firstly, in order to contribute to this repo, 
- Install Git from [here](https://git-scm.com/download/win) for Win10.
- Setup your Git profile, open git bash and run,
	```
	git config --global user.name "<Name>"
	git config --global user.email <email>
	```
- Now, to clone this repo into your folder, open git bash in that folder and run,
	```
	git clone https://github.com/s3-jarvis/Capstone-Project-T229.git
	```
- Now that a clone of this repo is created in your machine, need to follow the workflow as given below,
	- After adding files, open git bash in the repo and run,
		```
		git add .
		```
	- The files are staged and are ready to be commited, so run,
		```
		git commit -m "<Commit Message>"
		```
	- After a successful commit, you need to update the GitHub repo as well, so run,
		```
		git push
		```
- The above mention workflow is for adding new files or making changes in the existing files. The most important thing in GitHub is to keep the repo updated in both places (remote as well as local). Hence to maintain the changes from the previous commit point, remember to run this command before you start your work,
	```
	git pull
	```

<Comment Style>

