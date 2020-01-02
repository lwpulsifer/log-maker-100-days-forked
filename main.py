import datetime
import dateparser
from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument("date", nargs='?', default="",
                        help="Set your own starting date here, format : yyyy-mm-dd")
    parser.add_argument("-o", "--overwrite", action='store_true', help="If this argument exists, \
                        overwrites existing log.md file")
    parser.add_argument("-f", "--file", default="log.md", action='store', help="Specify a filename to store your log to")
    return parser.parse_args()

def get_start_date(args):
    if args.date:
        start_day = dateparser.parse(args.date)
    else:
        start_day = datetime.date.today()
    return start_day

def write_log_file(args, start_day):

    if args.overwrite:
        open_string = "w"
    else:
        open_string = "x"

    with open(args.file, open_string) as f:
        f.write(f"""# 100 Days Of Code - Log   
*Main Commitment*:

I will code in **Python** programming language for at least an hour every day for the next 100 days.

Start Date: {start_day.strftime("%B %d, %Y")}
End Date (without any breaks): {(start_day + datetime.timedelta(100)).strftime("%B %d, %Y")}

----
## Days:
|+|00                                    |10                                   |20                                 |30                                  |40                                  |50                                  |60                                  |70                                  |80                                  |90                                    |
|--|-------------------------------------|-------------------------------------|-----------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|--------------------------------------|
""")

        for i in range(10):
            f.write(f"|{i:02d}|")
            for j in range(1, 100, 10):
                day_format = start_day.strftime("%B-%d-%Y")
                f.write(f"[Day {i+j}](#day-{i+j}-{day_format.lower()}) | ")
                start_day += datetime.timedelta(10)
            if i+j == 99:
                f.write(f"[Day 100](#day-100-{day_format.lower()}) | ")
            f.write("\n")
            start_day -= datetime.timedelta(99)

        f.write(f"\n[Or Jump Right To Conclusion!](#Conclusion)\n")

        if args.date:
            start_day = dateparser.parse(args.date)
        else:
            start_day = datetime.date.today()

        for i in range(1, 101):
            day_format = start_day.strftime("%B, %d, %Y")
            f.write(f"""
### Day {i}: {day_format}

**Today's Progress**:

**Thoughts:**

**Link(s) to work**: [Example](http://www.example.com)

[Back to Top](#days)

----""")
            start_day += datetime.timedelta(1)

        f.write(f"\n\n\n# Conclusion\n\n")

def main():
    args = get_args()
    start_date = get_start_date(args)
    write_log_file(args, start_date)

if __name__ == '__main__':
    main()
