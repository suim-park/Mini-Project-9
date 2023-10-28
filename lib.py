import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
def load(path):
    df = pd.read_csv(path)
    return df

# Summary the data
def summary(path):
    data = load(path)
    data_summary = data.describe()
    print(data_summary)
    return data_summary

# Visualize the data
def visualize(path):
    data = load(path)

    folder_name = "Graphs"
    save_folder = os.path.join(folder_name)

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    boxplot = sns.boxplot(data=data, x="class", y="age", hue="alive", order=["First", "Second", "Third"])

    save_path = os.path.join(save_folder, f"boxplot class.png")
    plt.savefig(save_path)

    plt.show()