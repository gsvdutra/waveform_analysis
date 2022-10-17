import pandas as pd
from typing import List
import numpy as np

class CsvParser:

    def set_current_csv_file(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def load_valid_data_from_columns(self, columns: List[int]):
        self.df = self.df.iloc[:, columns]
        self.df = self.df[~self.df.isin([np.nan, np.inf, -np.inf]).any(1)]

    def remove_mean_from_data(self,reference_column: int):

        columns_to_filter = [
            index for index in
            list(range(0,len(self.df.columns)))
        ]
        columns_to_filter.pop(reference_column)
        columns_label = [self.df.columns[index] for index in columns_to_filter]

        mean_data = self.df[columns_label].mean()

        for label, mean in zip(columns_label, mean_data):
            self.df.loc[:, label] = self.df[label].apply(lambda x: x - mean)


    def remove_data_bellow_threshold(self, upper_threshold, lower_threshold, column):
        
        column_label = self.df.columns[column]
        data_mean = self.df[column_label].mean()

        self.df = self.df.loc[
            (self.df[column_label] <= data_mean + lower_threshold) | 
            (self.df[column_label] >= data_mean + upper_threshold)
            ]