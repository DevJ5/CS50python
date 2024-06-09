#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    # Drop empty rows
    df = df.dropna(how="all")
    # Drop empty columns
    df = df.dropna(axis=1, how="all")
    # Split the first column and append them at the end
    df[["Weekday", "Day", "Month", "Year", "Hour"]] = df["Päivämäärä"].str.split(
        expand=True
    )
    # Slice the first two digits of hourstring
    df["Hour"] = df["Hour"].str[0:2]
    # Take only the columns we need
    df = df[["Weekday", "Day", "Month", "Year", "Hour"]]

    # Dictionary for weekdays
    translations_weekday = {
        "ma": "Mon",
        "ti": "Tue",
        "ke": "Wed",
        "to": "Thu",
        "pe": "Fri",
        "la": "Sat",
        "su": "Sun",
    }

    # Dictionary for months
    translations_months = {
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
    # Map the translations
    df["Weekday"] = df["Weekday"].map(translations_weekday)
    # Any value that isnt found will be an empty string, convert it to None
    df["Weekday"] = df["Weekday"].replace("", np.nan)
    df["Month"] = df["Month"].map(translations_months)
    df["Month"] = df["Month"].replace("", np.nan)
    # Convert all the columns except the first one (Weekday) to integers
    df[df.columns[1:]] = df[df.columns[1:]].astype("int64")

    return df


def main():
    print(split_date())


if __name__ == "__main__":
    main()
