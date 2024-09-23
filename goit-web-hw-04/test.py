# from datetime import datetime
# str = "username=Petro&message=Hello+Alex+T%21"
# parse_dict = {key: value for key, value in [el.split('=') for el in str.split('&')]}
# print([el.split('=') for el in str.split('&')])
# p = datetime.now()
# format_string = "%Y-%m-%d %H:%M:%S" 
# pf= p.strftime(format_string)
# parse_dict.update({"time":pf })
# print(parse_dict)

import json

def add_to_json(filename, new_data):
    """
    Adds new data to a JSON file, preserving existing content.

    Args:
        filename: The name of the JSON file.
        new_data: A dictionary containing the new data to add.
    """

    try:
        # Read the existing JSON data from the file
        with open(filename, 'r') as f:
            existing_data = json.load(f)

        # Update the existing data with the new data
        existing_data.update(new_data)

        # Write the updated data back to the file
        with open(filename, 'w') as f:
            json.dump(existing_data, f, indent=4)

        print("Data added successfully to", filename)

    except FileNotFoundError:
        print("File not found:", filename)
    except json.JSONDecodeError:
        print("Error decoding JSON data in", filename)

if __name__ == "__main__":
    # Example usage:
    filename = "data.json"
    new_data = {"key1": "value1", "key2": "value2"}

    add_to_json(filename, new_data)