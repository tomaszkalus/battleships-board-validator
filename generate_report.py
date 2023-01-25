from string import Template
import os
import datetime

data = []
number_of_files = 0
valid = 0

for fname in os.listdir('in'):
    if fname.endswith('txt'):
        entry = {}
        try:
            with open(os.path.join('in',fname), 'r') as in_file:
                with open(os.path.join('out',fname), 'r') as out_file:
                    entry['name'] = fname
                    entry['in'] = in_file.read().replace('\n', '<br>')
                    entry['out'] = out_file.read()
                    number_of_files += 1

            data.append(entry)

        except OSError:
            pass
                
table = ""
for entry in data:
    row = "<tr>"
    row += f'<td>{entry["name"]}</td>'
    row += f'<td class="board">{entry["in"]}</td>'
    if entry["out"].startswith("True"):
        row += f'<td class="{"true"}">{entry["out"]}</td>'
        valid += 1
    else:
        row += f'<td class="false">{entry["out"]}</td>'
    row += "</tr>"
    table += row


today = str(datetime.date.today())

d = {
    'date': today,
    'output': table,
    'no_files': str(number_of_files),
    'valid': str(valid)
}

filename = 'raport_' + today
filename_suffix = 1
if os.path.exists(filename + '.html'):
    while os.path.exists(filename + '_' + str(filename_suffix) + '.html'):
        filename_suffix += 1
    filename += '_' + str(filename_suffix)

with open('report_template.html', 'r') as f:
    src = Template(f.read())
    result = src.substitute(d)
    
    with open(filename + '.html', 'w') as fout:
        fout.write(result)

    print(filename + '.html')