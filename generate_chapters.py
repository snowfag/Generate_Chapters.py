#!/usr/bin/env python3
import re, os, argparse
parser = argparse.ArgumentParser(description='Generates an mkv chapter file from an avs.')
parser.add_argument('-i', '--input', required=True, help='input avs file', nargs=1, action='store', metavar='/path/to/input/file')
parser.add_argument('-o', '--output', required=True,  help='output chapters file', nargs=1, action='store', metavar='/path/to/output/file')
parser.add_argument('-f', '--fps',  help='trim fps (defaults to 23.976)', nargs=1, action='store', dest='fps', metavar='23.976/24/29.97/30/59.94/60', default='23.976', choices=['23.976', '29.97', '59.94', '24', '30', '60'])
parser.add_argument('-c', '--chapter-names',  help='Names for your chapters. default("Intro, Opening, Part A, Part B, Ending, Preview")', nargs='*', action='store', dest='cstr', metavar='"Intro, Opening, Part A, Part B, Ending, Preview"', default='Intro, Opening, Part A, Part B, Ending, Preview')
args = parser.parse_args()
inputfile = os.path.abspath(''.join(args.input))
outputfile = os.path.abspath(''.join(args.output))
with open(inputfile, 'r') as inputf:
  for line in inputf:
    if re.match('^trim\(.*', line, re.IGNORECASE):
      trim = line
if ''.join(args.fps) == '23.976':
  fps = '1001 / 24000'
elif ''.join(args.fps) == '29.97':
  fps = '1001 / 30000'
elif ''.join(args.fps) == '59.94':
  fps = '1001 / 60000'
elif ''.join(args.fps) == '24':
  fps = '1000 / 24000'
elif ''.join(args.fps) == '30':
  fps = '1000 / 30000'
elif ''.join(args.fps) == '60':
  fps = '1000 / 60000'
def f2s(frames, framerate):
  return int(frames) * eval(framerate)
def tc(seconds):
  m, s = divmod(seconds, 60)
  h, m = divmod(m, 60)
  return '{:02d}:{:02d}:{:06.3f}'.format(int(h), int(m), s)

trim_list = trim.split("+")
timecodes = []
cur_frame = 0
uid = 7492010
cstrings = ''.join(args.cstr).split(', ')
csn = 0

for tr in trim_list:
  ptn = re.compile('\d+')
  r = ptn.findall(tr)
  length = int(r[1]) - int(r[0]) + 1
  timecodes.append(tc(f2s(cur_frame, fps)))
  cur_frame += length
with open(outputfile, 'w') as chap:
  print("""<?xml version="1.0" encoding="UTF-8"?>
  <Chapters>
    <EditionEntry>
      <EditionFlagHidden>0</EditionFlagHidden>
      <EditionFlagDefault>1</EditionFlagDefault>
      <EditionUID>7492009</EditionUID>""", file=chap)
with open(outputfile, 'a') as chap:
  for timec in timecodes:
    print("""    <ChapterAtom>
      <ChapterDisplay>
        <ChapterString>{0}</ChapterString>
        <ChapterLanguage>eng</ChapterLanguage>
        <ChapterCountry>us</ChapterCountry>
      </ChapterDisplay>
      <ChapterUID>{1}</ChapterUID>
      <ChapterTimeStart>{2}</ChapterTimeStart>
      <ChapterFlagHidden>0</ChapterFlagHidden>
      <ChapterFlagEnabled>1</ChapterFlagEnabled>
    </ChapterAtom>""".format(cstrings[csn], uid, timec), file=chap)
    csn = csn + 1
    uid = uid + 1
with open(outputfile, 'a') as chap:
  print("""  </EditionEntry>
  </Chapters>""", file=chap)
