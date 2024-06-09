#!/usr/bin/env python3

import pandas as pd
import numpy as np

# President	Start	Last	Seasons	Vice-president
# "Donald Trump"	"2017 Jan"	-	1	"Mike pence"
# "Barack Obama"	2009	2017	2	"joe Biden"
# "Bush, George"	2001	2009	2	"Cheney, dick"
# "Clinton, Bill"	1993	2001	two	"gore, Al"


def cleaning_data():
    df = pd.read_csv("src/presidents.tsv", sep="\t")
    # Can use 2 splits or for loop to loop through the 2 elements
    df["President"] = df["President"].apply(
        lambda x: f"{x.split(', ')[1]} {x.split(', ')[0]}" if ", " in x else x
    )

    # Run the apply method on each element in the series
    df["Start"] = (
        df["Start"]
        .apply(lambda x: x.split()[0] if isinstance(x, str) else x)
        .astype(int)
    )

    # Replace non-integer values in column 'Last' with NaN
    df["Last"] = pd.to_numeric(df["Last"], errors="coerce").astype(float)
    # Regex is slower, but allows for more complex replacements
    # df['A'] = df['A'].replace(to_replace=r'[^0-9]', value=np.nan, regex=True)

    # Have a dictionary do the work for custom translations (word2number library also an option)
    seasons_translations = {"two": 2}
    df["Seasons"] = df["Seasons"].replace(seasons_translations).astype(int)

    # Run the apply method on each element in the series
    df["Vice-president"] = df["Vice-president"].apply(
        lambda name: (
            " ".join(word.title() for word in reversed(name.split(", ")))
            if ", " in name
            else name.title()
        )
    )
    return df


def main():
    cleaning_data()


if __name__ == "__main__":
    main()
