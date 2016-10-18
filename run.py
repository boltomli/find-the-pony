from grab import grab, filter
import os

# entry = 'http://the-site-where-you-can-find-pony-info'
# link_class = 'link-internal'
data_dir = 'data'
# os.makedirs(data_dir, exist_ok=True)

# links = grab.get_urls(entry + '/wiki/Characters', link_class)
# for link in links:
#     url = link
#     if not url.startswith('http'):
#         url = entry + link
#     content = grab.get_text(url, False)
#     grab.dump_content(content, os.path.join(os.path.curdir, data_dir, link.replace('/', '_') + '.html'))

for file in os.listdir(data_dir):
    content = grab.load_content(os.path.join(data_dir, file))
    filtered = filter.filter_content(content, 'table', 'infobox')
    print(str(filtered).encode('UTF-8'))
