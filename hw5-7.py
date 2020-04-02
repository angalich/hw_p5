import json

profit = {}
a_p = {}
prof = 0
average_profit = 0
i = 0
with open('text_7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        firm, form, revenue, costs = line.split()
        profit[firm] = int(revenue) - int(costs)
        #https://stackoverflow.com/questions/3483520/use-cases-for-the-setdefault-dict-method
        if profit.setdefault(firm) >= 0:
            prof = prof + profit.setdefault(firm)
            i += 1
    if i != 0:
        average_profit = prof / i
        print(f'Прибыль средняя - {average_profit:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все компании работают в убыток')

    a_p = {'average_profit': round(average_profit)}
    print(f'Прибыль каждой компании - {profit}')

with open('text_7.json', 'w', encoding='utf-8') as write_js:
    # https://legkovopros.ru/questions/2830/soxranenie-znachenij-jz-on-v-tekstovy-j-fajl-dublikat
    js_str = json.dumps(profit, indent=4, ensure_ascii=False)
    js_str2 = json.dumps(a_p, indent=4, ensure_ascii=False)
    write_js.write(js_str + ',' + '\n')
    write_js.write(js_str2)
    print(f'Создан файл с расширением json со следующим содержимым: \n ' f' {js_str}, \n {js_str2}')
#+