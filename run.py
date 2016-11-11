#! /usr/bin/env python3

# -*- coding: utf-8 -*-

from grab import grab, process
from store import model, action
import os

entry = 'http://the-site-where-you-can-find-pony-info'
link_class = 'link-internal'
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

try:
    links = grab.get_urls(entry + '/wiki/Characters', link_class)
    for link in links:
        dump = os.path.join(os.path.curdir, data_dir, link.replace('/', '_') + '.html')
        if not os.path.exists(dump):
            url = link
            if not url.startswith('http'):
                url = entry + link
            content = grab.get_text(url, False)
            grab.dump_content(content, dump)
except:
    pass

for file in os.listdir(data_dir):
    content = grab.load_content(os.path.join(data_dir, file))
    found = process.find_content(content, 'table', 'infobox')
    for s in found:
        names = process.find_content(str(s), 'th')
        for n in names:
            name = n.replace('\n', '').replace('(', ' (').replace('  ', ' ').strip('" ')
            if 'More info' not in name:
                x = model.Creature()
                x.Name = name
                action.graph.push(x)

print(action.get_creatures())
