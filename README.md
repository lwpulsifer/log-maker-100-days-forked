# log-maker-100-days

Welcome to this Log Maker.

Just download the file and write `python main.py` in your terminal where the file is located to generate a log.md as this [example](log.md).

### Usage:
usage: main.py [-h] [-o] [-f FILE] [date]

positional arguments:
  date                  Set your own starting date here, format : yyyy-mm-dd

optional arguments:
  -h, --help            show this help message and exit
  -o, --overwrite       If this argument exists, overwrites existing log.md
                        file
  -f FILE, --file FILE  Specify a filename to store your log to

### Requirements :

* Python version should be 3.6 or above as I'm using the f-string format
* See `requirements.txt` for more

If you want to generate a log from a specific date (mostly and anterior date if you already started the challenge) you can do it this way :

`python main.py DATE`

This will generate a log.md starting from the given date. Most date formats should work. 
