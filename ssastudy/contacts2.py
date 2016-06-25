def main():
    contacts = []
    with open("C:\_code\ssastudy\contacts.txt",'r') as f:
        for line in f:
            contacts.append(line)


    chunks = []
    for c in contacts:
        newline = []
        pieces = c.split(',')
        #manipulate first argument
        i = pieces.shift
        #clean
        newline.append(i)
        i = pieces.shift
        #clean
        newline.append(i)
        i = pieces.shift
        #clean
        newline.append(i)

        chunks.append(newline)


        chunks.append([i.strip() for i in c.split(',')])
    for chunk in chunks:
        print(chunk)    

    names = []
    for n in chunks:
        names.append([i.strip() for i in n.split('\s')])
    for n in chunks:
        print(n)

            
if __name__ == "__main__":
    main()

