#app.py

#Welcome Message
print("Welcome to my Python program!")

#User input prompt
def get_study_hours():
    hours = input("How many hours did you study today?")
    return hours

#Calculate weekly study hours
def calculate_weekly_hours(hours_input):
    return hours_input * 7

def main():
    try:
        #Receive user input
        hours_input = get_study_hours()
        #Convert user input to float
        hours = float(hours_input)
        weekly_hours = calculate_weekly_hours(hours)
        #Display results
        print(f"\nYou studied {hours:.2f} hours today.") 
        print(f"You are on track to study {weekly_hours} hours this week.")
    except ValueError:
        print("Please enter valid number.")
        exit()

#Run the function
if __name__ == "__main__":
    main()
