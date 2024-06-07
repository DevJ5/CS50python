#!/usr/bin/env python3

import pandas as pd


def municipalities_of_finland():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    return df["Akaa":"Äänekoski"]


def main():
    print(municipalities_of_finland())


if __name__ == "__main__":
    main()
# "Region 2018"	"Population"	"Population change from the previous year, %"	"Share of Swedish-speakers of the population, %"	"Share of foreign citizens of the population, %"	"Proportion of the unemployed among the labour force, %"	"Proportion of pensioners of the population, %"
# "WHOLE COUNTRY"	5513130	0.2	5.2	4.5	13.5	25.3
# "Akaa"	16769	-0.9	0.2	1.6	14.6	26.1
