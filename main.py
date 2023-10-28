from lib import load, summary, visualize

data_path = "titanic.csv"

if __name__ == "__main__":
    data = load(data_path)
    summary(data)
    visualize(data)