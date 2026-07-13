import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


class FitnessTracker:
    def __init__(self, data):
        self.__data = data

    def show_5_rows(self):
        print("The first 5 rows of data are below::-\n")
        print(self.__data.head())
        print("\nThe last 5 rows of data are below::-\n")
        print(self.__data.tail())

    def add_row(self):
        while True:
            try:
                name_act = input("Enter the name of activity : ")
                duration = int(input("Enter the duration of activity(minutes) : "))
                calories = int(input("Enter the calories : "))
            except ValueError:
                print("Enter proper input")
            else:
                self.log_activity(name_act, duration, calories)
                break

    def log_activity(self, activity_type, duration, calories):
        new_row = {
            "Date": dt.date.today().strftime("%Y-%m-%d"),
            "Activity Type": activity_type,
            "Duration (Minutes)": duration,
            "Calories Burned": calories,
        }
        self.__data.loc[len(self.__data)] = new_row
        self.__data.to_csv("fitness_activities.csv", index=False)
        print("Activity added successfully.")

    def calculate_metrics(self):
        pass

    def __del__(self):
        del self.__data
        print("Thank you for using Fitness Tracker.")
        print("Good Bye!!!")


def load_data():
    try:
        d = pd.read_csv("fitness_activities.csv")
        return d
    except FileNotFoundError:
        print("There in no such file make it proper")
        return None


def show_menu():
    print("\n--------------------------------")
    print("|--Welcome to Fitness Tracker--|")
    print("--------------------------------\n")
    print("Enter your choice::-")
    print("-------------------------")
    print(" 1. See 5 top and bottom rows")
    print(" 2. Add new row")
    print(" 3. Calories Analyser")
    print(" 4. Data Filtering")
    print(" 5. Data Visualization")
    print(" 6. Exit")
    print("-------------------------")
    return input("Enter you choice : ")


def main():
    data = load_data()
    if data is None:
        print("Please try again")
        return
    fitness_tracker = FitnessTracker(data)
    while True:
        choice = show_menu()
        match choice:
            case "1":
                fitness_tracker.show_5_rows()
            case "2":
                fitness_tracker.add_row()
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                del fitness_tracker
                return
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
