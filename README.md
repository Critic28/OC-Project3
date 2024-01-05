# OC-Project3

## How to run ETL

To run the ETL pipeline you will need a few things installed:

- [Python](https://www.python.org/downloads/)
- Pip installed should come with the latest version of python
- Pandas (is already installed in environment)

You can either open the folder in a IDE like VSCode or Pycharm and run it manually there or from the command line by moving into the directory and running the command python .\main.py

## How to Activate Virtual Environment

- Clone the repository using git clone (url) this will give you all of the files in the repository
- In the terminal you will cd into the Scripts folder and run .\activate and that will activate your environment

## How to generate a flake8 file

- First you need to install flake8 using pip install flake8
- Create a directory you want to create the flake8 file in
- Run the command ```python3 -m flake8 --docstring-convention google --format=html --htmldir=reports/flake```

- Open the index file in a browser and it will display your report
