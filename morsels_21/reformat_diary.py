import re


def clean_text(text):
    REPLACEMENTS = {
        "&nbsp;": " ",
        "&quot;": '"',
        "&amp;": '&',
    }
    for original, replacement in REPLACEMENTS.items():
        text = text.replace(original, replacement)
    return text


def entries_by_date(file):
    dates = []
    entries = []
    for line in file.readlines():
        if re.match(r"\d{4}-\d{2}-\d{2}", line):
            dates.append(line)
            entries.append("")
        else:
            entries[-1] += clean_text(line)

    return [(d.strip(), e.strip()) for d, e in zip(dates, entries)]


def main(filename):
    with open(filename) as f:
        converted = entries_by_date(f)

    for date, entry in converted:
        with open("{}.txt".format(date), "w") as out:
            out.write(entry)
