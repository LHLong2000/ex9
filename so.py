import sys
from stackapi import StackAPI


def get_top_q_label(n, tag):
    site = StackAPI('stackoverflow')
    questions = site.fetch('questions', sort='votes', tagged=tag)

    list_q = questions['items']

    top_q = [list_q[0]]
    for i in list_q[:n]:
        if i['score'] > top_q[0]['score']:
            top_q = i
    print(top_q[0]['title'], top_q[0]['link'])


def main():
    get_top_q_label(int(sys.argv[1]), sys.argv[2])
    # get_top_q_label(3, 'label')


if __name__ == '__main__':
    main()
