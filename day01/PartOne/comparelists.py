#comparelists.py

import csv

def LoadTSV(path=str):
    with open(path, newline='') as csvfile:
        csv_file = list(csv.reader(csvfile))
        list1 = [int(row[0].split("   ")[0]) for row in csv_file]
        list2 = [int(row[0].split("   ")[1]) for row in csv_file]
    return list1, list2
        
def CompareLists(list1, list2):
    assert len(list1) == len(list2)
    diff_lists = []
    list1.sort()
    list2.sort()
    for value1, value2 in zip(list1, list2):
        diff = abs(value1 - value2)
        diff_lists.append(diff)
    print(sum(diff_lists))


if __name__ == "__main__":
    import comparelists as cl
    list1, list2 = cl.LoadTSV("./lists.csv")
    print(len(list1))
    print(len(list2))
    CompareLists(list1,list2)
