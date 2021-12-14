#!/bin/bash

# Migrate DB
flask db upgrade || exit 1

# Run the API
if [[ "${TK_DEBUG}" == "0" ]]; then
  uwsgi uwsgi.ini || exit 1
else
  python3 -m spellbook.application || exit 1
fi
