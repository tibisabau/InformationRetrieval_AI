import requests
import re

API_KEY = "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" # Tibi's API key
# API_KEY = "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" # Kevin's API key
API_URL_MISTRAL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3" # type = chat model
API_URL_GOOGLE = "https://api-inference.huggingface.co/models/google/flan-t5-small" # type = pretrained
headers = {"Authorization": f"Bearer {API_KEY}"}

# Read the prompt from a file
with open("prompt.txt", "r", encoding="utf-8") as file:
    prompt = file.read()

def query_model(text, api_url):
    payload = {"inputs": text}
    response = requests.post(api_url, headers=headers, json=payload)
    print(response)
    result = response.json()
    print(result)
    # Extract generated text
    generated_text = result[0]["generated_text"] if isinstance(result, list) and "generated_text" in result[0] else ""

    # Use regex to split sentences and get the last one
    sentences = re.split(r'(?<=[.!?:\n])\s+', generated_text.strip())  # Splits at ., !, or ? followed by a space
    last_sentence = sentences[-1] if sentences else generated_text  # Get the last sentence

    return last_sentence.strip()

def output_to_file(file, api_url):
    with open(file, "w", encoding="utf-8") as output_file:
        with open('queries.txt', 'r') as file:
            # Read each line in the queries file
            for line in file:
                # Make a request to the model
                response = query_model(prompt + "\n\n" + line.strip(), api_url)
                
                # Print the response to the console (optional)
                print(response)
                
                # Save each response to the output file
                output_file.write(response + "\n")  # Write each response on a new line

output_to_file("responses_mistral.txt", API_URL_MISTRAL)
output_to_file("responses_google.txt", API_URL_GOOGLE)