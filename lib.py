import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
def load(path):
    df = pd.read_csv(path, sep=",")
    return df

# Summary the data
def summary(data):
    data_summary = pd.describe(data)
    return data_summary

# Visualize the data
def visualize(data):
    boxplot = sns.boxplot(data=titanic, x="class", y="age", hue="alive")
    return boxplot