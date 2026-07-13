<h1 align="center">🏋️‍♂️ FITNESS TRACKER 🏃‍♀️</h1>

<h3 align="center">Your personal, no-nonsense workout logbook — right in the terminal 💻🔥</h3>

<p align="center">
Track it. Analyze it. Visualize it. Repeat. 🔁
</p>

---

<h2>📖 OVERVIEW</h2>

**Fitness Tracker** is a Python-powered command-line application that lets you log daily workouts, dig into your performance with real analytics, filter your history any way you like, and turn your numbers into eye-catching charts. 📊

Every activity — a run, a yoga session, a swim — gets stored with its **date, duration, and calories burned**, building a growing dataset of your fitness journey over time. 📅✨

Under the hood:
- 🐼 **Pandas** — stores and manipulates your activity data
- 🔢 **NumPy** — powers the number-crunching
- 🎨 **Matplotlib + Seaborn** — brings your data to life visually

---

<h2>🧭 MAIN MENU</h2>

When the app starts, this is what greets you:

```
--------------------------------
|--Welcome to Fitness Tracker--|
--------------------------------

Enter your choice::-
-------------------------
 1. See 5 top and bottom rows
 2. Add new row
 3. Calories Analyser
 4. Data Filtering
 5. Summary and other important
 6. Data Visualization
 7. Exit
-------------------------
Enter you choice :
```

Every feature below is one keystroke away. 🔑

---

<h2>1️⃣ 👀 VIEW TOP & BOTTOM ROWS</h2>

Get a quick snapshot of your **most recent and earliest** logged activities.

**🔡 Input:** `1`

**📤 Output:**
```
The first 5 rows of data are below::-

         Date Activity Type  Duration (Minutes)  Calories Burned
0  2026-03-01       Running                  30              300
1  2026-03-02          Yoga                  45              150
2  2026-03-03       Cycling                  60              450
3  2026-03-04      Swimming                  40              320
4  2026-03-05       Walking                  35              120

The last 5 rows of data are below::-

          Date Activity Type  Duration (Minutes)  Calories Burned
15  2026-03-16       Cycling                  55              410
16  2026-03-17          Yoga                  40              140
17  2026-03-18       Running                  28              280
18  2026-03-19      Swimming                  38              300
19  2026-03-20       Walking                  30              110
```

---

<h2>2️⃣ 📝 ADD NEW ACTIVITY</h2>

Log a fresh workout in seconds. Today's date is added automatically. 📆

**🔡 Sample Inputs:**
```
Enter the name of activity : Running
Enter the duration of activity(minutes) : 30
Enter the calories : 300
```

**📤 Output:**
```
Activity added successfully.
```

**⚠️ Invalid Input Example:**
```
Enter the name of activity : Running
Enter the duration of activity(minutes) : thirty
Enter proper input
```
*(The app loops back and asks again until valid numbers are entered.)*

---

<h2>3️⃣ 🔍 CALORIES ANALYSER</h2>

A fast summary of your overall performance.

**🔡 Input:** `3`

**📤 Output:**
```
The Total calories are :- 5430
The Average Duration are :- 39.25
The activity Frequency are :-
Running     6
Yoga        5
Cycling     4
Swimming    3
Walking     2
Name: Activity Type, dtype: int64
```

---

<h2>4️⃣ 🎯 DATA FILTERING</h2>

Slice your history exactly how you want it.

**🔡 Input:** `4`

**📤 Filter Menu Output:**
```
Simple Filtering
Choose a filter:
1. Activity Type
2. Duration (Minutes)
3. Calories Burned
4. Date
Enter your choice:
```

### 🏃 Filter by Activity Type
**Input:** `1` → `Running`
**Output:**
```
         Date Activity Type  Duration (Minutes)  Calories Burned
0  2026-03-01       Running                  30              300
5  2026-03-06       Running                  25              250
17 2026-03-18       Running                  28              280
```

### ⏳ Filter by Duration (Minutes)
**Input:** `2` → `40`
**Output:** All rows where duration is **40 minutes or more**.

### 🔥 Filter by Calories Burned
**Input:** `3` → `300`
**Output:** All rows where calories burned is **300 or more**.

### 📆 Filter by Date
**Input:** `4` → `2026-03-03`
**Output:**
```
         Date Activity Type  Duration (Minutes)  Calories Burned
2  2026-03-03       Cycling                  60              450
```

### ❌ No Matching Data
```
There is no data as per condition
```

---

<h2>5️⃣ 📑 SUMMARY REPORT</h2>

A complete health-check of your entire fitness dataset.

**🔡 Input:** `5`

**📤 Output:**
```
Fitness Report
--------------
Total activities: 20
Total unique activities: 5
Total duration: 785 minutes
Total calories burned: 5430
Average duration: 39.3 minutes
Average calories: 271.5
Average improvement: 4.87%
Data summary:
       Duration (Minutes)  Calories Burned
count            20.000000        20.000000
mean              39.250000       271.500000
std                9.812345        98.221100
min               25.000000       110.000000
25%               32.500000       200.000000
50%               38.000000       270.000000
75%               45.000000       320.000000
max               60.000000       450.000000
```

---

<h2>6️⃣ 🎨 DATA VISUALIZATION</h2>

Turn your raw numbers into stunning visuals — saved automatically as PNG files. 🖼️

**🔡 Input:** `6`

**📤 Chart Menu Output:**
```
Enter your choice::-
--------------------
 1. Bar chart
 2. Line Graph
 3. Pie Chart
 4. Heatmap
Enter your choice :
```

### 📊 Bar Chart — `1`
Shows **total duration by activity type**.
```
Graph saved as fitness_plot.png
```

### 📈 Line Graph — `2`
Shows **calories burned over time**, tracking your progress day by day.
```
Line graph saved as fitness_line.png
```

### 🥧 Pie Chart — `3`
Shows the **percentage share** of each activity type in your routine.
```
Pie chart saved as fitness_pie.png
```

### 🌡️ Heatmap — `4`
Shows the **correlation** between duration and calories burned.
```
Heatmap saved as fitness_heatmap.png
```

Each chart also **pops up on screen** immediately after saving. 🖥️✨

---

<h2>7️⃣ 👋 EXIT</h2>

**🔡 Input:** `7`

**📤 Output:**
```
Thank you for using Fitness Tracker.
Good Bye!!!
```

---

<h2>🚫 INVALID MENU CHOICE</h2>

If you type anything outside `1–7`:

**🔡 Input:** `9`

**📤 Output:**
```
Invalid choice
```

The menu simply reappears, ready for a valid selection. 🔄

---

<h2>📂 DATA FORMAT</h2>

Your history lives in `fitness_activities.csv`:

| 🏷️ Column | 📋 Description |
|---|---|
| `Date` | Date of the activity (`YYYY-MM-DD`) |
| `Activity Type` | Name of the workout (Running, Yoga, Cycling, etc.) |
| `Duration (Minutes)` | Length of the activity in minutes |
| `Calories Burned` | Calories burned during the activity |

---

<h2>🧾 QUICK REFERENCE — ALL INPUTS & OUTPUTS</h2>

| # | 🎬 Action | 🔡 Sample Input | 📤 Sample Output |
|---|---|---|---|
| 1 | View rows | `1` | First 5 & last 5 rows printed |
| 2 | Add activity | `Running`, `30`, `300` | `Activity added successfully.` |
| 3 | Analyse calories | `3` | Total calories, avg duration, frequency table |
| 4 | Filter by type | `1`, `Running` | Matching rows or "no data" message |
| 4 | Filter by duration | `2`, `40` | Rows with duration ≥ 40 |
| 4 | Filter by calories | `3`, `300` | Rows with calories ≥ 300 |
| 4 | Filter by date | `4`, `2026-03-03` | Rows matching that date |
| 5 | Summary report | `5` | Full stats + `describe()` table |
| 6 | Bar chart | `1` | `fitness_bar.png` saved + shown |
| 6 | Line graph | `2` | `fitness_line.png` saved + shown |
| 6 | Pie chart | `3` | `fitness_pie.png` saved + shown |
| 6 | Heatmap | `4` | `fitness_heatmap.png` saved + shown |
| 7 | Exit | `7` | Farewell message |
| — | Invalid choice | `9` | `Invalid choice` |
| — | Invalid text input | `thirty` (for a number field) | `Enter proper input` |

---

<h2>🛠️ TECH STACK</h2>

<p>
🐍 <b>Python</b> &nbsp;|&nbsp;
🐼 <b>Pandas</b> &nbsp;|&nbsp;
🔢 <b>NumPy</b> &nbsp;|&nbsp;
🎨 <b>Matplotlib</b> &nbsp;|&nbsp;
🌊 <b>Seaborn</b>
</p>

---

