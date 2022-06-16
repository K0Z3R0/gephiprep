# Gephiprep
A tool that creates an edge file and a node file that are used as an input in order to create a social network in Gephi.
## Usage
```
usage: gephiprep.py [-h] -s SOURCE -d DEST [-w WEIGHT] File

Creates nodes and edge file from a csv file for gephi

positional arguments:
  File                  the path to list

options:
  -h, --help            show this help message and exit

required arguments:
  -s SOURCE, --source SOURCE
                        The Source column name
  -d DEST, --dest DEST  The destination column name

optional arguments:
  -w WEIGHT, --weight WEIGHT 
 ```
