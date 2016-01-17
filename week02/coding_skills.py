import json

def read_json():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data


def skills():
    data = read_json()
    languages = {}
    for person in data['people']:
        for skill in person['skills']:
            if skill['name'] not in languages:
                languages[skill['name']] = [person['first_name'], person['last_name'], skill['level']]
            else:
                if languages[skill['name']][2] < skill['level']:
                    languages[skill['name']] = [
                        person['first_name'],
                        person['last_name'],
                        skill['level']
                    ]
    a = ''
    for language in languages:
        a += language + ' - ' + languages[language][0] + ' ' + languages[language][1] + '\n'
    return a


if __name__ == '__main__':
    print(skills())