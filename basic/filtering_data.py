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
    # Guardo en una lista los nombres de los trabajadores que usan Python
    # Con list comprehensions
        # python_workers = [worker["name"] for worker in DATA if worker["language"] == "python"]
    # Con HOF
        # python_workers = list(filter(lambda worker: worker["language"] == "python", DATA))
        # python_workers = list(map(lambda worker: worker["name"], python_workers))
    # Lista con todos los nombres de los mayores a 18 años
    # Con List comprehensions
        # adults = [worker["name"] for worker in DATA if worker["age"] > 18]
    # Con HOF
        # adults = list(filter(lambda worker: worker["age"] > 18, DATA))
        # adults = list(map(lambda worker: worker["name"], adults))
    # Agregar una clave a cada worker que indique si son adultos
    # Se usa el pipe operator | con Python 3.9
        # old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    # Para versiones de Python anteriores a la 3.9
        # old_people = list(map(lambda worker: dict(worker, **{"old": worker["age"] > 70}), DATA))
        pass

if __name__ == "__main__":
    run()