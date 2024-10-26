import pandas as pd
import matplotlib.pyplot as plt
# reads a csv file
df = pd.read_csv('csv_file/user_behavior_dataset.csv')
#filters the dataframe based on os, usage, age, and gender
filtered = df.filter(items=['Operating System', 'App Usage Time (min/day)', 'Age', 'Gender'])

# refilters based on operating system and a condition of age being less than 20
android_users_above_20 = filtered[(filtered["Operating System"] == 'Android') & (filtered['Age'] > 20)]

# groups the refiltered dataframe based on gender and adds up their usage time
usage_by_gender = android_users_above_20.groupby('Gender')['App Usage Time (min/day)'].sum()


android_users_below_20 = filtered[(filtered['Operating System'] == 'Android') & (filtered['Age'] <20)]

usage_by_gender2 = android_users_below_20.groupby('Gender')['App Usage Time (min/day)'].sum()

ios_users_above_20 = filtered[(filtered['Operating System'] == 'iOS') & (filtered['Age'] > 20)]
usage_by_gender3 = ios_users_above_20.groupby('Gender')['App Usage Time (min/day)'].sum()

ios_users_below_20 = filtered[(filtered['Operating System'] == 'iOS') & (filtered['Age'] < 20)]
usage_by_gender_4 = ios_users_below_20.groupby('Gender')['App Usage Time (min/day)'].sum()

# creates the rows and colums to plot the chart on
fig, axes =plt.subplots(2, 2)

usage_by_gender.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightpink'], ax=axes[0,0], title='Device Usage by Android Users above 20 based on Gender', ylabel='')


usage_by_gender2.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'lightcoral'], ax=axes[0,1], title='Device Usage by Android Users below 20 based on Gender', ylabel='')


usage_by_gender3.plot(kind='pie', autopct='%1.1f%%', startangle = 90, colors=['lightyellow', 'lightgrey'], ax=axes[1,0], title='Device Usage by iOS Users above 20 based on Gender', ylabel='')


usage_by_gender_4.plot(kind='pie', autopct='%1.1f%%', startangle = 90, colors=['orange', 'lime'], ax=axes[1,1], title='Device Usage by iOS Users below 20 based on Gender', ylabel='')



plt.tight_layout()
plt.show()
