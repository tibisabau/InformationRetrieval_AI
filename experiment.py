from util import search, evaluate, evaluate_all
import pyterrier as pt
import pandas as pd
import re
import subprocess

subprocess.run(["python", "models_api.py"])
subprocess.run(["python", "models_pipeline.py"])

DATASET = pt.datasets.get_dataset("irds:antique/test/non-offensive")
topics = DATASET.get_topics()
original_topics = topics.copy()
with open("queries.txt", "w", encoding="utf-8") as file:
    for qid, query in topics.iterrows():
        file.write(f"{query['query']}\n")

def get_MAP(file):
    with open(file, "r", encoding="utf-8") as file:
        rewritten_queries = [re.sub(r'[^a-zA-Z0-9\s]', '', line.strip()) for line in file.readlines()]
    topics.loc[:49, "query"] = rewritten_queries[:50]
    print("Modified Topics" +  file  + "MAP Score:", evaluate(topics))

print("Original Topics MAP Score:", evaluate(original_topics))

get_MAP("responses_ibm.txt")
get_MAP("responses_mistral.txt")
get_MAP("responses_google.txt")

