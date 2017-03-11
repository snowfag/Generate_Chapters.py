# Generate_Chapters.py
Generates an mkv chapter file from an avs.

```
usage: generate_chapters.py [-h] -i /path/to/input/file -o
                            /path/to/output/file
                            [-f 23.976/24/29.97/30/59.94/60]
                            [-c ["Intro, Opening, Part A, Part B, Ending, Preview" ["Intro, Opening, Part A, Part B, Ending, Preview" ...]]]

Generates an mkv chapter file from an avs.

optional arguments:
  -h, --help            show this help message and exit
  -i /path/to/input/file, --input /path/to/input/file
                        input avs file
  -o /path/to/output/file, --output /path/to/output/file
                        output chapters file
  -f 23.976/24/29.97/30/59.94/60, --fps 23.976/24/29.97/30/59.94/60
                        trim fps (defaults to 23.976)
  -c ["Intro, Opening, Part A, Part B, Ending, Preview" ["Intro, Opening, Part A, Part B, Ending, Preview" ...]], --chapter-names ["Intro, Opening, Part A, Part B, Ending, Preview" ["Intro, Opening, Part A, Part B, Ending, Preview" ...]] Names for your chapters. default("Intro, Opening, Part A, Part B, Ending, Preview")
```
