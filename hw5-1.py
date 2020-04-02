my_file = open('text.txt', 'w', encoding='utf-8')
line = input('Enter some text')
while line:
    #https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
    my_file.writelines(line + '\n')
    line = input('Enter some text')
    #https://ru.stackoverflow.com/questions/600671/%D0%97%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D1%86%D0%B8%D0%BA%D0%BB%D0%B0-%D0%BF%D1%80%D0%B8-%D0%B2%D0%B2%D0%BE%D0%B4%D0%B5-%D0%BF%D1%83%D1%81%D1%82%D0%BE%D0%B9-%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8-python
    if not line:
        break

my_file.close()
my_file = open('text.txt', 'r', encoding='utf-8')
content = my_file.readlines()
print(content)
my_file.close()
#+