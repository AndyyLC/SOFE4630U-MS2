import time
from google.cloud import pubsub_v1      # pip install google-cloud-pubsub  ##to install
import glob                             # for searching for json file 
import json
import os 
import csv
import numpy as np  

# Search the current directory for the JSON file (including the service account key) 
# to set the GOOGLE_APPLICATION_CREDENTIALS environment variable.
files=glob.glob("*.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=files[0];


# Set the project_id with your project ID
project_id="amiable-nirvana-449116-h3";
topic_name = "CSV";   # change it for your topic name if needed

# create a publisher and get the topic path for the publisher
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)
print("Published messages with ordering keys to {topic_path}.")

# read csv file to a list of dictionaries
with open('Labels.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader : 
        data = row

        message_json = json.dumps(row)
        # Convert the JSON string to bytes (serialization)
        message_bytes = message_json.encode("utf-8")

        # Publish the message
        time.sleep(1)
        print(f"Producing a record: {message_json}")
        future = publisher.publish(topic_path, message_bytes)
        
        # # convert the string to bytes (serialization)
        # message=str(data).encode('utf-8')
        
        # # send the value    
        # print("Producing a record: {}".format(message))
        # future = publisher.publish(topic_path, message);
        
        #ensure that the publishing has been completed successfully
        future.result()

        




 