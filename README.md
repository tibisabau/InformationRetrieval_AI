# Query Rewriting with Open Source AI Models
This repository is part of the **DSAIT4050: Information Retrieval** course at **Delft University of Technology** (TU Delft), developed for the group project in Quarter 3 of the academic year 2024-2025.

The project investigates the performance of general-purpose large language models (LLMs) on query rewriting, evaluated on the [**ANTIQUE**](https://arxiv.org/abs/1905.08957) dataset using **PyTerrier**.

## Prerequisites
### Installations
Run the following command in the terminal in order to install the correct dependencies:

```
pip install -r requirements.txt
```

In case of installation errors, you may switch to using **Anaconda** or **WSL** as a workaround.

### Hugging Face API Access
Some models are hosted via Hugging Face Inference API, so a Hugging Face access token is needed in order to query them. Here are the steps:
- Go to [Hugging Face](https://huggingface.co/), and sign into your account (or create an account).
- Click on your profile picture in the top right corner, and go to **Settings** → **Access Tokens**.
- Click on the **+ Create a new token** button.
- Select the **Fine-grained** token type, and check the box **Make calls to Inference Providers**.
- Create the token.
- Go to `.env`, and replace the placeholder with your token:

```
HUGGING_FACE_API_KEY=HUGGING_FACE_ASSESS_TOKEN
```

## How to Run the Code
Run the following command in the terminal in order to run the experiment:

```
python3 experiment.py
```

This will call the Hugging Face models to rewrite the queries, evaluate the rewritten queries using MAP scores, and generate a plot (`map_scores.png`) comparing the model performances.