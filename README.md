# IBM Watson NLU Tools
This repository contains scripts and curl commands to make it easier to work with the IBM Watson NLU.

## Prerequisites
* An IBM account with access to the Watson NLU.
* Python installed, and a basic understanding of how to run Python commands
* curl installed

## Convert Training Data from CSV to JSON
The NLU requires the training data to be in the following JSON format:

`
[
    {
        "text": "document 1",
        "labels": ["label1"]
    },
    {
        "text": "document 2",
        "labels": ["label2", "label3"]
    }
]
`
However, it's more likely that your training data will be in a .csv file. The script convert_csv_to_json.py, written by Corey Clemente, will convert the data to JSON format for you. 

### Usage
* Place the convert_csv_to_json.py file in the same directory as your .csv file.
* Run `python convert_csv_to_json.py` from the command line.
