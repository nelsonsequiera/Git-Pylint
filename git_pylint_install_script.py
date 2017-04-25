"""Clones git repo, install necessary packages, and creates alias for git-pylint"""
import os
from os.path import expanduser
import pip

GIT_URL = "git@github.com:nelsonsequiera/Git-Pylint.git"
HOME_PATH = expanduser("~") + '/'
REPO_PATH = os.getcwd()
GIT_PYLINT_FILE = 'git_pylint.py'
GIT_PYLINT_FILE_PATH = REPO_PATH + '/' + GIT_PYLINT_FILE
FILE_BASH = '.bashrc'
FILE_ZSH = '.zshrc'

ALIAS_CMD = "\n# alias for git-pylint\nalias pycheck='python {}'\n".format(GIT_PYLINT_FILE_PATH)
CMD_TO_SEARCH = "alias pycheck"

HOR_LINE = "--------------------------------------------------------"

# Install packages
# -------------------------------------------------------------------------------------------------
print HOR_LINE + "\nInstalling requirements now...\n" + HOR_LINE
with open(REPO_PATH + "/requirements.txt", "r") as package_list:
    for package in package_list:
        pip.main(['install', package])
print HOR_LINE + "\nFinished installing requirements.\n" + HOR_LINE

# create alias for zsh
# -------------------------------------------------------------------------------------------------
if os.path.isfile(HOME_PATH + FILE_ZSH):
    with open(HOME_PATH + FILE_ZSH, 'a+') as zsh:
        zsh.seek(0, 0)
        if any(CMD_TO_SEARCH in line for line in zsh):
            print "Alias cmd for git-pylint for zsh already created. Shabaash bete!!!"
        else:
            zsh.write(ALIAS_CMD)
            print "Alias cmd created for git-pylint for zsh."
            print "***[PLEASE RESTART]*** terminal / iterm / whatever this is."

# create alias for bash
# -------------------------------------------------------------------------------------------------
with open(HOME_PATH + FILE_BASH, 'a+') as bash:
    bash.seek(0, 0)
    if any(CMD_TO_SEARCH in line for line in bash):
        print "Alias cmd for git-pylint for bash already created. Shabaash bete!!!"
    else:
        bash.write(ALIAS_CMD)
        print "Alias cmd created for git-pylint for bash."
        print "***[PLEASE RESTART]*** terminal / iterm / whatever this is."
print HOR_LINE
