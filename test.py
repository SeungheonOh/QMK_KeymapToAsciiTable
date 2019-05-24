# ipt = open('Dictionary.txt', 'r')
# ipt = ipt.readlines()

# file = open('NDic.txt', 'w')
# file.write('\n')

# for line in ipt:
#     line = line.replace('\n', '')
#     line = line.replace('\\', '')
#     line = line.replace(' ', '')
#     if line[0] == '#':
#         print(file=file)
#         print("    {0}".format(line), file=file)
#         continue
#     line = line.replace(',', '')
#     line = line.replace('"', '')
#     line = line.split(':')

#     print("    \"{0}\"".format(line[0])+":"+"\"{0}\"".format(line[1])+",", file=file)

keymap = [["q","w","e","r","t","a"],["qf","w","e","r","t","a"],["qd","w","e","r","t","a"],["qs","w","e","r","t","a"]]

with open("KeyboardLayout.json", "w") as file:
    print("{", file= file)
    for row in keymap:
        print("\"{0}\": ".format(keymap.index(row)),file=file)
        print("{",file=file)

        for key in row:
            print("\"{0}\": 1".format(key),file=file, end='')
            if row.index(key) != len(row)-1:
                print(',',file=file, end='')
            print(file=file)
        print("}",file=file, end='')
        if keymap.index(row) != len(keymap)-1:
            print(',',file=file, end='')
        print(file=file)
    print("}", file= file)
    