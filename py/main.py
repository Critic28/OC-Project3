import pandas as pd
class DataCleaner:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
    def read_data(self):
        # Read the CSV file into a pandas DataFrame
        self.df = pd.read_csv(self.input_file)
    def remove_duplicates(self):
        # Remove duplicate rows
        self.df = self.df.drop_duplicates()
    def remove_missing_values(self):
        # Remove rows with missing values
        self.df = self.df.dropna()
    def convert_to_lowercase(self, column_name):
        # Convert string column to lowercase
        self.df[column_name] = self.df[column_name].str.lower()
    def remove_whitespaces(self, column_name):
        # Remove leading and trailing whitespaces from string column
        self.df[column_name] = self.df[column_name].str.strip()  
    def save_data(self):
        # Save the cleaned data to a new CSV file
        self.df.to_csv(self.output_file, index=False)
# Create an instance of the DataCleaner class
cleaner = DataCleaner('Electric_Vehicle_Population_data.csv', 'output.csv')
# Execute the data cleaning steps
cleaner.read_data()
cleaner.remove_duplicates()
cleaner.remove_missing_values()
cleaner.convert_to_lowercase('County')
cleaner.remove_whitespaces('County')
cleaner.save_data()
