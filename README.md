# IBM Watson NLU Tools
This repository contains scripts and curl commands to make it easier to work with the IBM Watson NLU.

## Prerequisites
* An IBM account with access to the Watson NLU.
* Python installed, and a basic understanding of how to run Python commands
* cURL installed

## Convert Training Data from CSV to JSON
The NLU requires the training data to be in the following JSON format:

```
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
```
However, it's more likely that your training data will be in a .csv file. The script convert_csv_to_json.py, written by Corey Clemente (https://github.com/coreyclemente), will convert the data to JSON format for you. 

### Usage
* Place the convert_csv_to_json.py file in the same directory as your .csv file.
* Run `python convert_csv_to_json.py` from the command line.

## cURL commands
Searching through IBM's documentation can be frustrating, so I'm compiling some commonly used curl commands here, for ease of use. I've placed all placeholder values inside of {{ }} to make it clear which parts need to be replaced. Remove the curly braces when replacing the placeholder values.

### Create a new classifier
Use this command to create a new NLU classifier

You will need:
* An apikey
* The name of your training data JSON file
* A name for your new classifier
* Your IBM NLU service URL

```
curl -X POST -u "apikey:{{your-API-key}}" -H "Content-Type: multipart/form-data" -F "training_data=@{{your-json-file.json}};type=application/json" -F "language=en" -F "{{name=name-of-your-classifier}}" -F "model_version=2022-01-06" "{{your-nlu-service-url}}/v1/models/classifications?version=2021-08-01"
```

### Check the status of a classifications model
Use this command to see when a classifier is done training.

You will need:
* An apikey
* Your IBM NLU service URL
* A classifier model_id

You can find the classifier's model_id by running the 'List NLU Classifiers' curl command below this one.

```
curl -X GET -u "apikey:{{your-API-key}}" "{{your-nlu-service-url}}/v1/models/classifications/{{model_id}}?version=2021-03-23"
```

### List NLU Classifiers
This command will list all of your classifiers that currently exist on the NLU.

You will need:
* An apikey
* Your IBM NLU service URL

```
curl -u "apikey:{{your-API-key}}" "{{your-nlu-service-url}}/v1/models/classifications?version=2021-08-01"
```

### Delete a Classifier
It's good practice to keep your previous classifier & create a new one with improved data during your iteration process. This way, you can easily revert back to the previous version if your new training data doesn't create the improvement you would expect. However, you still may need to delete a classifier if something goes wrong during creation or training. 

You will need:
* An apikey
* Your IBM NLU service URL
* The classifier model_id

```
curl --user "apikey":"{{your-API-key}}" "{{your-nlu-service-url}}/v1/models/classifications/{{model_id}}?version=2021-03-23" --request DELETE
```
