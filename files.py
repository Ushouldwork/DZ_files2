import os
folder_path = 'C:\\Users\\user\\OneDrive\\Рабочий стол\\DZ_file'
files = os.listdir(folder_path)

output_filename = 'итоговый_файл.txt'
if output_filename in files:
    files.remove(output_filename)

file_data = []

for filename in files:
    if filename.endswith('.txt'):  
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file_data.append((filename, len(lines), lines))

file_data.sort(key=lambda x: x[1])

with open(output_filename, 'w', encoding='utf-8') as output_file:
    for filename, num_lines, lines in file_data:
        output_file.write(f'{filename}\n{num_lines}\n')
        output_file.writelines(lines)
        output_file.write('\n')



