import json

def load_candidates():
    '''open and read jsom file'''
    with open("candidates.json", "r", encoding="utf-8") as file:
        return json.load(file)

def get_all():
    '''create and return list of all candidates'''
    candidates = load_candidates()
    return candidates

def get_by_pk(pk):
    '''function to choose a candidate by his/her pk'''
    candidates_by_pk = load_candidates()
    for candidate in candidates_by_pk:
        if candidate["pk"] == pk:
            return candidate

    return "Not found"


def get_by_skill(skill):
    '''function to choose a candidate by his/her skills'''
    candidates_by_skills = load_candidates()
    result = []
    for candidate in candidates_by_skills:
        skills = candidate["skills"].lower().split(", ")
        if skill in skills:
            result.append(candidate)
    return result


