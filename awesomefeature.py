#This file does nothing, it just has an example security issue in it

def xml_parse_noncompliant():
    from lxml import etree
    # Noncompliant: resolve_entities is not disabled
    # and is set to true by default.
    parser = etree.XMLParser()
    tree1 = etree.parse('resources/xxe.xml', parser)
