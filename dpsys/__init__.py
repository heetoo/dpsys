__version__ = '0.1.0'

import json
import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.absolute()
JSON_FILE_NAME = 'source_file_2.json'

json_file_path = os.path.join(BASE_DIR, JSON_FILE_NAME)

def load_json(path):
    with open(path) as json_file:
        dataset = json.load(json_file)
        return dataset    

def save_json_new_file(path, data):
    if os.path.isfile(path):
        os.remove(path)
    with open(path, 'w') as json_file:
        json.dump(data, json_file)


def main():
    dataset = load_json(json_file_path)

    watchers = dict()
    watchers_path = os.path.join(BASE_DIR, 'watchers.json')
    managers = dict()
    managers_path = os.path.join(BASE_DIR, 'managers.json')

    dataset.sort(key=lambda item: item['priority'])

    for item in dataset:
        item_name = item['name']
        item_managers = item['managers']
        item_watchers = item['watchers']

        for item_manager in item_managers:
            if not item_manager in managers:
                managers[item_manager] = []
            managers[item_manager].append(item_name)

        for item_watcher in item_watchers:
            if not item_watcher in watchers:
                watchers[item_watcher] = []
            watchers[item_watcher].append(item_name)

    save_json_new_file(watchers_path, watchers)
    save_json_new_file(managers_path, managers)


if __name__ == "__main__":
    main()