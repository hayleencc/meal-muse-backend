#!/bin/bash
# run_in_venv.sh

# Activate virtual environment
source .venv/bin/activate

# Run the command passed as an argument
"$@"
