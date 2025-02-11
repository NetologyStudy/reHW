import csv
from format_phonebook import normalize_contact

if __name__ == '__main__':
  with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(normalize_contact())

