import re
import os

command_list = [
    r'\G', r'\U', 
    r'\Tt', r'\Tit', r'\Titone',
    r'\Ttm', r'\Ttn', r'\xTtm', r'\xTtn',
    r'\Tpt', r'\Tqt', r'\Tjtau',
    r'\uit', r'\ut', r'\uiTit', r'\uiTitone',
    r'\git', r'\GiTit', r'\GiTitt', r'\GiTitone', 
    r'\GqTqt', r'\GpTpt', r'\GqTpt', r'\GpTqt',
    r'\GjTjtau', r'\GjTjttau',
    r'\gitt', r'\xiitt', r'\xtt', r'\xttone',
    r'\xittone', r'\xitt', r'\xtC', r'\xitC', r'\xitZ', 
    r'\fiTit', r'\fTit', r'\fpTpt', r'\fqTqt',
    r'\fqTpt', r'\fxt', r'\fxTt', r'\fixTt',
    r'\fixt', r'\fixtt', r'\fixttau', r'\fiTitt',
    r'\fxTttau', r'\fxttau', r'\fixtzerot', r'\fxtzerot',
    r'\xiTit', r'\xiTt', r'\xit', r'\xt',
    r'\xTit'
]

new_command_list = [
    r'\g', r'\uu', 
    r'\Tt', r'\Tit', r'\Tits',
    r'\Tonet', r'\Ttwot', r'\xTonet', r'\xTtwot',
    r'\Tpt', r'\Tqt', 
    r'\Tjtau',
    r'\uit', r'\ut', r'\uiTit', r'\uiTits',
    r'\git', r'\giTit', r'\giTittau', r'\giTits', 
    r'\gqTqt', r'\gpTpt', r'\gqTpt', r'\gpTqt',
    r'\gjTjtau', r'\gjTjtpietaupie',
    r'\gittau', r'\Xiittau', r'\xttau', r'\xttaus',
    r'\xittaus', r'\xittau', r'\xtC', r'\xitC', r'\xitzero', 
    r'\fixTitS', r'\fxTitS', 
    r'\fpxTptS', r'\fqxTqtS', r'\fqxTptS', 
    r'\fxts', r'\fxTtS', r'\fixTtS',
    r'\fixts', r'\fixtzeros', r'\fixttaus', r'\fixTittaus',
    r'\fxTttaus', r'\fxttaus', r'\fixtzerotaus', r'\fxtzerotaus',
    r'\XiTitS', r'\XiTtS', r'\Xitzeros', 
    r'\xts', r'\xTitS' 
]
# for i, a in enumerate(new_command_list):
#     for j, b in enumerate(new_command_list):
#         if i != j:
#             assert a != b
# exit(0)

for _, _, file_names in os.walk(os.getcwd()):
    pass

file_names = [file_name for file_name in file_names if file_name[-4:] == '.tex']

for file_name in file_names:
    mid_command_list = []

    with open(file_name, 'r') as f:
        content = f.read()

    for i, old_command in enumerate(command_list):
        new_command = r'\\%010d' % i
        mid_command_list.append(new_command)
        old_pat = re.compile('\\' + old_command + '(?![a-zA-Z])')
        content = old_pat.sub(new_command, content)

    for i, old_command in enumerate(mid_command_list):
        new_command = '\\' + new_command_list[i]
        old_pat = re.compile(old_command)
        content = old_pat.sub(new_command, content)

    with open(file_name, 'w') as f:
        f.write(content)
