import csv

#pre-defined variable values
fuel_capacity= 900 #gallons
fuel_consumption_rate= 50 # gallons per hour
true_air_speed= 150 #knots
payload= 5000 #pounds
fuel_weight= 6000 #pounds
moment_list = [10000, 2500] # pound-feet
total_weight= 1500 #pounds
cl= 1.5 # lift coefficent 
rho= 1.225 # air density in kg/m^3
v= 100 # velocity in m/s
s= 20 # wing area in m^2
cd= 0.02 # drag coefficent
mass= 5000 # mass in kg
g = 9.81 # accelaration due to gravity in m/s^2
thrust= 6000 #thrust in N
drag = 5000 #drag in N
velocity= 50 #initial velocity in m/s
accelaration= 2 # accelaration in m/s^2
time = 10 # time in seconds

csv_file= 'results.csv'

# Performance calculation code 

def calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed):
    range_in_hours = fuel_capacity/fuel_consumption_rate
    range_in_miles= range_in_hours * true_air_speed
    return range_in_miles

def calculate_endurance(fuel_capacity, fuel_consumption_rate):
    endurance_in_hours= fuel_capacity/ fuel_consumption_rate
    return endurance_in_hours

def calculate_total_weight(payload, fuel_weight):
    return payload + fuel_weight
    
def calculate_cg_position(moment_list, total_weight):
    total_moment= sum(moment_list)
    return total_moment/total_weight
    
def calculate_moment(weight, arm):
    return weight * arm
    
def calculate_lift(cl, rho, v, s):
    return 0.5 * cl * rho * v**2 * s
    
def calculate_drag(cd, rho, v, s):
    return 0.5 * cd * rho * v**2 * s
    
def calculate_weight(mass, g):
    return mass * g
    
def calculate_accelaration(thrust, drag, weight, mass):
    return (thrust - drag - weight)/mass
    
def calculate_velocity(velocity, accelaration, time):
    return velocity + accelaration * time
    
def calculate_distance(velocity, time):
    return velocity * time 

results = []

def save_to_csv(products):
    """
        Save results to a CSV
    """
    try:
        with open (CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer= csv.DictWriter(file, fieldnames = ["results"])
            writer.writeheader()
            writer.writerows(products)
            print(f"Data successfully saved to {CSV_FILE}")
    except Exception as e:
        print(f"Error saving data to csv: {e}")
