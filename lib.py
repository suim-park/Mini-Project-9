import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
def load(path):
    df = pd.read_csv(path)
    return df

# Summary the data
def summary(data):
    data_summary = data.describe()
    print(data_summary)
    return data_summary

# Visualize the data
def visualize(data):
    boxplot = sns.boxplot(data=data, x="class", y="age", hue="alive")
    plt.show()