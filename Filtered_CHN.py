import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filtered_data_chn_path = '/Users/apple/Downloads/filtered_data_CHN.xlsx'  
filtered_data_chn = pd.read_excel(filtered_data_chn_path)
filtered_data_chn.head()

gender_distribution_chn = filtered_data_chn['gender'].value_counts()
majority_status_distribution_chn = filtered_data_chn['majorityStatusAtExploit'].value_counts()
age_distribution_chn = filtered_data_chn['ageBroad'].value_counts()

fig, ax = plt.subplots(1, 3, figsize=(18, 6))

gender_distribution_chn.plot(kind='bar', ax=ax[0], color='skyblue')
ax[0].set_title('Gender Distribution of Trafficking Victims')
ax[0].set_xlabel('Gender')
ax[0].set_ylabel('Number of Cases')

majority_status_distribution_chn.plot(kind='bar', ax=ax[1], color='lightgreen')
ax[1].set_title('Majority Status at Exploit')
ax[1].set_xlabel('Majority Status')
ax[1].set_ylabel('Number of Cases')

age_distribution_chn.plot(kind='bar', ax=ax[2], color='salmon')
ax[2].set_title('Age Distribution of Trafficking Victims')
ax[2].set_xlabel('Age Group')
ax[2].set_ylabel('Number of Cases')
plt.tight_layout()
plt.show()


exploitation_types_columns = ['typeOfLabourAgriculture', 'typeOfLabourConstruction', 'typeOfLabourDomesticWork',
                              'typeOfLabourHospitality', 'typeOfLabourOther', 'typeOfSexProstitution', 
                              'typeOfSexPornography', 'typeOfSexOther']
exploitation_types_summary_chn = filtered_data_chn[exploitation_types_columns].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
exploitation_types_summary_chn.plot(kind='bar', color='purple')
plt.title('Distribution of Cases by Types of Exploitation')
plt.xlabel('Type of Exploitation')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)
plt.show()

means_of_control_columns = ['meansOfControlDebtBondage', 'meansOfControlTakesEarnings', 'meansOfControlThreats',
                            'meansOfControlPsychologicalAbuse', 'meansOfControlPhysicalAbuse', 'meansOfControlSexualAbuse',
                            'meansOfControlFalsePromises', 'meansOfControlPsychoactiveSubstances', 
                            'meansOfControlRestrictsMovement', 'meansOfControlRestrictsMedicalCare',
                            'meansOfControlExcessiveWorkingHours', 'meansOfControlThreatOfLawEnforce',
                            'meansOfControlWithholdsNecessities', 'meansOfControlWithholdsDocuments', 'meansOfControlOther']
means_of_control_summary_chn = filtered_data_chn[means_of_control_columns].sum().sort_values(ascending=False)

plt.figure(figsize=(14, 8))
means_of_control_summary_chn.plot(kind='bar', color='teal')
plt.title('Means of Control Used on Trafficking Victims')
plt.xlabel('Means of Control')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)
plt.show()

