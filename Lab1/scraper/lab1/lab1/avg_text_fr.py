import xml.etree.ElementTree as ET

def text_count(page):
    counter = 0
    for element in page:
        if(element.attrib['type'] == 'text'):
            counter += 1

    return counter

def display_links():
    mytree = ET.parse('outputs/uahotels.xml')
    myroot = mytree.getroot()
    overall_text_elements = 0

    for page in myroot:
        page_elements = text_count(page)
        overall_text_elements += page_elements
        
    mid_text_elements = overall_text_elements/20
    print(round(mid_text_elements))

       

display_links()

