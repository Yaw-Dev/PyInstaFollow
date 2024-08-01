# Introduction
**PyInstaFollow** is the simplest tool for finding out who is not following you back.

I know how these tools tend to be and how sketchy they always seem. For this reason I decided to create **PyInstaFollow** and publish it as an open source project.

# Usage
1. `git clone https://github.com/Yaw-Dev/PyInstaFollow`
2. `cd PyInstaFollow`
3. `pip install -r requirements.txt`
4. Fill in your information on *`config.json`*
4. Finally just run **main.py**

All you have to do now is run "Get Followers" and "Get Followees" at least once. After that you can run "Compare" and get a list of everyone not following you back. Simple as that!

**Warning: Using any of the features that require API calls may result in rate-limits or Instagram flagging it as suspicious behavior if done very frequently!**

## Todo
- add an option for unfollowing everyone that doesn't follow you back
- add option to backup followers.csv & followees.csv files for future use
- write the output of "Compare" to a file
- beautify the cli
- make code less shitty

#### Recommendations for new features (or even a new name for this project) will be appreciated :)