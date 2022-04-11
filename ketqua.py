import sys
import requests
import bs4


def your_lottery_number(a, b):
    global num_a
    global num_b
    num_a = a
    num_b = b
    return int(f"{a}{b}")


def check_lottery():
    r = requests.get('https://ketqua1.net')
    tree = bs4.BeautifulSoup(r.text, features="html.parser")
    node1 = tree.find("div", attrs={'id': 'rs_0_0'})

    node2 = tree.find("div", attrs={'id': 'rs_1_0'})

    node3 = tree.find("div", attrs={'id': 'rs_2_0'})
    node4 = tree.find("div", attrs={'id': 'rs_2_1'})

    node5 = tree.find("div", attrs={'id': 'rs_3_0'})
    node6 = tree.find("div", attrs={'id': 'rs_3_1'})
    node7 = tree.find("div", attrs={'id': 'rs_3_2'})
    node8 = tree.find("div", attrs={'id': 'rs_3_3'})
    node9 = tree.find("div", attrs={'id': 'rs_3_4'})
    node10 = tree.find("div", attrs={'id': 'rs_3_5'})

    node11 = tree.find("div", attrs={'id': 'rs_4_0'})
    node12 = tree.find("div", attrs={'id': 'rs_4_1'})
    node13 = tree.find("div", attrs={'id': 'rs_4_2'})
    node14 = tree.find("div", attrs={'id': 'rs_4_3'})

    node15 = tree.find("div", attrs={'id': 'rs_5_0'})
    node16 = tree.find("div", attrs={'id': 'rs_5_1'})
    node17 = tree.find("div", attrs={'id': 'rs_5_2'})
    node18 = tree.find("div", attrs={'id': 'rs_5_3'})
    node19 = tree.find("div", attrs={'id': 'rs_5_4'})
    node20 = tree.find("div", attrs={'id': 'rs_5_5'})

    node21 = tree.find("div", attrs={'id': 'rs_6_0'})
    node22 = tree.find("div", attrs={'id': 'rs_6_1'})
    node23 = tree.find("div", attrs={'id': 'rs_6_2'})

    node24 = tree.find("div", attrs={'id': 'rs_7_0'})
    node25 = tree.find("div", attrs={'id': 'rs_7_1'})
    node26 = tree.find("div", attrs={'id': 'rs_7_2'})
    node27 = tree.find("div", attrs={'id': 'rs_7_3'})

    list_prize = []
    special_prize = int(node1.text[-2:])
    first_prize = int(node2.text[-2:])
    second_prize = int(node3.text[-2:]), int(node4.text[-2:])
    third_prize = int(node5.text[-2:]), int(node6.text[-2:]), int(node7.text[-2:]), int(node8.text[-2:]), int(
        node9.text[-2:]), int(node10.text[-2:])
    fourth_prize = int(node11.text[-2:]), int(node12.text[-2:]), int(node13.text[-2:]), int(node14.text[-2:])
    fifth_prize = int(node14.text[-2:]), int(node16.text[-2:]), int(node17.text[-2:]), int(node18.text[-2:]), int(
        node19.text[-2:]), int(node20.text[-2:])
    sixth_prize = int(node21.text[-2:]), int(node22.text[-2:]), int(node23.text[-2:])
    seventh_prize = int(node24.text), int(node25.text), int(node26.text), int(node27.text)

    list_prize.append(special_prize)
    list_prize.append(first_prize)
    list_prize.extend(second_prize)
    list_prize.extend(third_prize)
    list_prize.extend(fourth_prize)
    list_prize.extend(fifth_prize)
    list_prize.extend(sixth_prize)
    list_prize.extend(seventh_prize)

    for prize in list_prize:
        if your_lottery_number(num_a, num_b) == prize:
            print("You won a prize!!")
            break
    else:
        print("Good luck next time.")
        print("Special Prize: %s " % special_prize)
        print("1st Prize: %s " % first_prize)
        print(f"2nd Prize: %s" % (second_prize,))
        print(f"3th Prize: %s" % (third_prize,))
        print(f"4th Prize: %s" % (fourth_prize,))
        print(f"5th Prize: %s" % (fifth_prize,))
        print(f"6th Prize: %s" % (sixth_prize,))
        print(f"7th Prize: %s" % (seventh_prize,))


def main():
    your_lottery_number(int(sys.argv[1]), int(sys.argv[2]))
    check_lottery()


if __name__ == '__main__':
    main()
