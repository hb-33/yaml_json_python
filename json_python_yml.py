import json
import yaml


#We are going to convert json from payment_monitor_config.json into yml file

#So first we need to read the json file using wiht open(filename, "r") as f:
#And convert, json to python using the load() function
#Then, we need to open the yml file and have the write model and then convert python to yml using safe_dump() since file

with open("payment_monitor_config.json", "r") as f:
    python_data = json.load(f)

with open("payment_monitor_config2.yml", "w") as f:
    yaml.dump(python_data, f, indent=2)
