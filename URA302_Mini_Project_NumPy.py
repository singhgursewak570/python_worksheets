
# URA302 Mini Project: NumPy Basics
# Sensor Data Analysis & Robot Path Analysis
# Dr. Rohit Kumar Singla – Thapar Institute of Engineering and Technology

import numpy as np

# -----------------------------
# PROJECT 1: SENSOR DATA
# -----------------------------
# CSV format assumed:
# time, temperature, distance, battery

sensor_file = "sensor_data.csv"

sensor_data = np.genfromtxt(sensor_file, delimiter=',', skip_header=1)

time = sensor_data[:, 0]
temperature = sensor_data[:, 1]
distance = sensor_data[:, 2]
battery = sensor_data[:, 3]

results_sensor = []
results_sensor.append(f"Average Temperature: {np.mean(temperature)}")
results_sensor.append(f"Min Temperature: {np.min(temperature)}")
results_sensor.append(f"Max Temperature: {np.max(temperature)}")

results_sensor.append(f"Average Distance: {np.mean(distance)}")
results_sensor.append(f"Min Distance: {np.min(distance)}")
results_sensor.append(f"Max Distance: {np.max(distance)}")

results_sensor.append(f"Average Battery: {np.mean(battery)}")
results_sensor.append(f"Min Battery: {np.min(battery)}")
results_sensor.append(f"Max Battery: {np.max(battery)}")

max_temp_time = time[np.argmax(temperature)]
results_sensor.append(f"Time of Highest Temperature: {max_temp_time}")

battery_below_30 = np.sum(battery < 30)
results_sensor.append(f"Battery below 30% count: {battery_below_30}")

with open("sensor_results.txt", "w") as f:
    for r in results_sensor:
        f.write(r + "\n")

print("Sensor Data Analysis Completed.")
print("\n".join(results_sensor))


# -----------------------------
# PROJECT 2: ROBOT PATH DATA
# -----------------------------
# CSV format assumed:
# x, y

robot_file = "robot_path.csv"

path = np.genfromtxt(robot_file, delimiter=',', skip_header=1)

x = path[:, 0]
y = path[:, 1]

# Total distance travelled
distances = np.sqrt(np.diff(x)**2 + np.diff(y)**2)
total_distance = np.sum(distances)

# Farthest point from origin
origin_distances = np.sqrt(x**2 + y**2)
farthest_index = np.argmax(origin_distances)
farthest_point = (x[farthest_index], y[farthest_index])

# Check revisits
visited = set()
revisited = False
for point in zip(x, y):
    if point in visited:
        revisited = True
        break
    visited.add(point)

results_robot = []
results_robot.append(f"Total Distance Travelled: {total_distance}")
results_robot.append(f"Farthest Point from Origin: {farthest_point}")
results_robot.append(f"Robot Revisited Same Position: {revisited}")

with open("robot_path_results.txt", "w") as f:
    for r in results_robot:
        f.write(r + "\n")

print("\nRobot Path Analysis Completed.")
print("\n".join(results_robot))
