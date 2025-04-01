from util import search, evaluate, evaluate_all
import matplotlib.pyplot as plt
import pyterrier as pt
import pandas as pd
import re
import subprocess
import os 


DATASET = pt.datasets.get_dataset("irds:antique/test/non-offensive")
topics = DATASET.get_topics()
original_topics = topics.copy()
scores = {}
venv_python = os.path.join("venv", "Scripts", "python.exe") # Windows venv

with open("queries.txt", "w", encoding="utf-8") as file:
    for qid, query in topics.iterrows():
        file.write(f"{query['query']}\n")

## If using venv
subprocess.run([venv_python, "models_api.py"])
subprocess.run([venv_python, "models_pipeline.py"])

## If using machine python exe
# subprocess.run(["python", "models_api.py"])
# subprocess.run(["python", "models_pipeline.py"])

def get_MAP(file):
    with open(file, "r", encoding="utf-8") as file:
        rewritten_queries = [re.sub(r'[^a-zA-Z0-9\s]', '', line.strip()) for line in file.readlines()]
    topics.loc["query"] = rewritten_queries
    # print("Modified Topics" +  file  + "MAP Score:", evaluate(topics))
    scores[file] = evaluate(topics)

print("Original Topics MAP Score:", evaluate(original_topics))
scores["original"] = evaluate(original_topics)

get_MAP("responses_ibm.txt")
get_MAP("responses_mistral.txt")
get_MAP("responses_google.txt")

print("MAP Scores:")
for model, score in scores.items():
    print(f"{model}: {score}")

labels = ["Original", "IBM", "Mistral", "Google"]
map_scores = list(scores.values())

plt.figure(figsize=(10, 6))
plt.bar(labels, map_scores, color=['blue', 'orange', 'green', 'red'])
plt.xlabel("Model")
plt.ylabel("MAP Score")
plt.title("MAP Scores for Different Models")
plt.xticks(rotation=45)
plt.ylim(0, max(map_scores) + 0.05)
plt.tight_layout()
plt.savefig("map_scores.png")
plt.show()