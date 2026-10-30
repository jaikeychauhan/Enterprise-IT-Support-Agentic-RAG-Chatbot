1. Create .env file to have all the API Keys for example:
    OPENAI_API_KEY="key-value"
2. Create the Virtual Environment using below command
    Command: python -m venv venv
3. Now activate the V.E. using below command
   command:  .\venv\Scripts\Activate.ps1
   NOTE: If get any error the execute "Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass"
   Then try again now
4. Create a requirements.txt file and add the package names for installing the packages and run the below command to install these packages
    pip install -r requirements.txt
        or (if system blocks the PIP command then)
    python pip install -r requirements.txt

5. Now we can create folders for work
6. We need to create requirements.txt file to download/install all the packages
7. Add .gitignore file to skip sensitive files data to merge in git repository