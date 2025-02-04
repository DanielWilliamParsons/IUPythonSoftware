#!/bin/bash

# Exit if any command fails
set -e

# Variables
REPO_NAME="IUPythonSoftware"
GITHUB_USERNAME="DanielWilliamParsons"
REMOTE_URL="git@github.com:$GITHUB_USERNAME/$REPO_NAME.git"

# Initialize git repository
git init

# Add remote origin
git remote add origin "$REMOTE_URL" 2>/dev/null || echo "⚠️ Remote origin already exists."

# Add all files, commit, and push to GitHub
git add .
git commit -m "Initial commit" || echo "⚠️ Nothing to commit."
git branch -M main
git push -u origin main

echo "✅ Successfully pushed to GitHub!"
