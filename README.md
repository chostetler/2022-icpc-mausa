# 2022-icpc-mausa

Code for Eastern Mennonite University for ICPC Mausa 2022. Problems found here: https://mausa21.kattis.com/contests/mausa21/problems/espresso

## Running the answer checker
This test input checker runs through the sample data provided by ICPC and tests each one to see if it works. It will *not* work on Windows unless you are running it using Git Bash. I plan to make an updated version written in Python in the future.

```
sh testcode.sh <question name>
```

For example, `sh testcode.sh b` would run the test for question b

If you don't have that installed, you can also run each script manually by doing `python <program>.py < <inputfile>`. For example:
```
python a.py < sampledata/a/2.in
```