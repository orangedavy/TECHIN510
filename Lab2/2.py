import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


faces = pd.read_csv('Labs/2_Data_Visualization/robot_faces.csv')
people = pd.read_csv('Labs/2_Data_Visualization/people.csv')
accel = pd.read_csv('Labs/2_Data_Visualization/accelerometer.csv')
print(people.shape)
mean_age = people['Age'].mean()
valid = people.groupby('City').size() > 3
people_val = people[people.apply(lambda row: valid[row['City']], axis=1)]

# people = people[people.apply(lambda row: sum(people.City == row['City']) > 3, axis = 1)]
print(people_val)
# 

# Q2

faces['year'] = faces['year'].astype('Int64')
after_15 = faces[faces['year'] >= 2015]
before_15 = faces[faces['year'] < 2015]
count_after_15 = after_15['category'].value_counts()
count_before_15 = before_15['category'].value_counts()
ranks = pd.DataFrame({
    'Category': count_after_15.index[:5],
    '2015 onward': count_after_15[:5],
    '2015 backward': count_before_15[:5]
})

ranks.plot(x='Category', y=['2015 onward', '2015 backward'], kind='barh', rot=0)

print(ranks)