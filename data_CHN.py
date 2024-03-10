import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_undoc_chn_path_new = '/Users/apple/Downloads/dataUNDOC_CHN.xlsx'  
data_undoc_chn_new = pd.read_excel(data_undoc_chn_path_new)

#Trend
data_undoc_chn_new['Year'] = pd.to_numeric(data_undoc_chn_new['Year'], errors='coerce')
data_undoc_chn_new['txtVALUE'] = pd.to_numeric(data_undoc_chn_new['txtVALUE'], errors='coerce')
data_undoc_chn_new.head()

#Distribution
data_undoc_chn_clean = data_undoc_chn_new.dropna(subset=['txtVALUE'])
convictions_chn = data_undoc_chn_clean[data_undoc_chn_clean['Indicator'] == 'Persons convicted'].groupby('Year')['txtVALUE'].sum().reset_index()
victims_chn = data_undoc_chn_clean[data_undoc_chn_clean['Indicator'] == 'Detected trafficking victims'].groupby('Year')['txtVALUE'].sum().reset_index()
fig, axes = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

sns.lineplot(data=convictions_chn, x='Year', y='txtVALUE', marker='o', ax=axes[0], color='blue')
axes[0].set_title('Trend of Human Trafficking Convictions Over Time in China')
axes[0].set_ylabel('Number of Convictions')


sns.lineplot(data=victims_chn, x='Year', y='txtVALUE', marker='o', ax=axes[1], color='red')
axes[1].set_title('Trend of Detected Trafficking Victims Over Time in China')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('Number of Detected Victims')
plt.tight_layout()
plt.show()

