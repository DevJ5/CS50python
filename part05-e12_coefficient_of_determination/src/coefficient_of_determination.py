#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')

    X = df.loc[:, 'X1':'X5']
    y = df.loc[:, 'Y']

    model = linear_model.LinearRegression(fit_intercept=True)

    model.fit(X, y)
    score = model.score(X, y)

    r2_scores = [score]
    for i in range(len(X.columns)):
        Xi = X.iloc[:, i].values.reshape(-1, 1)
        model.fit(Xi, y)
        r2_scores.append(model.score(Xi, y))

    return r2_scores

def main():
    r2_scores = coefficient_of_determination()
    print(f"R2-score with feature(s) X: {r2_scores[0]}")
    for i in range(1, len(r2_scores)):
        print(f"R2-score with feature(s) X{i}: {r2_scores[i]}")

if __name__ == "__main__":
    main()
