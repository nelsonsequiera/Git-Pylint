"""Run pylint on files that are modified or added"""
import os
import sys

from git import Repo
from git.exc import InvalidGitRepositoryError
from pylint import lint


def get_files():
    """Returns the files which should be run.

    If the command is to run staged files then only files in staging are processed.
    Else the files not in staging are processed.
    """
    files = []
    cwd = os.getcwd()
    try:
        repo = Repo(cwd)
    except InvalidGitRepositoryError:
        print "NOT A GIT REPO!!! Please check the path."
        print "This command should be run from base directory of your git repo."
        exit(0)

    if len(sys.argv) > 1 and sys.argv[1] == '-a':
        staged_files = repo.index.diff("HEAD")
        files = [i.a_path for i in staged_files if i.a_path.endswith('.py')]
    else:
        git = repo.git
        u_files = git.status('-s')
        files = get_files_path(u_files)

    print "----------------------------------------------------------------------------"
    if files:
        print "python files got are: ({})".format(len(files))
        for i in files:
            print "\t" + i
    else:
        print "No python changes detected. Nothing to LINT."
    print "----------------------------------------------------------------------------"

    return files


def get_files_path(u_files):
    """Returns full path of the file wrt base directory.

    WHen we do git status, the result is in unicode format.
    We need to parse the string and get filename into list.
    """
    files = []

    delimiter_new_line = '\n'
    indicator_new_file = '??'
    indicator_modified_file = ' M'
    indicator_python_file = '.py'

    for each_file in u_files.split(delimiter_new_line):
        if each_file.endswith(indicator_python_file):
            if each_file.startswith(indicator_new_file):
                files.append(each_file.replace(indicator_new_file, '').strip())
            elif each_file.startswith(indicator_modified_file):
                files.append(each_file.replace(indicator_modified_file, '').strip())
    return files


def run_pylint(files):
    """runs pylint on given files"""
    disable_args = ['--disable=line-too-long']
    # in case you want to disable more options, do:
    # disable_args.append('--disable=too-few-public-methods')
    msg_args = []
    # If you want change format of message displayed, do:
    # msg_args = ["--msg-template={path}:{line}: [{msg_id}({symbol}), {obj}] {msg}"]
    args = disable_args + msg_args + files
    lint.Run(args, exit=False)


if __name__ == '__main__':
    FILES = get_files()
    if FILES:
        run_pylint(FILES)
    else:
        exit(0)
