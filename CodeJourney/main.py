import json

#To view profile from JSON
try:
       with open("profile.json","r") as file:
             profile=json.load(file)
except FileNotFoundError:
      profile={}

#To view progress from JSON
try:
       with open("progress.json","r") as file:
             progress=json.load(file)
except FileNotFoundError:
      progress=[]  
print("========================================")
print("CodeJourney – Personal Progress Tracker")
print("========================================")

#To store profile in JSON
def save_profile():
      with open("profile.json","w") as file:
            json.dump(profile,file)

#To store progress in JSON
def save_progress():
      with open("progress.json","w") as file:
            json.dump(progress,file)

#To create a new profile
def create_profile():
    global profile
    print("Creating Profile")
    name=input("Enter your Name: ")
    coll=input("Enter your College: ")
    branch=input("Enter your Branch: ")
    sem=input("Enter your Semester: ")
    goal=input("Enter your Daily Coding Goal : ")
    profile={
        "Name":name,
        "College":coll,
        "Branch":branch,
        "Semester":sem,
        "Daily Coding Goal":goal
        }
    print("Profile successfully created!")
    save_profile()

#To view the saved profile
def view_profile():
    if not profile:
                print("Profile not found...Create a new one")
    else:
        print("========== Profile ==========")
        print("Name: ",profile["Name"])
        print("College: ",profile["College"])
        print("Semester: ",profile["Semester"])
        print("Branch: ",profile["Branch"])
        print("Daily Coding goal: ",profile["Daily Coding Goal"])
        print("=============================")

#To add progress 
def add_progress():
     if not profile:
                 print("No profile found...Create a new one")
     else:
        print("==========Add your achievement==========")
        date=input("DD-MM-YYYY: ")
        platform=input("Enter the Platform: ")
        topic=input("Enter the topics Studied: ")
        problems=int(input("Enter the number of problems solved: "))
        hours=int(input("Enter the number of hours: "))
     session={
            "Date":date,
            "Platform":platform,
            "Topic":topic,
            "Problems":problems,
            "Hours":hours
            }
     progress.append(session)
     print("Today's achievement is successfully saved")
     save_progress()

#To view the saved progress
def view_progress():
    if not progress:
                print("No Progress stored")
    else:
                print("==========Progress Report========")
                for session in progress:
                        print("Date: ",session["Date"])
                        print("Platform: ",session["Platform"])
                        print("Topic: ",session["Topic"])
                        print("Problems: ",session["Problems"])
                        print("Hours: ",session["Hours"])
                        print("---------------------------------")
    print("=================================")

#To view the dashboard                 
def dashboard():
        print("==========Dashboard===========")
        if not progress:
            print ("No progress")
        else:
              total_hours=0
              total_problems=0
              for session in progress:
                    total_hours+= session["Hours"]
                    total_problems+= session["Problems"]
        print("Total Study sessions: ", len(progress))
        print("Total no. of problems solved: ", total_problems)
        print("Total time spent: ", total_hours)
        print("=================================")

#To search a particular progress
def search_progress():
      print("Enter the date(DD-MM-YYYY): ")
      if not progress:
            print("No progress found")
      else:
           date=input("Enter the date (DD-MM-YYYY): ")
           flag=False
           for session in progress:
                 if date==session["Date"]:
                        print("Progress found")
                        print("Date: ",session["Date"])
                        print("Platform: ",session["Platform"])
                        print("Topic: ",session["Topic"])
                        print("Problems: ",session["Problems"])
                        print("Hours: ",session["Hours"])
                        flag=True

      if not flag:
                  print("No Session found in this date")
                                     

while True:
      print("\nChoose an option from the menu")
      print("1.Create profile")
      print("2.View Profile")
      print("3.Add Coding Progress")
      print("4.View Progress")
      print("5.Dashboard")
      print("6.Search Progress")
      print("7.Exit")

      try:
            n=int(input("Enter your choice: "))
      except ValueError:
                  print("Enter a number from 1 to 7")
                  print("=================================")
                  continue
      
      if n<1 or n>7:
                  print("Enter a number from 1 to 7")
                  print("=================================")
                  continue
           
      if n==1:
        create_profile()
    
      elif n==2:
         view_profile()
        
      elif n==3:
         add_progress()
        
      elif n==4:
          view_progress()
        
      elif n==5:
          dashboard()        

      elif n==6:
          search_progress()

      elif n==7:
          print("-------------------------------")
          print("Thank you for using CodeJourney")
          print("-------------------------------")
          break
    
      else:
        print("Invalid Choice")
    