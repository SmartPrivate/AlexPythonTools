import os
import sys


def add_style(input_ass, output_ass):
    reader = open(input_ass, 'r', encoding='utf-8')
    lines = reader.readlines()
    new_lines = []
    for line in lines:
        new_line = line
        if line.startswith('Style:'):
            new_line = 'Style: Default,STKaiti,20,&H00E0E0E0,&H0000FFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,1,1,2,1,1,5,1'
        if '\\N' in line:
            new_line = add_eng_effect(line)
            new_line = add_blur_effect(new_line)
        new_lines.append(new_line)

    if os.path.exists(output_ass):
        os.remove(output_ass)
    writer = open(output_ass, 'a', encoding='utf-8')
    writer.writelines(new_lines)
    writer.close()


def add_blur_effect(line):
    line_list = list(line)
    line_list.insert(50, '{\\blur2}')
    index = line.index('\\N')
    line_list.insert(index+1, '{\\r}')
    new_line = ''.join(line_list)
    return new_line


def add_eng_effect(line):
    index = line.index('\\N')
    line_list = list(line)
    eng_effect = '{\\fnCronos Pro Subhead\\fs14\\1c&H3CF1F3&}'
    line_list.insert(index+2, eng_effect)
    line_list.insert(-1, '{\\r}')
    new_line = ''.join(line_list)
    return new_line


input_ass = sys.argv[1]
output_ass = sys.argv[2]

add_style(input_ass=input_ass, output_ass=output_ass)
