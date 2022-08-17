import csv
import logging
import os
import sys

logging.basicConfig(filename='clean_csv.log',
                    level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')


def clean(row):
    return [entry.rstrip() for entry in row]


def main(path):
    # open file to clean, create or open a new file with the same filename + "_clean" to write too
    with open(path, 'r', encoding="utf8") as old_file, \
            open(os.path.splitext(path)[0] + "_clean.csv", 'w', encoding="utf8", newline='') as new_file:

        logging.info("Script started.")

        deleted_rows = 0
        csv_reader = csv.reader(old_file, delimiter=',')
        csv_writer = csv.writer(new_file)

        # will only write rows without empty entries to new file
        for row in csv_reader:
            if "" in row:
                deleted_rows += 1
            else:
                csv_writer.writerow(clean(row))

        if deleted_rows > 0:
            logging.warning(f"Deleted {deleted_rows} rows with empty entries.")

        logging.info("Script finished.")


if __name__ == '__main__':
    main(sys.argv[1])
