import json

value_file = "Values.json"
structure_file = "TestcaseStructure.json"


def get_data(name_file):
    try:
        with open(name_file, 'r', encoding='utf-8') as f:
            string = f.read()
            string = string.replace('\t', '')
            string = string.replace('\n', '')
            string = string.replace(',}', '}')
            string = string.replace(',]', ']')
            data = json.loads(string)
            f.close()
            return data
    except FileNotFoundError:
        error_file = "error.json"
        with open(error_file, "w") as f:
            json.dump(error_file, f, indent=4, ensure_ascii=False)
            f.close()
            return None


values = get_data(value_file)
caseStructure = get_data(structure_file)


def get_value(item, value):
    try:
        for param in item["params"]:
            get_value(param, value)
    except KeyError:
        try:
            for i in item["values"]:
                if i['id'] == value['value'] and value['id'] == item['id']:
                    item['value'] = i['title']
                    return item['value']
                get_value(i, value)

        except KeyError:
            if item['id'] == value['id']:
                item['value'] = value['value']
                return item['value']


if values is not None and caseStructure is not None:
    for value in values["values"]:
        get_value(caseStructure, value)
    structureValuesFile = "StructureWithValues.json"
    with open(structureValuesFile, "w", encoding='utf-8') as write_file:
        json.dump(caseStructure, write_file, indent=4, ensure_ascii=False)
        write_file.close()
