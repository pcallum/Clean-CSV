import csv

with open('imdb_data.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    empty_entries = 0
    for row in csv_reader:
        for entry in row:
            if entry == "":
                print("None" + ",", end=' ')
                empty_entries += 1
            else:
                print(entry + ",", end=' ')

        print("\n")

        line_count += 1
    print(str(line_count) + " lines.")
    print(str(empty_entries) + " empty entries.")
