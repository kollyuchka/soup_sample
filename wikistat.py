from bs4 import BeautifulSoup
from collections import defaultdict
import re
import os


def bridge_update(bridge,storage_end):
    for i in bridge:
        if i in storage_end:
            bridge.remove(i)
    return  bridge



def same_deleted(storage_end):
    new_storage_end = []
    for i in storage_end:
        if i not in new_storage_end:
            new_storage_end.append(i)
    return (new_storage_end)

def bridge_update(bridge,storage_end):
    for i in bridge:
        if i in storage_end:
            bridge.remove(i)
    return  bridge


def same_deleted_patch(patch):
    for key, value in patch.items():
        value=  same_deleted(value)
        patch[key]=value
    return patch

start = 'Stone_Age'
storage_end = ['Python_(programming_language)']
path = './wiki/'
bridge = os.listdir(path)
patch_item = []

def search(start,storage_end,bridge,patch_item):
    path = './wiki/'
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")
    bridge = bridge_update(bridge,storage_end)
    patch = defaultdict(list)
    current_end = []

    for file in bridge:

        with open("{}{}".format(path, file)) as data:
            links = re.findall(link_re, data.read())
            for link in links:

                if link in storage_end:
                    patch[link].append(file)
                    current_end.append(file)
                    current_end=  same_deleted(current_end)
                    patch=  same_deleted_patch(patch)
                    patch_item.append(patch)

    if start in  current_end:
        reversed_patch = []
        for i in patch_item[::-1]:
            reversed_patch.append(i)

        return reversed_patch

    else:
        return search(start,current_end,bridge,patch_item)

new = search(start,storage_end,bridge,patch_item)


def get_patch(start,patch):
    new_patch = [start]
    for item in patch:
        for key, value in item.items():
           if start in value:
            start = key
            new_patch.append(start)
    true_patch =[]
    for i in new_patch[::-1]:
        true_patch.append(i)

    return true_patch

print(get_patch(start,new))
