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