with open('text_3.txt', 'r', encoding='utf-8') as my_file:
    salary = []
    small = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            small.append(i[0])
        salary.append(i[1])
print(f'Salary less than 20.000 {small}, normal salary {sum(map(float, salary)) / len(salary)}')
#+