#!/bin/bash

# Migrate DB
flask db upgrade || exit 1

# Run the API
python3 -m spellbook.run || exit 1
