gitignore_content = """
#Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
venv/
env/
myenv/
.venv/
.env/

# Environment variables
.env

# Database files
*.sqlite3

# Logs
*.log

# OS generated files
.DS_Store
Thumbs.db

# IDE files
.vscode/
.idea/

# Python notebooks
*.ipynb_checkpoints/
"""

with open('.gitignore', 'w') as file:
    file.write(gitignore_content.strip())

print(".gitignore file created successfully");