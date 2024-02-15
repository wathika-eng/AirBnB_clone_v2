#!/bin/bash
sudo apt install python3-pip python3-virtualenv -y
# Install virtualenv
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
source venv/bin/activate

# Install fabric and pip
pip install fabric pip

# Deactivate the virtual environment
# deactivate