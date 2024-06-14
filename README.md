# Robot Codebase

## Description
This codebase houses submodules and utility code to bring together various robotic systems. It also provides scripts and all other software needs for codebase management.  

## File Structure
`scpt` - See here for some scripts regarding codebase management
`src`  - Source code of project

### Programming Summary
The majority of this codebase is written in python and shouldn't require any compilation to be used. For more information on code functionality please see the [src](src) directory.

### Running/Execution
To clone the source code use this command

    git clone --recurse-submodules https://github.com/Package-Repository/robot

It's important to recurse submodules so you can edit each project separately. It's also very important to note that if you change a submodule git will automatically generate a branch for you so you might want to checkout the main/master branch. Also when you commit to the submodule, you will have to commit that you changed the submodule in this module. Yes it is slightly annoying.

I prefer to keep executable and source code separate so there is a [install.sh](scpt/install.sh) script that will place all python files into a ROBOT_LIB directory. Run that script in the root directory of this project so that it copies all files to be executed. This directory is (should be) included in the PATH environment variable from the ~/.bashrc so it can serve as a convenient single point of storage for executed code. To run any script, you can omit the interpreter and any other syntax, just write the file name directly into the terminal - ie. executable.py 
