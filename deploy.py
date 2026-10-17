"""Push the app to a Hugging Face Space."""
import os
import sys

from dotenv import load_dotenv
from huggingface_hub import HfApi

FILES = ["app.py", "requirements.txt", "README.md", "me/business_summary.txt", "me/about_business.pdf", "assets/bob.jpeg", "assets/paw.svg"]

if len(sys.argv) != 2:
    sys.exit("Usage: python deploy.py <your-hf-username>")
repo_id = f"{sys.argv[1]}/boxbnb"

missing = [f for f in FILES if not os.path.exists(f)]
if missing:
    sys.exit(f"Missing files: {missing}. Run this from the repo root.")

load_dotenv()
key = os.getenv("GOOGLE_API_KEY")
if not key:
    sys.exit("GOOGLE_API_KEY not found in .env")

api = HfApi()
api.create_repo(repo_id, repo_type="space", space_sdk="gradio", exist_ok=True)
api.add_space_secret(repo_id, "GOOGLE_API_KEY", key)
api.upload_folder(repo_id=repo_id, repo_type="space", folder_path=".", allow_patterns=FILES,
                  commit_message="Deploy Boxbnb")
print(f"Done: https://huggingface.co/spaces/{repo_id}")
