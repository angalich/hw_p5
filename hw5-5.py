import random

def summ():
    try:
        with open('text5.txt', 'w+', encoding='utf-8') as file_obj:
            line = []
            for i in range (0, 10):
                x = random.randint(1, 100)
                line.append(x)
            file_obj.writelines(str(line))

            print(sum(map(int, line)))
    except IOError:
        print('Error in file')
    except ValueError:
        print('Not number')
summ()
#+- space?