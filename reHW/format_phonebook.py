import re
from info_csv import contacts_list
from pprint import pprint


def format_contacts(list_):
    my_list = [list_[0]]
    for contact in list_[1:]:
        contact1 = ','.join(contact[:3]).strip(',').replace(',', ' ').split()
        if len(contact1) == 2:
            contact1.append('')
        contact2 = ','.join(contact[3:]).split(',')
        contact1.extend(contact2)
        my_list.append(contact1)
    return my_list


def normalize_phone():
    text = format_contacts(contacts_list)
    normalize_list = [text[0]]
    for t in text[1:]:
        phone_pattern = r"(\+7|8)\s*\(*(\d{3})\)*[-.\s]*(\d{3})[-.\s]*(\d{2})[-.\s]*(\d{2})\s*\(*(доб.)*\s*(\d{4})*\)*"
        pattern_subst = r'+7(\2)\3\4\5'
        result = re.findall(phone_pattern, ','.join(t))
        if result and result[0][-1]:
            pattern_subst = r'+7(\2)\3\4\5 \6\7'
            result = re.sub(phone_pattern, pattern_subst, ','.join(t))
            normalize_list.append(result.split(','))
        else:
            result = re.sub(phone_pattern, pattern_subst, ','.join(t))
            normalize_list.append(result.split(','))
    return normalize_list


def normalize_contact():
    text = normalize_phone()
    normal_list = [text[0]]
    grouped_data = {}
    for record in text[1:]:
        lastname = record[0]
        firstname = record[1]
        key = (lastname, firstname)
        if key not in grouped_data:
            grouped_data[key] = record[:]
        else:
            for i in range(3, len(record)):
                if not grouped_data[key][i] and record[i]:
                    grouped_data[key][i] = record[i]
    normal_list.extend(list(grouped_data.values()))
    return normal_list
