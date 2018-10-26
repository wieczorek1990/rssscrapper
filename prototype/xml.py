from xml.etree import ElementTree


ns = {
    'cb': 'http://www.cbwiki.net/wiki/index.php/Specification_1.1'
}
with open('sample-rss.xml') as f:
    content = f.read()
    root = ElementTree.fromstring(content)
    print(root.findall('.//cb:exchangeRate', ns))
