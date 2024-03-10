import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filtered_data_path = '/Users/apple/Downloads/filtered_data_USA.xlsx'  
filtered_data = pd.read_excel(filtered_data_path)

#Trend
filtered_data['Year'] = pd.to_numeric(filtered_data['Year'], errors='coerce')
filtered_data['txtVALUE'] = pd.to_numeric(filtered_data['txtVALUE'], errors='coerce')
filtered_data.columns, filtered_data.head()



