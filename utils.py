import json


def load_candidates_from_json(path):
    """Загружает список кандидатов из файла JSON"""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def format_candidates(candidat_raw):
    result = '<pre>'
    for i in candidat_raw:
        result += (
            f'Имя кандидата - {i["name"]}\n'
            f'Позиция кандидата {i["id"]}\n'
            f'Навыки кандидата {i["skills"]}\n\n'
        )
    result += '<pre>'
    return result


def get_candidate_id(candidat_raw, candidate_id):
    for i in candidat_raw:
        if i['id'] == candidate_id:
            return i


def get_candidates_skills(candidat_raw, candidate_skill):
    result = []
    for i in candidat_raw:
        candidat_skill = i['skills'].lower().split(', ')
        if candidate_skill.lower() in candidat_skill:
            result.append(i)
    return result



# yyy = [
# {
# "id": 1,
# "name": "Adela Hendricks",
# "picture": "https://picsum.photos/200",
# "position": "Go разработчик",
# "gender": "female",
# "age": 40,
# "skills": "go, python"
# },
# {
# "id": 2,
# "name": "Adela Sheri Torres",
# "picture": "https://picsum.photos/200",
# "position": "Delphi developer",
# "gender": "female",
# "age": 26,
# "skills": "Delphi, pascal, fortran, basic"
# }
# ]
#
# ttt = get_candidates_skills(yyy, 'pascal')
# print(ttt)


def get_candidates_by_name(candidat_raw, candidate_name):
    result = []
    for i in candidat_raw:
        candidat_name = i['name']
        if candidate_name in candidat_name:
            result.append(i)
    return result

