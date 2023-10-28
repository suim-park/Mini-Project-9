from lib import load, summary, visualize

import pandas as pd

path = "titanic.csv"
original_data = pd.read_csv(path)

def test_load():
    result_load_data = load(path)
    assert original_data == result_load_data, "Test has failed."

def test_summary():
    result_summary = summary(original_data)
    expected_summary = pd.describe(original_data)
    assert result_summary == expected_summary, "Test has failed."

def test_visualize():
    result_plot = visualize(original_data)
    assert result_plot is not None, "Test has failed."


if __name__ == "__main__":
    data = test_load(path)
    test_summary(data)
    test_visualize(data)