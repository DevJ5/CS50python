#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def split_date_continues():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    # Drop empty rows, drop empty columns (there is one at the end)
    df = df.dropna(how="all")
    df = df.dropna(axis=1, how="all")

    # Seperate the first column and drop it from the df
    col = df.iloc[:, 0]
    df = df.drop(df.columns[0], axis=1)

    # Split the first column into seperate columns
    col = col.str.split(expand=True)
    col.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    col["Hour"] = col["Hour"].str[0:2]

    weekdays = {
        "ma": "Mon",
        "ti": "Tue",
        "ke": "Wed",
        "to": "Thu",
        "pe": "Fri",
        "la": "Sat",
        "su": "Sun",
    }

    months = {
        "tammi": 1,
        "helmi": 2,
        "maalis": 3,
        "huhti": 4,
        "touko": 5,
        "kesä": 6,
        "heinä": 7,
        "elo": 8,
        "syys": 9,
        "loka": 10,
        "marras": 11,
        "joulu": 12,
    }

    # .map can take a dictionary
    col["Weekday"] = col["Weekday"].map(weekdays)
    col["Month"] = col["Month"].map(months)
    # .astype can take a dictionary as well
    col = col.astype(
        {"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int}
    )

    # Concatenate the columns together
    res = pd.concat([col, df], axis=1)

    return res

def cyclists_per_day():
    df = split_date_continues()
    df = df.drop(["Hour", "Weekday"], axis=1)
    grouped_df = df.groupby(["Year", "Month", "Day"]).sum()
    return grouped_df

def main():
    df = cyclists_per_day()
    rows = df.loc[(2017, 8)]
    # Plot using matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(rows)
    # Adding labels and title
    plt.xlabel("Day")
    plt.ylabel("Total")
    plt.title("All data")
    plt.legend()
    # Displaying the plot
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
