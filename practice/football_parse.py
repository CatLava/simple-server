# parsing a csv file

# test_football_v1.py
import pytest
import csv

@pytest.fixture
def mock_csv_data():
    return [
        "Team,Games,Wins,Losses,Draws,Goals For,Goals Against",
        "Liverpool FC, 38, 32, 3, 3, 85, 33",
        "Norwich City FC, 38, 5, 27, 6, 26, 75",
    ]

@pytest.fixture
def mock_csv_file(tmp_path, mock_csv_data):
    datafile = tmp_path / "football.csv"
    datafile.write_text("\n".join(mock_csv_data))
    return str(datafile)


with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:

        print(row)
        if line_count > 0:
            gd = int(row[5]) - int(row[6])
            print("Goal differential: ", gd)
        line_count += 1
