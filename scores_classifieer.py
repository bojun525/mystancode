"""
file:scores_classifier
name:Gary
------------------------------
this program classifies scores into 4 categories
90up:A
80-90:B
70-80:C
Below 70:D


"""


def main():
    score=int(input('分數?'))
    if   score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    else:
        print('D')


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
