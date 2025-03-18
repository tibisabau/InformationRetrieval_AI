from util import search, evaluate, evaluate_all
import pyterrier as pt
import pandas as pd

DATASET = pt.datasets.get_dataset("irds:antique/test/non-offensive")
topics = DATASET.get_topics()
original_topics = topics.copy()
with open("queries.txt", "w", encoding="utf-8") as file:
    for qid, query in topics.iterrows():
        file.write(f"{query['query']}\n")

with open("rewritten_queries.txt", "r", encoding="utf-8") as file:
    rewritten_queries = [line.strip() for line in file.readlines()]

# Ensure the number of rewritten queries matches the original number
if len(rewritten_queries) != len(topics):
    raise ValueError("Mismatch between the number of original and rewritten queries")

# Replace the original queries with the rewritten ones
topics["query"] = rewritten_queries

print("Original Topics MAP Score:", evaluate(original_topics))
print("Modified Topics MAP Score:", evaluate(topics))
