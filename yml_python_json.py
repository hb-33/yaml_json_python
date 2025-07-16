"""
🔧 Task 2: Convert YAML → JSON (and vice versa) in Python
Script:
Write a short Python script that:
    Reads the payment_monitor_config.yaml
    Converts it into JSON format
    Writes it to a new file called payment_monitor_config.json
"""
import json
import yaml


#so we are going to use with open(filename, read mode) as f: to read the yaml file
#then we are going to convert yaml to python using to safe_load() function since we are reading from a yaml file
#then we are going to again use with open(filename, write mode) as f: and call the dump(datas, f) function since we are convering python to json


with open("payment_monitor_config.yml", "r") as f:
    data = yaml.safe_load(f) #converts yaml to python dictonary

with open("payment_monitor_config.json", "w") as f:
    json.dump(data, f, indent=2) #we don't need f.write() since we are telling where to write inside of json.dump() function

