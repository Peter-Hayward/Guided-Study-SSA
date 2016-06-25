def main():
    contacts = []
    with open("C:\_code\ssastudy\contacts.txt",'r') as f:
        for line in f:
            contacts.append(line)    

    #find David
    #print(contacts)
    
    chunks = []
    for c in contacts:
        chunks.append([i.strip() for i in c.split(',')])

    #print(chunks)

    for chunk in chunks:
        if chunk[0] == "David Dirksen":
            print(chunk)

if __name__ == "__main__":
    main()

