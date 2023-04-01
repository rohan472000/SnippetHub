import json 

def create_json_schema(file_path: str) -> None:
    """
    Reads a text file containing column names and types separated by a comma, creates a list of dictionaries
    representing each column with its name, type, mode, and description, and saves it as a JSON file.

    :param file_path: A string with the path to the input text file.
    :return: None

    Example:

    >>> create_json_schema("columns_names.txt")
    """
    blocks = []
    
    with open(file_path) as f:
        lines = f.readlines()   
        for line in lines:     
            values = line.strip().split(',') 
            name = values[0]      
            type = values[1]         
            block = {"name": name, "type": type, "mode": "NULLABLE", "desc": ""}   
            blocks.append(block)         
    
    with open("output.json", "w") as f: 
        json.dump(blocks, f, indent=4)
