#!/usr/bin/env python3

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def mystery_data():
    # Step 1: Load the CSV file
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")

    # Step 2: Separate the independent variables (X) and the dependent variable (y)
    X = df.iloc[:, :-1]  # Assuming last column is the dependent variable
    y = df.iloc[:, -1]
    # x = df.loc[:, 'X1':'X5']
    # y = df.loc[:, 'Y']

    # Step 3: Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 4: Train the linear regression model
    model = LinearRegression(fit_intercept=False)
    model.fit(X_train, y_train)

    # Step 5: Evaluate the model
    y_pred = model.predict(X_test)

    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Mean Squared Error:", mse)
    print("R-squared:", r2)

    # Optional: Print coefficients
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)
    return model.coef_


def main():
    coefficients = mystery_data()
    # print the coefficients here
    for i, co in enumerate(coefficients):
        print(f"Coefficient of X{i+1} is {co}")


if __name__ == "__main__":
    main()
