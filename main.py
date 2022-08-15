import csv
import logging

logging.basicConfig(filename = 'imdb_csv_log.log',
                    level = logging.DEBUG,
                    format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')

with open('imdb_data.csv', 'r', encoding="utf8") as csv_file:
    logging.info("imdb_data.csv opened in reading mode.")

    csv_reader = csv.reader(csv_file, delimiter=',')
    clean_file = []
    clean_row = []
    empty_entries_in_file = 0
    for row in csv_reader:
        for entry in row:
            if entry == "":
                clean_row.append("None")
                empty_entries_in_file += 1
            else:
                clean_row.append(entry.rstrip())

        clean_file.append(clean_row)
        clean_row = []

    logging.warning(f"File has {empty_entries_in_file} empty entries.")

logging.info("imdb_data.csv closed.")

with open('imdb_data_clean.csv', 'w', encoding="utf8", newline='') as csv_file:
    logging.info("imdb_data_clean.csv opened.")
    # write clean file to a new file
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(clean_file)
logging.info("imdb_data_clean.csv closed.")