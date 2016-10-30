#!/usr/bin/python

import argparse
import operator
import re


def num_there(s):
    """
    http://stackoverflow.com/a/19859340/1391441
    """
    return any(i.isdigit() for i in s)


def main(f_name, max_w=20):
    """
    http://stackoverflow.com/a/21108583/1391441
    """
    with open(f_name) as f:
        wordcount = {}
        for word in f.read().split():
            word = word.lower().strip(r"""',.})]:@""")
            if re.match(r'\w', word) and not num_there(word):
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
        # Reverse, put most used words on top.
        w_sort = sorted(wordcount.items(), key=operator.itemgetter(1),
                        reverse=True)
        # Count total number of words.
        w_sum = 0
        for w in w_sort:
            w_sum += w[1]
        print("Words total: {}\n".format(w_sum))
        # Print results.
        p_sum = 0.
        for i, w in enumerate(w_sort[:max_w]):
            p = w[1] / float(w_sum) * 100.
            p_sum += p
            print("{:3d}. {:5d} ({:3.1f}%) - {}".format(i, w[1], p, w[0]))
        print("\nSum percentage: {:.1f}%".format(p_sum))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", required=True, type=str,
                        help="Name of .tex file to process.")
    parser.add_argument("-m", required=False, type=int,
                        help="Maximum number of words displayed.")
    args = parser.parse_args()
    if args.m is not None:
        main(args.n, args.m)
    else:
        main(args.n)
