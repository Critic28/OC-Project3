"""Imports pandas."""
import pandas as pd


class DataCleaner:
    """Defines the class."""

    def __init__(self, data):
        """Defines data."""
        self.data = data

    def remove_duplicates(self):
        """Removes duplicate rows."""
        self.data = self.data.drop_duplicates()

    def remove_missing_values(self):
        """Removes missing values."""
        self.data = self.data.dropna()

    def convert_to_lowercase(self, column):
        """Converts values to title."""
        self.data[column] = self.data[column].str.title()

    def clean_data(self):
        """Cleans the data."""
        self.remove_duplicates()
        self.remove_missing_values()

    def get_cleaned_data(self):
        """Gets the cleaned data."""
        return self.data


data = pd.read_csv('Electric_Vehicle_Population_data.csv')
cleaner = DataCleaner(data)
cleaner.clean_data()
cleaned_data = cleaner.get_cleaned_data()
cleaner.convert_to_lowercase('Make')
cleaner.convert_to_lowercase('Model')
cleaner.convert_to_lowercase('Electric Utility')
compression_opts = dict(method='zip',
                        archive_name='cleaned_data.csv')
cleaned_data.to_csv('cleaned_data.zip', compression=compression_opts)
