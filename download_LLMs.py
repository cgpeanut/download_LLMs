import os
# Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)
# Change the working directory
os.chdir("/home/roxasrr/LLMs")
# Verify the change
new_directory = os.getcwd()
print("New Directory:", new_directory)


#from huggingface_hub import snapshot_download
#model_id="codellama/CodeLlama-70b-Python-hf"
#snapshot_download(repo_id=model_id, local_dir="CodeLlama-70b-Python-hf", local_dir_use_symlinks=False, revision="main")
