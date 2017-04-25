# Git-Pylint
Run Pylint with the help of Git

Runs "pylint" on the files which are modified.

There are two cmds:

	• pycheck : this cmd runs "pylint" on only those files which are modified and are NOT in staging area.
	• pycheck -a : this cmd runs "pylint" on only those files which are modified and are IN staging area.

Steps to install:

	• Clone the repo to any directory.
	• From your terminal, navigate to the repo, and find the file "git_pylint_install_script.py"
	• Run the cmd: python git_pylint_install_script.py
	• Restart your terminal

Steps to use Git-Pylint:

	• From your terminal, navigate to your project folder. (This should be the base directory of your project)
	• Run the cmd: pycheck
	
