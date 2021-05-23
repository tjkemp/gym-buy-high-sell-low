#!/usr/bin/env bash

function process_status () {
  if [ $? -ne 0 ]; then
    echo " FAILED"
    exit 1
  else
    echo " OK"
  fi
};

echo Creating a virtual environment \"venv\"...
python -m venv venv || { process_status; }

echo Updating pip and friends...
venv/bin/pip install -q --upgrade pip setuptools wheel || { process_status; }

if [ -x "$(command -v pip-compile)" ]; then
  echo Updating requirements.txt with pip-compile...
  pip-compile -q requirements/requirements.in || { process_status; }
else
  echo WARNING - Install pip-tools and run pip-comile to keep your requirements.txt up to date
fi

echo Installing dependencies...
venv/bin/pip install -q -r requirements/requirements.txt || { process_status; }

echo Creating a VS Code default settings file...
cp .vscode/settings-default.json .vscode/settings.json

echo Virtual environment created. Type \"source venv/bin/activate\" to activate it. Type \"code .\" to start coding.
