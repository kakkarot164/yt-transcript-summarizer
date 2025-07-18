import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "YT_transcript_summarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/summary_pipeline.py",
    f"src/{project_name}/config/config.yaml",
    "app.py",
    "main.py",
    "requirements.txt",
    "setup.py",
    "Procfile",
    "runtime.txt",
    ".gitignore",
    "README.md",
    "research/trials.ipynb",
    "assets/.gitkeep"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
