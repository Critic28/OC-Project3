import pandas as pd
class DataCleaner:
    def __init__(self, data):
        self.data = data
    
    def remove_duplicates(self):
        self.data = self.data.drop_duplicates()
    
    def remove_missing_values(self):
        self.data = self.data.dropna()
    
    def convert_all_to_lowercase(self, column):
        self.data[column] = self.data[column].str.title()
    
    def convert_to_numeric(self, column):
        self.data[column] = pd.to_numeric(self.data[column], errors='coerce')
    
    def clean_data(self):
        self.remove_duplicates()
        self.remove_missing_values()
    
    def get_cleaned_data(self):
        return self.data
data = pd.read_csv('Electric_Vehicle_Population_data.csv')
cleaner = DataCleaner(data)
cleaner.clean_data()
cleaned_data = cleaner.get_cleaned_data()
cleaner.convert_all_to_lowercase('Make')
cleaner.convert_all_to_lowercase('Model')
cleaner.convert_all_to_lowercase('Electric Utility')
# Export cleaned data to a new CSV file
cleaned_data.to_csv('cleaned_data.csv', index=False)