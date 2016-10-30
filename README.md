# LatexWordStats
Display the percentage that each single word represents in a LaTeX document.


## Usage

The `-n` argument (required) passes the document's name, and the `-m` argument (optional, default is 20) the maximum number of unique words to be displayed.

`$python LatexWordStats.py -n=document.tex -m=10`

which results in:

```
Words total: 16571

  0.  1417 (8.6%) - the
  1.   521 (3.1%) - of
  2.   497 (3.0%) - in
  3.   365 (2.2%) - for
  4.   357 (2.2%) - to
  5.   352 (2.1%) - a
  6.   345 (2.1%) - and
  7.   278 (1.7%) - is
  8.   208 (1.3%) - words
  9.   200 (1.2%) - are

Sum percentage: 27.4%
```
