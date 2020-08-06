# CC-Price-Compare
Using requests and BeautifulSoup the program collects data from websites, compares them and prints out a sorted list. 

## Features
```
+ Given a games name the program compares the prices from several websites and prints the prices in decreasing order
+ GUI
+ CLI
```

## Installation
```bash
# Clone the repo
git clone git@github.com:32byte/cc_price_compare.git
# or use https
git clone https://github.com/32byte/cc_price_compare.git

# Install requirements
pip3 install -r requirements.txt
# on windows
pip install -r requirements.txt
```

## Usage
```bash
# Run gui
python3 gui.py
# or on windows
python gui.py

# Run cli
# for help use cli.py --help
python3 cli.py <game> [options]
# or on windows
python cli.py <game> [options]
```

### Syntax
```
usage: python3 cli.py <game> [options]

Commandline tool to compare prices between different websites

positional arguments:
  query       Game you're searching for

optional arguments:
  -h, --help  show this help message and exit
  --dlc       Are you searching a dlc?
  --max MAX   Max number of results per website
```

## Github-Commands
```bash
# ALWAYS PULL BEFORE YOU PUSH

git clone url # download the project

git add file # add the file to the repository (project)

git commit -m "Message" # Your changes 

git pull # Download all new chantges

git push # Uplaod your changes
```