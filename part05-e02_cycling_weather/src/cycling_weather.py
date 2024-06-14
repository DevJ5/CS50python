#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date(df):
    df = df["Päivämäärä"].str.split(expand=True)
    df.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
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


def split_date_continues():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how="all")
    df = df.dropna(axis=1, how="all")

    first_col = df.iloc[:, [0]]
    df_first_col = split_date(first_col)

    df = df.drop(df.columns[0], axis=1)
    df = pd.concat([df_first_col, df], axis=1)

    return df


def cycling_weather():
    df1 = split_date_continues()
    df2 = pd.read_csv("src/kumpula-weather-2017.csv")
    df = pd.merge(df1, df2, left_on=["Year","Day", "Month"], right_on=["Year","d","m"])
    df = df.drop(columns=["m","d","Time","Time zone"])
    return df


def main():
    print(cycling_weather())


if __name__ == "__main__":
    main()
