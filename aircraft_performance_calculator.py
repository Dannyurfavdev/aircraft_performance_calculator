import csv

CSV_FILE = "results.csv"

# pre-defined values
defaults = {
    "fuel_capacity": 900,
    "fuel_consumption_rate": 50,
    "true_air_speed": 150,
    "payload": 5000,
    "fuel_weight": 6000,
    "moment_list": [10000, 2500],
    "total_weight": 1500,
    "cl": 1.5,
    "rho": 1.225,
    "v": 100,
    "s": 20,
    "cd": 0.02,
    "mass": 5000,
    "g": 9.81,
    "thrust": 6000,
    "drag": 5000,
    "velocity": 50,
    "accelaration": 2,
    "time": 10,
}

# Prompt user for input with default fallback
def get_input(prompt, default, is_list=False):
    user_input = input(f"{prompt} [default={default}]: ")
    if not user_input.strip():
        return default
    if is_list:
        try:
            return list(map(float, user_input.strip().split(",")))
        except:
            print("Invalid list format. Using default.")
            return default
    try:
        return float(user_input)
    except:
        print("Invalid input. Using default.")
        return default

# Calculation functions
def calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed):
    return (fuel_capacity / fuel_consumption_rate) * true_air_speed

def calculate_endurance(fuel_capacity, fuel_consumption_rate):
    return fuel_capacity / fuel_consumption_rate

def calculate_total_weight(payload, fuel_weight):
    return payload + fuel_weight

def calculate_cg_position(moment_list, total_weight):
    return sum(moment_list) / total_weight

def calculate_lift(cl, rho, v, s):
    return 0.5 * cl * rho * v**2 * s

def calculate_drag(cd, rho, v, s):
    return 0.5 * cd * rho * v**2 * s

def calculate_weight(mass, g):
    return mass * g

def calculate_accelaration(thrust, drag, weight, mass):
    return (thrust - drag - weight) / mass

def calculate_velocity(velocity, accelaration, time):
    return velocity + accelaration * time

def calculate_distance(velocity, time):
    return velocity * time

# Save to CSV
def save_to_csv(data):
    try:
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["Metric", "Value"])
            writer.writeheader()
            writer.writerows(data)
        print(f"\n✅ Data successfully saved to {CSV_FILE}")
    except Exception as e:
        print(f"❌ Error saving data to CSV: {e}")

# Main script logic
def main():
    print("🛩 Aircraft Performance Calculator\n")

    # Get user inputs or use defaults
    fuel_capacity = get_input("Enter fuel capacity (gallons)", defaults["fuel_capacity"])
    fuel_consumption_rate = get_input("Enter fuel consumption rate (gallons/hour)", defaults["fuel_consumption_rate"])
    true_air_speed = get_input("Enter true air speed (knots)", defaults["true_air_speed"])
    payload = get_input("Enter payload (pounds)", defaults["payload"])
    fuel_weight = get_input("Enter fuel weight (pounds)", defaults["fuel_weight"])
    moment_list = get_input("Enter moment list (comma-separated)", defaults["moment_list"], is_list=True)
    total_weight = get_input("Enter total weight (pounds)", defaults["total_weight"])
    cl = get_input("Enter lift coefficient", defaults["cl"])
    rho = get_input("Enter air density (kg/m^3)", defaults["rho"])
    v = get_input("Enter velocity (m/s)", defaults["v"])
    s = get_input("Enter wing area (m^2)", defaults["s"])
    cd = get_input("Enter drag coefficient", defaults["cd"])
    mass = get_input("Enter mass (kg)", defaults["mass"])
    g = get_input("Enter gravity (m/s^2)", defaults["g"])
    thrust = get_input("Enter thrust (N)", defaults["thrust"])
    drag = get_input("Enter drag (N)", defaults["drag"])
    velocity = get_input("Enter initial velocity (m/s)", defaults["velocity"])
    accelaration = get_input("Enter acceleration (m/s^2)", defaults["accelaration"])
    time = get_input("Enter time (seconds)", defaults["time"])

    # Perform calculations
    results = [
        {"Metric": "Range (miles)", "Value": calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed)},
        {"Metric": "Endurance (hours)", "Value": calculate_endurance(fuel_capacity, fuel_consumption_rate)},
        {"Metric": "Total Weight (pounds)", "Value": calculate_total_weight(payload, fuel_weight)},
        {"Metric": "CG Position (feet)", "Value": calculate_cg_position(moment_list, total_weight)},
        {"Metric": "Lift (N)", "Value": calculate_lift(cl, rho, v, s)},
        {"Metric": "Drag (N)", "Value": calculate_drag(cd, rho, v, s)},
        {"Metric": "Aircraft Weight (N)", "Value": calculate_weight(mass, g)},
        {"Metric": "Acceleration (m/s^2)", "Value": calculate_accelaration(thrust, drag, calculate_weight(mass, g), mass)},
        {"Metric": "Velocity after 10s (m/s)", "Value": calculate_velocity(velocity, accelaration, time)},
        {"Metric": "Distance in 10s (m)", "Value": calculate_distance(velocity, time)},
    ]

    # Save to CSV
    save_to_csv(results)

# Entry point
if __name__ == "__main__":
    main()
