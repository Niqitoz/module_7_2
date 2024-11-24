def custom_write(file_name, strings):
    line_position = {}
    file = open(file_name, 'a', encoding = 'utf-8')
    line = 0
    for i in strings:
        position = file.tell()
        file.write(i + '\n')
        line +=1
        line_position[line, position] = i
    file.close()
    return line_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)





