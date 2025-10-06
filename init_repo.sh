#!/bin/bash

# Initialize git repository
git init

# Change default branch to main
git branch -M main

# Add remote origin
git remote add origin https://github.com/CDCgov/cfa-catalog-pub.git

echo "Git repository initialized successfully!"
echo "Default branch: main"
echo "Remote origin: https://github.com/CDCgov/cfa-catalog-pub.git"
