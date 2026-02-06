# Import Libraries
import pandas as pd
import numpy as np
import statistics as stats

data = pd.read_csv("Titanic Dataset.csv")
print(data.head())

"""####**Median Value of Age and Fare**"""
median_age = np.median(data['Age'])
print("Median value of Age -", median_age)

median_fare = np.median(data['Fare'])
print("Median value of Fare -", median_fare)

"""####**Mode Value of Age and Pclass**"""
mode_age = stats.mode(data['Age'])
print("Mode value of Age -", mode_age)

mode_pclass = stats.mode(data['Pclass'])
print("Mode value of Pclass -", mode_pclass)

"""####**Mode Value of Categorical Feature - Gender**"""
mode_gender = data['Gender'].value_counts().index[0]
print("Mode of Feature Gender -", mode_gender)