import pandas as pd

def clean_data():
    df = pd.read_csv("data/Laptop.csv")

    df.drop_duplicates(inplace=True)

    df["value_score"] = df["Ratings"] / df["Price"]

    df_sorted = df.sort_values(by="value_score", ascending=False)

    df_sorted.to_csv("data/cleaned_laptop.csv", index=False)
    df_sorted.to_excel("data/cleaned_laptop.xlsx", index=False)

    print("Cleaned data saved!")
    return df_sorted
