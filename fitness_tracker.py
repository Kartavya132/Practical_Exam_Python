import matplotlib

try:
    import tkinter  # noqa: F401

    matplotlib.use("TkAgg")
except Exception:
    matplotlib.use("Agg")

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

    def generate_report(self):

        durations = np.array(self.__data["Duration (Minutes)"], dtype=float)
        calories = np.array(self.__data["Calories Burned"], dtype=float)

        print("\nFitness Report")
        print("--------------")
        print(f"Total activities: {len(self.__data)}")
        print(f"Total unique activities: {self.__data['Activity Type'].nunique()}")
        print(f"Total duration: {np.sum(durations):.0f} minutes")
        print(f"Total calories burned: {np.sum(calories):.0f}")
        print(f"Average duration: {np.mean(durations):.1f} minutes")
        print(f"Average calories: {np.mean(calories):.1f}")

        if len(calories) > 1:
            changes = ((calories[1:] - calories[:-1]) / calories[:-1]) * 100
            print(f"Average improvement: {changes.mean():.2f}%")

        print(f"Data summary:\n{self.__data.describe()}")

    def visualization(self):
        print("Enter your choice::-")
        print("--------------------")
        print(" 1. Bar chart")
        print(" 2. Line Graph")
        print(" 3. Pie Chart")
        print(" 4. Heatmap")
        ch = input("Enter your choice : ")
        sns.set_theme(style="whitegrid")
        match ch:
            case "1":
                plt.figure(figsize=(10, 8), dpi=120)
                sns.barplot(
                    data=self.__data,
                    x="Activity Type",
                    y="Duration (Minutes)",
                    hue="Activity Type",
                )
                plt.title("Total Duration by Activity", fontsize=14)
                plt.xlabel("Activity", fontsize=12)
                plt.ylabel("Duration", fontsize=12)
                plt.xticks(rotation=90)
                plt.tight_layout()
                plt.savefig("plot\\fitness_bar.png")
                print("Graph saved as fitness_plot.png")
                plt.show()
            case "2":
                plt.figure(figsize=(10, 8), dpi=120)
                sns.lineplot(
                    data=self.__data,
                    x="Date",
                    y="Calories Burned",
                    marker="o",
                    linewidth=2,
                )
                plt.title("Calories Burned Over Time", fontsize=14)
                plt.xlabel("Date", fontsize=12)
                plt.ylabel("Calories Burned", fontsize=12)
                plt.xticks(rotation=90)
                plt.tight_layout()
                plt.savefig(
                    "plot\\fitness_line.png",
                )
                print("Line graph saved as fitness_line.png")
                plt.show()
            case "3":
                activity_counts = self.__data["Activity Type"].value_counts()
                plt.figure(figsize=(8, 8))
                plt.pie(
                    activity_counts.values.tolist(),
                    labels=activity_counts.index.tolist(),
                    autopct="%1.1f%%",
                    startangle=90,
                    wedgeprops={"linewidth": 1},
                )
                plt.title("Activity Share by Percentage", fontsize=14)
                plt.axis("equal")
                plt.tight_layout()
                plt.savefig("plot\\fitness_pie.png")
                print("Pie chart saved as fitness_pie.png")
                plt.show()
            case "4":
                numeric_data = self.__data[
                    ["Duration (Minutes)", "Calories Burned"]
                ].corr()
                plt.figure(figsize=(8, 8))
                sns.heatmap(numeric_data, annot=True, cmap="coolwarm", fmt=".2f")
                plt.title("Correlation Heatmap", fontsize=14)
                plt.tight_layout()
                plt.savefig("plot\\fitness_heatmap.png")
                print("Heatmap saved as fitness_heatmap.png")
                plt.show()

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
                fitness_tracker.generate_report()
            case "6":
                fitness_tracker.visualization()
            case "7":
                del fitness_tracker
                return
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
