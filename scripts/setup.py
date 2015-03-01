#!/usr/bin/python
# -*- coding: utf-8 -*-

# Feast your eyes on the most pythonic code ever written.

import os
import sys

HOME_DIR = os.path.expanduser("~")
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

if sys.platform == "darwin" and raw_input('Do you want to configure homebrew? y/n: ') == 'y':
    sys.stdout.write("Setting up homebrew... \n")
    if not os.path.exists(os.path.join("/usr/local/bin", "brew")):
        os.system('ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    with open(os.path.join(SCRIPT_DIR, "brew")) as brew:
        for package in brew.readline().split():
            sys.stdout.write("Installing {}\n".format(package))
            os.system("brew install {} > /dev/null 2>&1".format(package))

    do_you_want = 'Do you want to install {}? y/n: '
    if raw_input(do_you_want.format('Firefox')) == 'y':
        sys.stdout.write('Installing firefox...\n')
        os.system('brew cask install firefox')

    if raw_input(do_you_want.format('Chrome')) == 'y':
        os.system('brew cask install google-chrome')

    if raw_input(do_you_want.format('Dash')) == 'y':
        os.system('brew cask install dash')

    sys.stdout.write("Done installing packages\n\n");

sys.stdout.write("Setting up vim... \n")
os.chdir("../vim")
VIM_DIR = os.path.abspath(os.curdir)
try:
    os.symlink(os.path.join(VIM_DIR, "vimrc"), os.path.join(HOME_DIR,  ".vimrc"))
except OSError:
    os.rename(os.path.join(HOME_DIR, ".vimrc"), os.path.join(HOME_DIR, ".vimrc.OLD"))
    os.symlink(os.path.join(VIM_DIR, "vimrc"), os.path.join(HOME_DIR, ".vimrc"))
try:
    os.symlink(VIM_DIR, os.path.join(HOME_DIR, ".vim"))
except OSError:
    os.rename(os.path.join(HOME_DIR, ".vim"), os.path.join(HOME_DIR, ".vim.OLD"))
    os.symlink(VIM_DIR, os.path.join(HOME_DIR, ".vim"))

sys.stdout.write('Setting up git...\n')
os.chdir('../git')
GIT_DIR = os.path.abspath(os.curdir)
try:
    os.symlink(os.path.join(GIT_DIR, 'gitignore_global'), os.path.join(HOME_DIR, '.gitignore_global'))
except:
    os.rename(os.path.join(HOME_DIR, ".gitignore_global"), os.path.join(HOME_DIR, ".gitignore_global.OLD"))
    os.symlink(os.path.join(GIT_DIR, "gitignore_global"), os.path.join(HOME_DIR, ".gitignore_global"))

os.system('git config --global core.excludesfile ~/.gitignore_global')

git_username = raw_input('Enter your git username: ')
git_email = raw_input('Enter your git email: ')
os.system('git config --global user.name "{}"'.format(git_username))
os.system('git config --global user.email "{}"'.format(git_email))

sys.stdout.write("Setting up tmux...\n")
os.chdir("../tmux")
TMUX_DIR = os.path.abspath(os.curdir)
try:
    os.symlink(os.path.join(TMUX_DIR, "tmux.conf"), os.path.join(HOME_DIR, ".tmux.conf"))
except:
    os.rename(os.path.join(HOME_DIR, ".tmux.conf"), os.path.join(HOME_DIR, ".tmux.conf.OLD"))
    os.symlink(os.path.join(TMUX_DIR, "tmux.conf"), os.path.join(HOME_DIR, ".tmux.conf"))

sys.stdout.write("Setting up oh-my-zsh... \n")
if not os.path.exists(os.path.join(HOME_DIR, ".oh-my-zsh")):
    sys.stdout.write("Oh My Zsh wasn't found in the home directory\n")
    install_oh_my_zsh = raw_input("Do you want to install it? y/n: ")
    while install_oh_my_zsh != "y" and install_oh_my_zsh != "n":
        install_oh_my_zsh = raw_input(">")
    if install_oh_my_zsh == "y":
        os.system("curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh")

sys.stdout.write("Setting up zsh... \n")
os.chdir("../zsh")
ZSH_DIR = os.path.abspath(os.curdir)
try:
    os.symlink(os.path.join(ZSH_DIR, "zshrc"), os.path.join(HOME_DIR, ".zshrc"))
except OSError:
    os.rename(os.path.join(HOME_DIR, ".zshrc"), os.path.join(HOME_DIR, ".zshrc.OLD"))
    os.symlink(os.path.join(ZSH_DIR, "zshrc"), os.path.join(HOME_DIR, ".zshrc"))
