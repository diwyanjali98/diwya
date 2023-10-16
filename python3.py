def factorial(n):
    import csv

    # Function to read data from a CSV file
    def read_csv(filename):
        data = []
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data



    # Function to write processed data to a new CSV file
    def write_csv(filename, data):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    # Input and output file names
    input_file = "input.csv"
    output_file = "output.csv"

    # Read data from the input CSV file
    data = read_csv(input_file)

    # Process the data
    processed_data = process_data(data)
