# LatexWordStats
Display the percentage that each single word represents in a LaTeX document.


## Usage

The `-n` argument (required) passes the document's name, and the `-m` argument (optional, default is 20) the maximum number of unique words to be displayed.

Run with:

`$ python LatexWordStats.py -n=document.tex -m=10`

which results in:

```
Number of unique words: 1944
Total number of words: 16536

  0.  1210     (7.32%) - the
  1.   461     (2.79%) - in
  2.   431     (2.61%) - of
  3.   317     (1.92%) - a
  4.   313     (1.89%) - and
  5.   304     (1.84%) - to
  6.   304     (1.84%) - for
  7.   241     (1.46%) - is
  8.   176     (1.06%) - then
  9.   165     (1.00%) - by
 10.   163     (0.99%) - are
 11.   159     (0.96%) - with
 12.   142     (0.86%) - this
 13.   142     (0.86%) - values
 14.   141     (0.85%) - fig
 15.   138     (0.83%) - age
 16.   134     (0.81%) - mass
 17.   133     (0.80%) - mean
 18.   128     (0.77%) - as
 19.   122     (0.74%) - those
Sum percentage: 32.2%

Word lengths distribution:
 1  ++ (317)
 2  ++++++++++++++++++++ (2602)
 3  ++++++++++++++++++++++++++++++ (3823)
 4  ++++++++++++++++++ (2342)
 5  ++++++++++++++ (1752)
 6  +++++++++++ (1348)
 7  +++++++++ (1154)
 8  ++++++++ (1071)
 9  ++++++ (787)
10  +++++ (586)
11  +++ (383)
12  + (129)
13  + (123)
14  + (36)
15  + (83)
```
