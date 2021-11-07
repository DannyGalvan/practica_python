DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    #list comprehension
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    #high order function
    python = list(filter(lambda worker: worker["language"] == "python", DATA))
    python = list(map(lambda worker: worker["name"],python))


    #list comprehension
    all_platzi_worker = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    #high order function
    platzi = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    platzi = list(map(lambda worker: worker["name"],platzi))


    #high order function
    children = list(filter(lambda worker: worker['age'] < 18, DATA))
    children = list(map(lambda worker: worker["name"], children))
    #list comprehension
    menores = [worker["name"] for worker in DATA if worker["age"] < 18]

    all_mayores = list(filter(lambda worker: worker["age"] > 18,DATA))

    for worker in all_mayores:
        print("Es mayor de edad" , worker["name"], "y trabaja en: ", worker["organization"])


if __name__ == "__main__":
    run()

