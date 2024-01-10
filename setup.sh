#!/bin/bash

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Additional setup steps if needed
# ...

# Print a message indicating successful setup
echo "Environment setup complete."
