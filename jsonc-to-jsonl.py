import json
import json5 as jsonc
import os

# Input and output file paths
input_file_path = os.path.join(os.path.dirname(__file__), 'training-data.jsonc')  # Change to your JSONC file
output_file_path = os.path.join(os.path.dirname(__file__), 'output.jsonl')

# Read and parse JSONC file
try:
    with open(input_file_path, 'r', encoding='utf8') as file:
        raw_content = file.read()
except FileNotFoundError:
    print(f"Error: The input file '{input_file_path}' does not exist.")
    exit(1)

# Parse the JSONC content
try:
    data_array = jsonc.loads(raw_content)
except json.JSONDecodeError as e:
    print(f"Error parsing JSONC content: {e}")
    exit(1)

# Convert array to JSONL format
jsonl_content = ""

# Loop through the parsed data
for obj in data_array:
    obj['messages'][2]['content']  = json.dumps(obj['messages'][2]['content'])
    # Append the object to the JSONL content (as a JSON object, including the stringified 'content' for assistant)
    jsonl_content += json.dumps(obj) + "\n"

# Write to output JSONL file
try:
    with open(output_file_path, 'w', encoding='utf8') as file:
        file.write(jsonl_content)
    print(f"Converted JSONC to JSONL: {output_file_path}")
except Exception as e:
    print(f"Error writing to output file: {e}")
    exit(1)