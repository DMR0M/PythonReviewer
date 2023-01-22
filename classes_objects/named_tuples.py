from typing import NamedTuple


class Person(NamedTuple):
    """Class data container"""
    first_name: str
    last_name: str
    age: int
    prog_languages: list


def main():
    first_name = 'Rommel Rudolf'
    last_name = 'Dela Merced'
    age = 23
    prog_langs = ['Python', 'Javascript', 'Rust']
    p1 = Person(first_name, last_name, age, prog_langs)

    # Accessing object properties
    print(p1.prog_languages)
    for lang in p1.prog_languages:
        if lang in ['Java', 'Python', 'C', 'C++', 'C#']:
            print(f'You are a {lang} expert!')


if __name__ == '__main__':
    main()


