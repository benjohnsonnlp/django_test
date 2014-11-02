from collections import defaultdict
import csv
import io
import json
import requests

__author__ = 'ben'

csv_url = 'https://docs.google.com/spreadsheet/pub?key=0AsKyuF-d-OHadEJQYjlPbzByclBXZUNZcE1PcXdydXc&output=csv'

csv_text = requests.get(csv_url).text

f = io.StringIO(csv_text)

rows = csv.reader(f)

cards = defaultdict(list)

qualities = ['best', 'excellent', 'good', 'average', 'poor', 'terrible',]

next(rows)

for row in rows:
    for index in range(1, 7):
        cards[qualities[index - 1]].append(row[index].lower())
        #when index = 1
        # cards['best'].append(row[index]))


# TODO: Take a list of card names and print them out in sorted order
def compare_cards(c1, c2):
    c1_quality, c2_quality = None, None
    c1_index, c2_index = None, None
    for key, value in cards.items():
        if c1.lower() in value:
            c1_quality = key
            c1_index = value.index(c1)
        if c2.lower() in value:
            c2_quality = key
            c2_index = value.index(c2)

    if not c1_quality or not c2_quality:
        return "Cards not valid"

    if qualities.index(c1_quality) < qualities.index(c2_quality): #checks to see if c1 is "higher quality"
        return c1
    elif qualities.index(c2_quality) < qualities.index(c1_quality):
        return c2
    elif c1_index < c2_index:
        return c1
    elif c1_index > c2_index:
        return c2
    else:
        return "Equal"


if __name__ == '__main__':
    print(cards)
    print(compare_cards("Lorewalker Cho", "Onyxia"))
    print(compare_cards("Tinkmaster Overspark", "Nozdormu"))
    print(json.dumps(cards, indent=4))