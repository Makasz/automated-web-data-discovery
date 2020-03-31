import csv
from utils import keywords

def filter_by_keyword(keywords, text):
    found = [word for word in keywords if word in text]
    return found


old_file = open('results/result.csv', 'r', encoding='utf8')
new_file = open('results/result_filtered.csv', 'w', encoding='utf8', newline='')
reader = csv.reader(old_file, delimiter='|')
writer = csv.writer(new_file, delimiter='|')
for line in reader:
    if filter_by_keyword(keywords, line[-1]):
        line[-1] = line[-1].replace('\n', '')
        line.append()
        writer.writerow(line)
        print(line)
