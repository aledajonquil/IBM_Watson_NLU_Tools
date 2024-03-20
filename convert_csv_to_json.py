import json
import csv 

INPUT_FILE = 'your-input-file.csv'
OUTPUT_FILE = 'resulting-filename.json'

nlu_training_data = []

with open(INPUT_FILE, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        text = row[0]
        classification = row[1]
        nlu_training_data += [{
            'labels': [classification],
            'text': text
        }]

f = open(OUTPUT_FILE, 'w')
f.write(json.dumps(nlu_training_data, indent=2))
f.close()
