import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cpu"
model_path = "ibm-granite/granite-3.0-1b-a400m-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_path)
# drop device_map if running on CPU
with open("prompt.txt", "r", encoding="utf-8") as file:
    prompt = file.read()
model = AutoModelForCausalLM.from_pretrained(model_path)
model.eval()
# change input text as desired
with open("responses_ibm.txt", "w", encoding="utf-8") as output_file:
    with open('queries.txt', 'r') as file:
        # Read each line in the queries file
        for line in file:
            # Make a request to the model
            chat = [
                { 
                    "role": "user", "content": prompt + " " + line.strip() 
                },
            ]
            chat = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
            # tokenize the text
            input_tokens = tokenizer(chat, return_tensors="pt").to(device)
            # generate output tokens
            output = model.generate(**input_tokens, 
                                    max_new_tokens=100)
            # decode output tokens into text
            output = tokenizer.batch_decode(output)

            response = output[0].split(">")[-2].split("<")[0]
            print(response)
            output_file.write(response + "\n")