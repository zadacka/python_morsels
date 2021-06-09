#! /usr/bin/python
from argparse import ArgumentParser, FileType


# Early attempt: tried to use str.encode('ascii', errors=<>) to do the conversion
# with open(args.filename, encoding='utf-8') as f:
#   for line in f.readlines():
#       line_as_bytes = line.encode(encoding='utf-8')
#       line_as_string = line_as_bytes.decode(encoding='ascii', errors=errors)
#       print(line_as_string, end='')

def convert(char, style):
    code = ord(char)
    if code <= 127:  # can be represented as ascii
        return char
    elif style == 'html':  # style set to 'html'
        return f"&#{hex(code)[1:]};"
    elif code <= 0xffff:  # use four hex digits when possible
        return rf"\u{hex(code)[2:]:0>4}"
    else:  # else use full Unicode escaping
        return rf"\U{hex(code)[2:]:0>8}"


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file', type=FileType('rt', encoding='UTF-8'))
    parser.add_argument('--style', default='default', choices=['html', 'default'])
    args = parser.parse_args()

    converted_string = ''.join(
        convert(character, style=args.style)
        for character in args.file.read()
    )

    print(converted_string, end="")

