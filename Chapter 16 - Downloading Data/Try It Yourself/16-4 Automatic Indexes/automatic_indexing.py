import csv
import matplotlib.pyplot as plt
from datetime import datetime



filename = 'data/death_valley_2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'
place_name = ''

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print(header_row)


    # Get dates, and rainfall amounts from this file.
    dates, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        prcp = float(row[3])
        prcps.append(prcp)

    # Plot the rainfall amounts.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, prcps, c='red', alpha=0.6)
    plt.fill_between(dates, prcps, facecolor='blue', alpha=0.1)

    # Format plot.
    plt.title("Sitka Rainfall, - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Daily rainfall amounts', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

