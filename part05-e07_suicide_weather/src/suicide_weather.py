#!/usr/bin/env python3


import pandas as pd


def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv")
    df["Suicides_Per_Population"] = df["suicides_no"] / df["population"]
    mean_fraction = df.groupby("country")["Suicides_Per_Population"].mean()

    return mean_fraction


def suicide_weather():
    df_temperature = pd.read_html(
        "src/List_of_countries_by_average_yearly_temperature.html",
        header=0,
        index_col=0,
    )[0]

    series_temperature = df_temperature.iloc[:, 0]
    series_temperature = series_temperature.str.replace("\u2212","-").astype(float)
    series_suicide = suicide_fractions()
    spearman_corr = series_temperature.corr(series_suicide, method="spearman")

    # Merge the dataframe and the series together based on their index
    df_common = pd.merge(
        df_temperature, series_suicide, left_index=True, right_index=True
    )

    # Concat is not correct, because it does an outer join
    # common_series = pd.concat([series_temperature, series_suicide], axis=1)
    # print(len(common_series))

    return (
        len(series_suicide),
        len(series_temperature),
        df_common.shape[0],
        spearman_corr,
    )


def main():
    suicide_rows, temperature_rows, common_rows, correlation = suicide_weather()
    print(f"Suicide DataFrame has {suicide_rows} rows")
    print(f"Temperature DataFrame has {temperature_rows} rows")
    print(f"Common DataFrame has {common_rows} rows")
    print(f"Spearman correlation: {correlation}")
    return


if __name__ == "__main__":
    main()
