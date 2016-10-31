#!/usr/bin/python

import argparse
import operator
import re


def read_file(f_name):
    """
    """
    all_words = []
    st_check = ("%", r"\begin{", r"\document", r"\use", r"\newco", r"\renew")
    not_word = (
        "texttt", "textbf", "emph", "hline", "citet", "citep", "simeq", "www")
    with open(f_name) as f:
        data = f.read()
        for line in data.splitlines():
            if not line.startswith(st_check) and line != '':
                l_words = re.findall(r"[\w']+", line)
                for word in l_words:
                    word = word.lower().strip(r"""'.,;()[]{}:@""")
                    if re.match(r'\w', word) and not num_there(word):
                        if len(word) == 1 and word == 'a':
                            all_words.append(word)
                        elif len(word) > 1 and word not in not_word:
                            all_words.append(word)
    return all_words


def num_there(s):
    """
    http://stackoverflow.com/a/19859340/1391441
    """
    return any(i.isdigit() for i in s)


def count_words(all_words):
    """
    """
    wordcount = {}
    for word in all_words:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount


def lenght_dist(wordcount):
    """
    """
    lenghts = [0 for _ in range(15)]
    for w, val in wordcount.items():
        if len(w) < 15:
            lenghts[len(w) - 1] += val
        else:
            lenghts[14] += val
    return lenghts


def main(f_name, max_w=20):
    """
    http://stackoverflow.com/a/21108583/1391441
    """
    # Read file and split into single words.
    all_words = read_file(f_name)
    # Count unique words.
    wordcount = count_words(all_words)

    # Reverse, put most used words on top.
    w_sort = sorted(wordcount.items(), key=operator.itemgetter(1),
                    reverse=True)
    # Count total number of words.
    w_sum = 0
    for w in w_sort:
        w_sum += w[1]
    print("\nNumber of unique words: {}".format(len(w_sort)))
    print("Total number of words: {}\n".format(w_sum))
    # Print results.
    p_sum = 0.
    for i, w in enumerate(w_sort[:max_w]):
        p = w[1] / float(w_sum) * 100.
        p_sum += p
        print("{:3d}. {:5d}     ({:3.2f}%) - {}".format(i, w[1], p, w[0]))
    print("Sum percentage: {:.1f}%\n".format(p_sum))

    print("Word lengths distribution:")
    lenghts = lenght_dist(wordcount)
    l_max = max(lenghts)
    for i, le in enumerate(lenghts):
        l_p = max(1, int(round(le * 30. / l_max)))
        print("{:2d}  ".format(i + 1) + "+" * l_p + " ({})".format(le))


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
