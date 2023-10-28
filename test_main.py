from lib import load, summary, visualize

import pandas as pd

path = "titanic.csv"
original_data = pd.read_csv(path)

def test_load():
    result_load_data = load(path)
    assert original_data.equals(result_load_data), "Test has failed."

def test_summary():
    result_summary = summary(original_data)
    expected_age_mean = original_data["age"].mean()
    result_age_mean = result_summary.iloc[1,2]
    assert expected_age_mean == result_age_mean, "Test has failed."

def test_visualize():
    result_plot = visualize(original_data)
    assert result_plot is None, "Test has failed."


if __name__ == "__main__":
    test_load()
    test_summary()
    test_visualize()