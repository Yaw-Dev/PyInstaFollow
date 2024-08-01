import instabot as pyinstafollow
import instaloader
import time
import json
import os

print("[+] Welcome to PyInstaFollow!")

with open("config.json", "r", encoding="utf-8") as file:
    login_data = json.load(file)
    username = login_data["username"]
    password = login_data["password"]
    login_on_start = login_data["login-on-start"]

L = instaloader.Instaloader()
is_logged_in = False

def login():
    try:
        print("\n[+] Logging in...")
        L.login(username, password)
        print("[+] Logged in!")
    except Exception as e: 
        print("[!] Login failed:\n" + str(e))
        print("\n[+] Press Enter to continue..."); os.system("pause > nul"); os.system("cls")

def read_usernames_from_csv(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        return set(line.strip() for line in file)
    
if login_on_start:
    login()
    is_logged_in = True

while True:
    print("\nSelect an option:\n[1] Get Followers\n[2] Get Followees\n[3] Compare\n")
    user_choice = input(">> ")
    match user_choice:
        
        case '1': 
            if not login_on_start and not is_logged_in:
                login()
            pyinstafollow.follow_handler("followers", L)

        case '2': 
            if not login_on_start and not is_logged_in:
                login()
            pyinstafollow.follow_handler("followees", L)

        case '3':
            if os.path.exists("output\\followers.csv") and os.path.exists("output\\followees.csv"):
                os.system("cls")
                print("[+] List of people not following you back will be printed below.\n")
                time.sleep(1)
                followers = read_usernames_from_csv('output\\followers.csv')
                followees = read_usernames_from_csv('output\\followees.csv')
                non_followers = followees - followers

                for username in non_followers:
                    print(username)
            else: print("[!] Error: Files are missing...\nPlease run options [1] and [2] before comparing.")
        
        case _: print("[!] Invalid option. Please try again.")
        
    print("\n[+] Press Enter to continue..."); os.system("pause > nul"); os.system("cls")