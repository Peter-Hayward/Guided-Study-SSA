def main():
    contacts = []
    with open("C:\_code\ssastudy\contacts.txt",'r') as f:
        for line in f:
            contacts.append(line)

    import re
    re_contact = re.compile("\s*([^\s,]+)\s*([^\s,]+)\s*,\s*([0-9]+)\s*,\s*([^\s,]+)")

    for c in contacts:
        m = re_contact.search(c)
        print(m.group(1,2,3,4))

if __name__ == "__main__":
    main()
