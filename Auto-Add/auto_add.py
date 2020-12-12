import re

def add_par(input_name):
    is_math = False
    output_name = input_name.split('.')[0] + '-tmp.' + input_name.split('.')[-1] 
    math_sym_start = re.compile(r'(\$\$|\\begin\{equation\}|\\begin\{eqnarray\})')
    math_sym_end = re.compile(r'(\$\$|\\end\{equation\}|\\end\{eqnarray\})')
    overset = re.compile(r'\\overset')
    with open(input_name, 'r', encoding='utf-8') as f_in:
        with open(output_name, 'w', encoding='utf-8') as f_out:
            in_lines = f_in.readlines()
            for line in in_lines:
                if is_math:
                    if math_sym_end.search(line):
                        f_out.write(line)
                        is_math = False
                        continue
                    if overset.search(line):
                        f_out.write(line)
                        continue
                    new_line = line.replace(r'(', r' \left( ').replace(r')', r' \right) ').\
                        replace(r'[', r' \left[ ').replace(r']', r' \right] ')
                    f_out.write(new_line)
                else:
                    f_out.write(line)
                    if math_sym_start.search(line):
                        is_math = True
                        continue

def add_parallel(input_name):
    output_name = input_name.split('.')[0] + '-tmp.' + input_name.split('.')[-1]
    subed = re.compile(r'\\parallel(.+?)\\parallel') 
    repl = r'\\left\\lVert \1\\right\\rVert '
    with open(input_name, 'r', encoding='utf-8') as f_in:
        with open(output_name, 'w', encoding='utf-8') as f_out:
            content = ''.join(f_in.readlines())
            new_content = re.sub(subed, repl, content)
            f_out.write(new_content)


add_parallel('performance.tex')
