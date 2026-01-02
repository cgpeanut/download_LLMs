import subprocess # just to call an arbitrary command e.g. 'ls'

# enter the directory like this:
with cd("~/LLMs"):
   # we are in ~/Library
   subprocess.call("ls")

# outside the context manager we are back wherever we started.





#from huggingface_hub import snapshot_download
#model_id="codellama/CodeLlama-70b-Python-hf"
#snapshot_download(repo_id=model_id, local_dir="CodeLlama-70b-Python-hf", local_dir_use_symlinks=False, revision="main")
