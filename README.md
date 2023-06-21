# python-git-venv-tutorial
Basic Python workflow with Github, venv, and VSCode.

### Basic setup steps:
1. create remote repository (with Python `.gitignore` template)
2. clone from remote repo + open project in VSCode
3. install/verify python installation with `brew install python@3.X` on Mac
4. create virtual environment with `venv` using `python3.X -m venv .venv`
5. associate the `.venv` folder with the project in VSCode (`cmd + shift + p` to open command palette > `Python: Select Interpreter`)
6. `pip install` any packages you need
7. `pip freeze > requirements.txt` to export a list of installad packages 
8. create your Python file <pythonfilename>.py
9. run `python` in the terminal to start an interactive session using `.venv`
10. run the Python command `with open('<pythonfilename>.py', 'r') as f: exec(f.read())` to execute your Python file interactively, i.e., with all variables and results in memory


### Basic Git controls:
1. `git status` to see status of local repository (with comparison to remote)
2. `git add .` to add all untracked/changed files
3. `git commit -m "<commitmessage>"` to commit changes locally
4. `git push` to push to the remote repository (`origin` by default)
* `git remote -v` to list remote repo URLs