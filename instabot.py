import csv
import json
import instaloader

global username_to_scrape
with open("config.json", "r", encoding="utf-8") as file:
    login_data = json.load(file)
    username_to_scrape = login_data["username"]

def follow_handler(mode, L):
    global username_to_scrape
    try:
        profile = instaloader.Profile.from_username(L.context, username_to_scrape)
        if mode == "followers":
            to_print = "Getting followers from: "
            filename = 'output\\followers.csv'
            follow_count = profile.followers
            follow_generator = profile.get_followers()
        else: 
            to_print = "Getting followees from: "
            filename = 'output\\followees.csv'
            follow_count = profile.followees
            follow_generator = profile.get_followees()

        print(to_print + username_to_scrape)
        with open(filename,'w',newline='',encoding="utf-8") as csvf:
            csv_writer = csv.writer(csvf)
        total=0
        for person in follow_generator:
            try:
                total+=1
                username = person.username
                with open(filename,'a', newline='', encoding='utf-8') as csvf:
                    csv_writer = csv.writer(csvf)
                    csv_writer.writerow([username])
                print(f'{username} ({total}/{follow_count})')
            except Exception as e: print(e)
        
        print("File written: Check 'output' folder.")
    except Exception as e: print(e)