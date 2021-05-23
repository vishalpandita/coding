with open('xmen.txt','w+') as my_file:
    my_file.write('Beast\n')
    my_file.write('pheonix\n')
    my_file.writelines([
        'Cyclops\n',
        'Bishop\n',
        'Nightcrawler\n',
    ])
    my_file.seek(0)
    my_file.write('Morph')
    print(my_file.read())
    my_file.seek(0)
    print(my_file.read())
# my_file.close()
# my_file = open('xmen.txt','r')
# print(my_file.read())
#  my_file.close()
my_file = open('xmen.txt','r')
with my_file:
    print(my_file.readlines())
    my_file.seek(0)
    for line in my_file.readlines():
        print(line)
