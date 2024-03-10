import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_undoc_isr_path= '/Users/apple/Downloads/dataUNDOC_ISR.xlsx'  
data_undoc_isr = pd.read_excel(data_undoc_isr_path)

#Trend
data_undoc_isr['Year'] = pd.to_numeric(data_undoc_isr['Year'], errors='coerce')
data_undoc_isr['txtVALUE'] = pd.to_numeric(data_undoc_isr['txtVALUE'], errors='coerce')
data_undoc_isr.head()

#Distribution
convictions_isr = data_undoc_isr[data_undoc_isr['Indicator'] == 'Persons convicted'].groupby('Year')['txtVALUE'].sum().reset_index()
victims_isr = data_undoc_isr[data_undoc_isr['Indicator'] == 'Detected trafficking victims'].groupby('Year')['txtVALUE'].sum().reset_index()
fig, axes = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

sns.lineplot(data=convictions_isr, x='Year', y='txtVALUE', marker='o', ax=axes[0], color='blue')
axes[0].set_title('Trend of Human Trafficking Convictions Over Time in Israel')
axes[0].set_ylabel('Number of Convictions')

sns.lineplot(data=victims_isr, x='Year', y='txtVALUE', marker='o', ax=axes[1], color='red')
axes[1].set_title('Trend of Detected Trafficking Victims Over Time in Israel')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('Number of Detected Victims')
plt.tight_layout()
plt.show()