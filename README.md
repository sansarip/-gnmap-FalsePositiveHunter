# FalsePositiveHunter
Have you ever wanted to get rid of those pesky ~6500  port false positives from your gnmap file?

Use this tool to sort through your gnmap file and get rid of potential false positives.

How do you run it?
Designate a number as a limit. Any host with more open ports than the limit will be either excluded from the output file, or exlusively included in the output file (-inc or -ex).

Flags:
_____________________________________________________________________________________________________________________________
-i (input file)
_____________________________________________________________________________________________________________________________
-o (output file)
_____________________________________________________________________________________________________________________________
-l (port limit)
_____________________________________________________________________________________________________________________________
-inc (include only hosts within the limit in your output file)
_____________________________________________________________________________________________________________________________
-ex (include only hosts exceeding the limit in your output file)
_____________________________________________________________________________________________________________________________
-noStat (get rid of the "status:" lines in the gnmap file
_____________________________________________________________________________________________________________________________
-i -o -l are required parameters | by default -inc is selected and -noStat is off
_____________________________________________________________________________________________________________________________
Example:
python FPH.py -i file.gnmap -l 1000 -ex -o file.gnmap
