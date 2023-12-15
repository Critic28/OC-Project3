import pandas as pd
class DataCleaner:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
    def read_data(self):
        self.df = pd.read_csv(self.input_file)
    def remove_duplicates(self):
        self.df = self.df.drop_duplicates()
    def remove_missing_values(self):
        self.df = self.df.dropna()
    def convert_to_lowercase(self, column_name):
        self.df[column_name] = self.df[column_name].str.lower()
    def remove_whitespaces(self, column_name):
        self.df[column_name] = self.df[column_name].str.strip()  
    def save_data(self):
        self.df.to_csv(self.output_file, index=False)
cleaner = DataCleaner('Electric_Vehicle_Population_data.csv', 'output.csv')
cleaner.read_data()
cleaner.remove_duplicates()
cleaner.remove_missing_values()
cleaner.convert_to_lowercase('County')
cleaner.remove_whitespaces('County')
cleaner.save_data()
