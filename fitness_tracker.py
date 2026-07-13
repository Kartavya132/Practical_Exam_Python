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
                continue
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
        print(f"The Total calories are :- {self.__data['Calories Burned'].sum()}")
        print(f"The Average Duration are :- {self.__data['Duration (Minutes)'].mean()}")
        print("The activity Frequency are :-")
        print(self.__data["Activity Type"].value_counts())

    def filter_activities(self, condition):
        if condition[0] == "Activity Type":
            return self.__data[
                self.__data[condition[0]].str.lower() == condition[1].lower()
            ]
        elif condition[0] == "Date":
            return self.__data[self.__data[condition[0]] == condition[1]]
        elif condition[0] == "Duration (Minutes)":
            return self.__data[self.__data[condition[0]] >= int(condition[1])]
        elif condition[0] == "Calories Burned":
            return self.__data[self.__data[condition[0]] >= int(condition[1])]
        else:
            print("Invalid column")
            return None

    def filteration(self):
        print("\nSimple Filtering")
        print("Choose a filter:")
        print("1. Activity Type")
        print("2. Duration (Minutes)")
        print("3. Calories Burned")
        print("4. Date")

        choice = int(input("Enter your choice: "))
        columns = ["Activity Type", "Duration(Minutes)", "Calories Burned", "Date"]

        if columns[choice - 1] in self.__data.columns:
            column = self.__data.columns[choice]
            value = input(f"Enter the value for {column}: ")
            condition = [column, value]

            result = self.filter_activities(condition)
            if result is not None:
                print(result)
            else:
                print("There is no data as per condition")
        else:
            print("Invalid Choice")

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
    print(" 5. Summary and other important")
    print(" 6. Data Visualization")
    print(" 7. Exit")
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
                fitness_tracker.calculate_metrics()
            case "4":
                fitness_tracker.filteration()
            case "5":
                pass
            case "6":
                pass
            case "7":
                del fitness_tracker
                return
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
