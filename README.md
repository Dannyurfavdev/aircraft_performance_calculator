#  Simulated Aircraft Performance Calculator

A Python script for calculating aircraft performance metrics such as range, endurance, lift, drag, center of gravity (CG), acceleration, and more.

It supports **user input via terminal**, with sensible **default values preloaded**, and exports results to a `results.csv` file.

---

# Features

- Calculate:
  - Range (miles)
  - Endurance (hours)
  - Total Weight
  - Center of Gravity (CG)
  - Lift and Drag (N)
  - Aircraft Weight (N)
  - Acceleration
  - Final velocity and distance traveled over time
- CSV export for easy sharing and analysis
- User-friendly command-line input with default fallbacks
- Modular and well-structured code
- `if __name__ == "__main__"` structure for reusability

---

# 🛠 Technologies Used

- Python 3
- Built-in libraries: `csv`

---

# Getting Started

# 1. Clone the Repository

```bash
git clone https://github.com/Dannyurfavdev/aircraft_performance_calculator.git
cd aircraft_performance_calculator
2. Run the Script
Make sure you have Python installed (Python 3.x recommended).

python or python3 aircraft_performance_calculator.py
You’ll be prompted to input values like fuel capacity, airspeed, lift coefficient, etc. Press Enter to use the default values shown.

📥 Sample Input & Output

Sample Prompt:

Enter fuel capacity (gallons) [default=900]:
Enter fuel consumption rate (gallons/hour) [default=50]: 55
Enter moment list (comma-separated) [default=[10000, 2500]]: 12000,3000

Sample Output in results.csv:

Metric	Value
Range (miles)	2454.55
Endurance (hours)	16.36
Total Weight (pounds)	11000
CG Position (feet)	10.0
Lift (N)	183750.0
Drag (N)	2450.0
Aircraft Weight (N)	49050.0
Acceleration (m/s^2)	0.31
Velocity after 10s (m/s)	70.0
Distance in 10s (m)	500.0


# File Structure

# aircraft_performance_calculator
# calculator.py         # Main script
# results.csv           # Output file after script runs
# README.md             # Project documentation


# Contribution

#Contributions are welcome! Please open an issue or submit a pull request for improvements, bug fixes, or new features.