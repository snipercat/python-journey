# Initial config

This is the step by step to star a new project on Python using Vs code and Git.

## Install Software

Considering you have an fresh PC, these are the tools you'll need.

### Python

Go to https://www.python.org/ and download the latest Python version.
currently **Python 3.14.3**.

When installing, check "*Add Python to PATH*"

### Visual Studio Code (VS Code)
Download Vs Code from https://code.visualstudio.com/
Open VS Code, go to Extensions (crl + shift + X) search for Python Extension and install it.
this will install these extensions:

* Python
* Pylance
* Python Debugger
* Python Environments



###  GIT
Download from https://git-scm.com/


## Create Project and Environments

Create a folder on the location you want your project.
on VS code select `File > Open folder` and select your folder.

Open the terminal with `View > Terminal` (crl+ `) and run:

`py -m venv .venv`
or 
`python -m venv .venv`

This will create a folder called `.venv` where you'll store dependences and configuration

add permissions to the environment with

`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

then activate thee environment

`.venv\Scripts\Activate.ps1`

You'll know this was activated because you'll see (.venv) at the start of the console path


## Initialize GIT

On root folder create a file called `.gitignore` and add these lines to avoid upload heavy or unnecessary files, you can add more files later

```
.env
.venv/
__pycache__/
*.pyc
```

Run these commands, you can use gitBash on the root folder or the console from Vs Code

```bash
# Create empty repository
git init

# prepare all files for the snapshot
git add .

# set your identity, you can ommit --global
# if you only want to set the indentity for this repository
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

# Makes the first commit                     
git commit -m "Initial commit: Your message here"
```

## Connect to GitHub
1. **Create Repository on GitHub**:
   * Go to https://github.com/ login wiht your account and create a new repository.
   * Do **not** initialize with .gitignore since you already have them locally.
   * Copy the remote repository URL (it looks like `https://github.com/your-user/your-repo.git`).

2. **Link Local to Remote**:
In your terminal, run the following commands:

```bash
# Add the remote URL as 'origin'
git remote add origin  https://github.com/your-user/your-repo.git

# Rename your local branch to 'stable' (if not already)
git branch -M stable

# Push your code to GitHub
git push -u origin stable
```

# Security Recommendations

## Protect your Credentials

 **Never upload `.env` files**: These files often contain passwords or API keys. Always ensure `.env` is listed in your `.gitignore`.

**Token Safety**: The token stored by Git is local to your machine. If you use a public or shared PC, **always** sign out and clear the Git Credentials Manager using these commands.
```bash
git credential-manager clear
git config --unset user.name
git config --unset user.email
```

## GitHub Account Security
**Enable 2FA**: Go to `Settings > Password and Authentication` and enable Two-Factor Authentication.
**Review Sessions**: Periodically check `Settings > Sessions` to ensure only your trusted devices have access.
