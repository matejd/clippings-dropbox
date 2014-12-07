#!/usr/bin/env python3
# encoding: utf-8

import sys, re, csv, tempfile, shutil
from datetime import datetime

def usage():
    print('Converts My Clippings.txt Kindle file to CSV format.')
    print('Usage: convert_csv.py <clippings.txt> <converted.csv> [--verbose]')
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
    verbose = False
    args = sys.argv[1:]
    for i, arg in enumerate(args[:]):
        if arg == '--verbose':
            verbose = True
            del args[i]
    if len(args) < 2:
        usage()
    contents = None
    try:
        contents = open(args[0]).read()
    except IOError:
        print('Failed to open ' + args[0])
        sys.exit(2)
    clips = contents.split('==========\n')
    assert len(clips) > 1
    del clips[-1]

    # Go through clips, try to extract title, author, time and content.
    # In case format changes and this regular expression doesn't match it anymore,
    # report that (if verbose option is set). We could just use re.findall, but then
    # there would be no feedback in case the regular expression is outdated or otherwise buggy.
    num_failed_clips = 0
    pattern_title_author = re.compile(r'(.*?) \((.*?)\)')
    pattern_date = re.compile(r'Added on (.*)')
    tmp_file = tempfile.NamedTemporaryFile(mode='w', newline='', delete=False)
    csv_writer = csv.DictWriter(tmp_file, fieldnames=['author', 'title', 'date', 'content'])
    csv_writer.writeheader()
    for clip in clips:
        try:
            lines = clip.splitlines()
            assert len(lines) == 4
            m = pattern_title_author.match(lines[0])
            assert m
            title = m.group(1)
            author = m.group(2)
            m = pattern_date.search(lines[1])
            assert m
            date_str = m.group(1)
            date = datetime.strptime(date_str, '%A, %B %d, %Y %I:%M:%S %p')
            content = lines[3]
            csv_writer.writerow({'author': author, 'title': title, 'date': date, 'content': content})
        except (AssertionError, ValueError):
            if verbose:
                print('Failed to match clip: ')
                print()
                print(clip)
                num_failed_clips += 1
            else:
                num_failed_clips += 1
    tmp_file.close()
    shutil.copyfile(tmp_file.name, args[1])
    print('Number of clips found: ' + str(len(clips)))
    print('Number of clips failed to match (should be 0): ' + str(num_failed_clips))
