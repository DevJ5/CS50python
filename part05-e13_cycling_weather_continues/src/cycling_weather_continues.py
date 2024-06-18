#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def read_weather_data():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how="all")
    df = df.dropna(axis=1, how="all")
    split_column = df["Päivämäärä"].str.split("\s", expand=True)
    df[["Weekday", "Day", "Month", "Year", "Hour"]] = split_column
    df["Hour"] = df["Hour"].str[0:2]
    df.drop("Päivämäärä", axis=1, inplace=True)
    new_column_order = ["Weekday", "Day", "Month", "Year", "Hour"] + [
        col
        for col in df.columns
        if col not in ["Weekday", "Day", "Month", "Year", "Hour"]
    ]
    df = df[new_column_order]

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

    df["Weekday"] = df["Weekday"].replace(weekdays)
    df["Month"] = df["Month"].replace(months)
    df = df.astype(
        {"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int}
    )
    return df


def cycling_weather_continues(station):
    df1 = read_weather_data()
    selected_columns = df1.columns[:5].tolist() + [station]
    df1 = df1[selected_columns]
    df1 = df1[df1["Year"] == 2017]
    df1 = df1.groupby(["Month", "Day"])[station].sum().reset_index()
    df2 = pd.read_csv("src/kumpula-weather-2017.csv")
    df = pd.merge(df1, df2, left_on=["Month", "Day"], right_on=["m", "d"])
    df = df.drop(columns=["Year", "Time", "Time zone","m","d"])
    df = df.ffill()
    nan_columns = df.columns[df.isna().any()].tolist()
    print(nan_columns)
    # Splitting into X and y
    X = df.iloc[:, -3:]  # Features
    y = df[station]  # Target variable
    model = LinearRegression(fit_intercept=True)
    model.fit(X, y)
    score = model.score(X, y)
    return model.coef_, score


def main():
    station = "Baana"
    coef, score = cycling_weather_continues(station)
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {coef[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]:.1f}")
    print(f"Score: {score:.2f}")

if __name__ == "__main__":
    main()
