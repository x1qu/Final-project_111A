import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path_undoc_new = '/Users/apple/Downloads/dataUNDOC_USA.xlsx'  
data_new = pd.read_excel(file_path_undoc_new)

#Trend
data_new['Year'] = pd.to_numeric(data_new['Year'], errors='coerce')
data_new['txtVALUE'] = pd.to_numeric(data_new['txtVALUE'], errors='coerce')
data_new.head()
#Distribution
convictions_over_time = data_new[data_new['Indicator'] == 'Persons convicted'].groupby('Year')['txtVALUE'].sum().reset_index()
victims_over_time = data_new[data_new['Indicator'] == 'Detected trafficking victims'].groupby('Year')['txtVALUE'].sum().reset_index()

fig, ax = plt.subplots(2, 1, figsize=(14, 14))

sns.lineplot(data=convictions_over_time, x='Year', y='txtVALUE', marker='o', ax=ax[0], color='blue')
ax[0].set_title('Trend of Human Trafficking Convictions Over Time in the USA')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Convictions')

sns.lineplot(data=victims_over_time, x='Year', y='txtVALUE', marker='o', ax=ax[1], color='red')
ax[1].set_title('Trend of Detected Trafficking Victims Over Time in the USA')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of Detected Victims')
plt.tight_layout()
plt.show()

convictions_stats = convictions_over_time['txtVALUE'].describe()
victims_stats = victims_over_time['txtVALUE'].describe()
convictions_stats, victims_stats

