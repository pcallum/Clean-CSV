import csv
import logging

logging.basicConfig(filename='imdb_csv_log.log',
                    level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

deleted_rows = 0

with open('imdb_data.csv', 'r', encoding="utf8") as old_file, open('imdb_data_clean.csv', 'w', encoding="utf8",
                                                                   newline='') as new_file:
    logging.info("Script started.")

    csv_reader = csv.reader(old_file, delimiter=',')
    csv_writer = csv.writer(new_file)

    for row in csv_reader:
        if "" in row:
            deleted_rows += 1
        else:
            csv_writer.writerow([entry.rstrip() for entry in row])

    if deleted_rows > 0:
        logging.warning(f"Deleted {deleted_rows} rows with empty entries.")

    logging.info("Script finished.")
