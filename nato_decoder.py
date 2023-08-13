from nato_tree import NatoTree

def main():
    nato = NatoTree()
    with open(f'nato_message.txt') as txtfile:
        for line in txtfile:
            if line.strip()[0:1:1] == '\\':
                nato.add(line.strip()[0:2:1], line.strip()[2:])
            else:
                nato.add(line.strip()[0:1:1], line.strip()[1:])

    txtfile.close()
    # print(nato.find("victor"))
    # Ask user to input a nato alphabet character, print and save character to txt file
if __name__ == "__main__":
    main()