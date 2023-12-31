# В большой текстовой строке подсчитать количество встречаемых слов 
# и вернуть 10 самых частых. Не учитывать знаки препинания и регистр 
# символов. За основу возьмите любую статью из википедии или из 
# документации к языку.

LIMIT = 10
str = """Россия, или Российская Федерация — государство в Восточной Европе 
и Северной Азии. Россия — крупнейшее государство в мире, её территория в 
международно признанных границах составляет 17 098 246 км². Население страны в 
тех же границах, но включая территорию украинского Крыма, вторжение в который 
и его последующая аннексия Россией не получила международного признания, 
составляет 146 447 424 чел. (2023; 9-е место в мире). Столица — Москва. 
Государственный язык на всей территории страны — русский, в ряде регионов 
России также установлены свои государственные и официальные языки. Денежная 
единица — российский рубль. Россия — многонациональное государство с широким 
этнокультурным многообразием. Согласно результатам переписей населения России 
2010 года, а также Крыма и Севастополя 2014 года в стране живут представители 
свыше 190 национальностей, среди которых русские составляют свыше 80%, а русским 
языком владеют свыше 99,4% россиян. Большая часть населения (около 75%) в 
религиозном отношении относит себя к православию, что делает Россию страной с 
самым многочисленным православным населением в мире."""

def common(text: str) -> list[str]:
    dict_counts = {}
    new_sorted_dict = {}

    new_text = text.replace(',', '').replace('.', ''). \
        replace('"', '').replace('«', '').replace('»', ''). \
        replace('(', '').replace(')', ''). \
        replace('[', '').replace(']', ''). \
        replace('{', '').replace('}', ''). \
        replace('!', '').replace('?', ''). \
        replace(':', '').replace(';', ''). \
        replace(' —', ''). \
        lower(). \
        strip()
    words = new_text.split()

    for word in words:
        counter = words.count(word)
        dict_counts[word] = counter

    sorted_values = sorted(dict_counts.values())[::-1]

    for i in sorted_values:
        for k in dict_counts.keys():
            if dict_counts[k] == i:
                new_sorted_dict[k] = dict_counts[k]

    return list(new_sorted_dict.items())[0: LIMIT]

print(common(str))
