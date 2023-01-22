from data_classes import ConfigureJson
from named_tuples import Person

# Client Code
# path = 'data_dir/sample.json'
# emp = ConfigureJson(path)
# emp.add_entry()
emp1 = Person('Maricar', 'Gamay', 22, ['Java', 'C#', 'HTML/CSS', 'Javascript'])
for lang in emp1.prog_languages:
    print(f'You are a {lang} expert!')
print(emp1)



