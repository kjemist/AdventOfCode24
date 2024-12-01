import csv
import pandas as pd
import os

def LoadCSV(path=str):
    with open(path, newline='') as csvfile:
        csv_file = list(csv.reader(csvfile))
        list1 = [int(row[0].split("   ")[0]) for row in csv_file]
        list2 = [int(row[0].split("   ")[1]) for row in csv_file]
    return list1, list2

if __name__ == "__main__":
    print(os.getcwd())
    list1,list2 = LoadCSV("./lists.csv")
    lists_df = pd.DataFrame(
        {
            "list1":list1,
            "list2":list2
        }
    )

    counts = lists_df["list2"].value_counts().to_dict()

    similarity_list = []
    for idx, row in lists_df.iterrows():
        value1 = row["list1"]
        if value1 in counts.keys():
            print("Found instance")
            print(value1)
            similarity_list.append(value1 * counts[value1])
    print(sum(similarity_list))



