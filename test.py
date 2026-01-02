import argparse
from huggingface_hub import snapshot_download

# python download_model.py --model_id "unsloth/Qwen-Image-2512-GGUF"

# 1. Set up the argument parser
parser = argparse.ArgumentParser(description="Download a model from Hugging Face Hub")
parser.add_argument("--model_id", type=str, required=True, help="The Hugging Face model ID")

# 2. Parse the arguments from the command line
args = parser.parse_args()

# 3. Retain the model_id as a variable
model_id = args.model_id

# 4. Use the variable in the function
print(f"Starting download for: {model_id}")
snapshot_download(
    repo_id=model_id, 
    local_dir=model_id.split("/")[-1], # Automatically names folder after model
    local_dir_use_symlinks=False, 
    revision="main"
)