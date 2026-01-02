#!/usr/bin/env python3

import os
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(description="Download a model from Hugging Face Hub")
parser.add_argument("--model_id", type=str, required=True, help="The Hugging Face model ID")

# Parse the arguments from the command line
args = parser.parse_args()

# Retain the model_id as a variable
model_id = args.model_id

# Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)
# Change the working directory
os.chdir("/home/roxasrr/LLMs")
# Verify the change
new_directory = os.getcwd()
print("Entering Directory:", new_directory)


from huggingface_hub import snapshot_download

# 4. Use the variable in the function
# python download_model.py --model_id "unsloth/Qwen-Image-2512-GGUF"

print(f"Starting download for: {model_id}")
snapshot_download(
    repo_id=model_id, 
    local_dir=model_id.split("/")[-1], # Automatically names folder after model
    local_dir_use_symlinks=False, 
    revision="main"
)