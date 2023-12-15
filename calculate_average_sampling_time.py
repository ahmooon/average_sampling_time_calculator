def calculate_average_sampling_time(data_points):
    if len(data_points) < 2:
        print("At least two data points are required to calculate sampling time.")
        return

    # Calculate time intervals
    time_intervals = [data_points[i] - data_points[i - 1] for i in range(1, len(data_points))]

    # Calculate average sampling time
    average_sampling_time = sum(time_intervals) / len(time_intervals)

    return average_sampling_time

def read_data_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data_points = [float(line.split()[0]) for line in file.readlines()]
            return data_points
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

# Specify the path to your data file in the Downloads folder
file_path = '/Users/hojinmoon/Downloads/data0_5hz25mm.txt'

# Read data from the file
data_points = read_data_from_file(file_path)

# If data was successfully read, calculate and print the average sampling time
if data_points is not None:
    result = calculate_average_sampling_time(data_points)
    print(f"Average Sampling Time: {result} units")


