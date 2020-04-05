import csv

new_file = open('auto_scraper/results/dataset_no_marked_words.csv', 'w', encoding='utf8', newline='')
old_file = open('auto_scraper/results/dataset_2.csv', 'r', encoding='utf8')
reader = csv.reader(old_file, delimiter='|')
writer = csv.writer(new_file, delimiter='|')
for line in reader:
    label = '1' if '>>' in line[1] else '0'
    line = [label] + [line[1].replace('>>', '').replace('<<', '')]
    writer.writerow(line)

