import requests
import re
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("HUGGING_FACE_API_KEY")
API_URL_MISTRAL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
API_URL_GOOGLE = "https://api-inference.huggingface.co/models/google/gemma-3-27b-it" 
headers = {"Authorization": f"Bearer {API_KEY}"}

# Read the prompt from a file
with open("prompt.txt", "r", encoding="utf-8") as file:
    prompt = file.read()

def query_model(text, api_url):
    payload = {"inputs": text}
    response = requests.post(api_url, headers=headers, json=payload)
    result = response.json()
    print(result)

    # Extract generated text
    generated_text = result[0]["generated_text"] if isinstance(result, list) and "generated_text" in result[0] else ""

    # Split by newline and get the last two parts
    lines = generated_text.strip().split("\n")

    if len(lines) >= 2:
        extracted_text = lines[-1]  # Get the second-last line
    else:
        extracted_text = generated_text  # Default to full text if not enough lines

    return extracted_text.strip()

def output_to_file(file, api_url):
    with open(file, "w", encoding="utf-8") as output_file:
        with open('queries.txt', 'r') as file:
            # Read each line in the queries file
            for line in file:
                # Make a request to the model
                response = query_model(prompt + "\n\n" + line.strip(), api_url)
                
                # Print the response to the console (optional)
                print(response)
                if response is not "":
                # Save each response to the output file
                    output_file.write(response + "\n")  # Write each response on a new line
                else:
                    output_file.write("placeholder" + "\n")

output_to_file("responses_mistral.txt", API_URL_MISTRAL)
output_to_file("responses_google.txt", API_URL_GOOGLE)