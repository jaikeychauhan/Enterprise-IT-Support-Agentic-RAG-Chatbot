from pathlib import Path    

root=Path(".")
print(root)

#Folders to create
folders=[
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "uploads",
    "tests"
]
# Files to create
files=[
    "app/main.py",
    "ingest-sample-kb.py",
    "run.py",
    ".env",
    "requirements.txt"
]

# Creating folders
for folder in folders:
    (root / folder).mkdir(parents=True,exist_ok=True)

# Creating files
for file in files:
    (root / file).touch(exist_ok=True)

print("Project structure created successfully.")