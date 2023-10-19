from string import punctuation

input_file = 'file_folder/text.txt'
output_file = 'file_folder/output.txt'

with open(input_file, 'r') as file:
    lines = file.readlines()

output_lines = []

for i, line in enumerate(lines, 1):
    counter_of_letters = 0
    counter_of_puncts = 0

    line = line.rstrip()

    for element in line:
        if element.isalpha():
            counter_of_letters += 1
        elif element in punctuation:
            counter_of_puncts += 1

    line_info = f"Line {i}: {line} ({counter_of_letters})({counter_of_puncts})"
    output_lines.append(line_info)

    with open(output_file, 'w') as file:
        file.write('\n'.join(output_lines))
