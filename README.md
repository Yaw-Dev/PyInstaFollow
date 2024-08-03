# Introduction
**PyInstaFollow** is the simplest tool for finding out who is not following you back.

I know how these tools tend to be and how sketchy they always seem. For this reason I decided to create **PyInstaFollow** and publish it as an open source project.

### So what does it do?
- Get a list of people *following you* (Followers).
- Get a list of people *you follow* (Followees).
- Compare the two lists and see who isn't following you back.
- (NEW) Backup old followers and followees lists.

# Usage
1. `git clone https://github.com/Yaw-Dev/PyInstaFollow`
2. `cd PyInstaFollow`
3. `pip install -r requirements.txt`
4. Fill in your information on *`config.json`* 
5. Finally just run **main.py**

All you have to do now is run "Get Followers" and "Get Followees" at least once. After that you can run "Compare" and get a list of everyone not following you back. Simple as that!

---

> You can now set whether you want the login to happen on program start (every time) or only when using [1] or [2]. This will help lower API calls (login) which may have been useless if the user only wanted to run "Compare". 

- You can do this by changing the `login-on-start` value on `config.json`

**Warning: Using any of the features that require API calls may result in rate-limits or Instagram flagging it as suspicious behavior if done very frequently! Please use with caution.**

## Todo
- add an option for unfollowing everyone that doesn't follow you back (not possible with instaloader)
- write the output of "Compare" to a file
- beautify the cli
- make code less shitty

**Contributions and suggestions are appreciated :)**