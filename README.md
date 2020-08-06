# CC-Price-Compare
Using requests and BeautifulSoup the program collects data from websites, compares them and prints out a sorted list. 

## Features
```
+ Given a games name the program compares the prices from several websites and prints the prices in decreasing order
+ GUI
+ CLI
```

## Installation
### Linux
```bash
# Basic install
sudo bash -c "$(curl https://raw.githubusercontent.com/32byte/cc_price_compare/master/unix-install.sh)"

# Download and install
curl https://raw.githubusercontent.com/32byte/cc_price_compare/master/unix-install.sh > unix-install.sh
# or with wget
wget https://raw.githubusercontent.com/32byte/cc_price_compare/master/unix-install.sh

chmod +x unix-install.sh

# Install
./unix-install.sh
# Update
./unix-install.sh update
# Uninstall
./unix-install.sh uninstall
```

### Windows
```bash
# or use https
git clone https://github.com/32byte/cc_price_compare.git
# on windows
pip install -r requirements.txt
```

## Usage
### Linux
```bash
# Run gui
cc_price_gui

# for help use cli.py --help
cc_price_cli <game> [options]
```

### Windows
```bash
# Run gui
python gui.py

# for help use cli.py --help
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