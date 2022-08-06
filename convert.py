import csv

txt_file = r"telephon_book.txt"
csv_file = r"telephon_book.csv"
def converti():
    with open(txt_file, 'r') as infile, open(csv_file, 'w', newline = '') as outfile:
        tripped = (line.strip() for line in infile)
        lines = (line.split() for line in tripped if line)
        writer = csv.writer(outfile)
        writer.writerows(lines)
