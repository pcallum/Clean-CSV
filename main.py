import csv

with open('imdb_data.csv', 'r', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    clean_file = []

    for row in csv_reader:
        # appends the cleaned row with empty entries replaced and whitespace stripped to a clean file
        clean_file.append([("None" if (x == "") else x.rstrip()) for x in row])


with open('imdb_data_clean.csv', 'w', encoding="utf8") as csv_file:
    # write clean file to a new file
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(clean_file)
