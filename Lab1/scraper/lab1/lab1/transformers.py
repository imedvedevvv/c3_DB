import lxml.etree as ET


def xslt_parse():
    dom = ET.parse('outputs/zvetsad.xml')
    xslt = ET.parse('outputs/zvetsad.xslt')

    transform = ET.XSLT(xslt)
    newdom = transform(dom)

    with open('outputs/zvetsad.html', 'wb') as fileobj:
        fileobj.write(ET.tostring(newdom, pretty_print=True))


if __name__ == '__main__':
    xslt_parse()
