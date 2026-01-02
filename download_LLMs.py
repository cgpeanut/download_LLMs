import os
# Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)
# Change the working directory
os.chdir("/home/roxasrr/LLMs")
# Verify the change
new_directory = os.getcwd()
print("Entering Directory:", new_directory)


from huggingface_hub import snapshot_download
model_id="unsloth/Qwen-Image-2512-GGUF"
snapshot_download(repo_id=model_id, local_dir="Qwen-Image-2512-GGUF", local_dir_use_symlinks=False, revision="main")
