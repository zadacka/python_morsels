import argparse
import csv


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_filename')
    parser.add_argument('output_filename')
    parser.add_argument('--in-delimiter', dest='delimiter')
    parser.add_argument('--in-quote', dest='quote')
    args = parser.parse_args()

    arguments = {}
    if args.delimiter:
        arguments['delimiter'] = args.delimiter
    if args.quote:
        arguments['quotechar'] = args.quote
    if not (args.delimiter or args.quote):
        with open(args.input_filename) as input_file:
            arguments['dialect'] = csv.Sniffer().sniff(input_file.read())

    with open(args.input_filename) as input_file:
        with open(args.output_filename, mode='w') as output_file:
            reader = csv.reader(input_file, **arguments)
            writer = csv.writer(output_file)
            for line in reader:
                writer.writerow(line)
#
# def guess_delimiter(input_filepath, potential_delimiters):
#     """
#     Guess the delimiter (or quote character) used in a file:
#     * open the file and read a line of text
#     * return the first character found in the 'potential_delimiters' list
#     * return None if no match found
#     This works around frequency-based problems (spaces are common, but commas are
#       more likely to be the *actual* delimiter even if less common) but is a pretty
#       manual hack at what turns out to be a solved problem. Use csv.Sniffer
#     """
#
# Example use:
# quote = guess_delimiter(args.input_filename, potential_delimiters='"\'|')
# delimiter = guess_delimiter(args.input_filename, potential_delimiters=",\t| ")

#     with open(input_filepath) as file:
#         text = file.readline()
#
#     for potential_delimiter in potential_delimiters:
#         if potential_delimiter in text:
#             return potential_delimiter
#     return None
