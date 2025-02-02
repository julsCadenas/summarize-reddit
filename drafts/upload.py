from huggingface_hub import upload_folder

repo_name = "julsCadenas/summarize-reddit"

upload_folder(
    folder_path="insert your path here", 
    repo_id=repo_name,
    repo_type="model"
)
