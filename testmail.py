import re
import json

file_path = input("Введите имя файла: ")

with open(file_path, encoding="utf-8") as file:
    file_data = file.read()

# print(type(file_data))

emails = file_data.split("\n")
# print(emails)

domains_dict = dict()

for mail in emails:
    match = re.split("@+", mail)
    domain = match[1]
    if domain not in domains_dict:
        domains_dict[domain] = []
    domains_dict[domain].append(mail)

print(json.dumps(domains_dict, indent=4))