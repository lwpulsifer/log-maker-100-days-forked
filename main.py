import datetime
import dateparser
from argparse import ArgumentParser
from log_table import LogTable


def get_args():
    parser = ArgumentParser()
    parser.add_argument("date", nargs='?', default="",
                        help="Set your own starting date here, format : yyyy-mm-dd")
    parser.add_argument("-o", "--overwrite", action='store_true', help="If this argument exists, \
                        overwrites existing log.md file")
    parser.add_argument("-f", "--file", default="log.md", action='store', help="Specify a filename to store your log to")
    parser.add_argument("-d", "--days", default=100, action='store', type=int, help="Specify the number of days in your log")
    return parser.parse_args()

def get_start_date(args):
    if args.date:
        start_day = dateparser.parse(args.date)
    else:
        start_day = datetime.date.today()
    return start_day

def get_file_open_string(args):
    if args.overwrite:
        open_string = "w"
    else:
        open_string = "x"
    return open_string

def get_num_days(args):
    return args.days

def write_log_file(args, start_day):

    open_string = get_file_open_string(args)
    num_days = get_num_days(args)
    num_buckets = [i * (num_days // 10) for i in range(10)]

    with open(args.file, open_string) as f:
        log_table = LogTable(start_day, days=num_days)
        f.write(log_table.get_intro())
        f.write(log_table.get_string_table())
        f.write(log_table.get_diary())
        f.write(f"\n\n\n# Conclusion\n\n")

def main():
    args = get_args()
    start_date = get_start_date(args)
    write_log_file(args, start_date)

if __name__ == '__main__':
    main()
