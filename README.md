# Misc Scripts
Miscellaneous Python Scripts

## First Time setup

run command 
```bash
bash init
```

This sets up the execution permissions for the config script which allows you easily modify the config file used by each script.

## Config

The config script can be used to modify the config file (conf.conf). It provides an alternative to manually editing the file, although that does remain an option.

To use the script, execute the command

```bash
./config [options]
```

To see a list of available options, execute the command with either no options or the -h option.

## Usage
### Anagram Solver

This script finds all perfect anagrams of the input word. It loads the wordfile configured in the config file (conf.conf) and asks you for the initial word. It then returns all perfect anagrams (same length & same letters) of the input word.

Execute the script using the command
```bash
python3 anagram.py
```

### Day of week Finder

This script returns the day of the week that a given day is. It asks for a date in ISO format (YYYY-MM-DD).

Execute the script using the command
```bash
python3 dayFinder.py
```
It is based on the information at this site: https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html 
