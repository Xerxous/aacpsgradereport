from bs4 import BeautifulSoup
import static, numpy

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def clean_up(text):
    for ch in static.DISCARD:
        text = text.replace(ch, '')
    return text

def get_info(session, tag):
    info = []
    page = session.get(static.LINK[tag]).content
    for content in BeautifulSoup(page, 'html.parser').find_all(static.TARGET_ELEMENT):
        clean = clean_up(content.get_text().encode('utf-8'))
        if len(clean):
            info.append(clean)
    info = info[static.CLIP + static.DISPLACE[tag]:]
    return [info[i:i+static.CHUNKS[tag]] for i in range(0, len(info), static.CHUNKS[tag])]

def glued(session, tag, exclude):
    info = get_info(session, tag)
    glue = []
    print(info)
    for content in info:
        for i in reversed(exclude):
            del content[i]
        for i in range(len(content)):
            if not is_ascii(content[i]):
                content[i] = 'FOREIGN'
        for i in range(len(content)):
            content[i] = content[i].split('(', 2)[0]
            if content[i] == '-':
                content[i] = 'N/A'
        content = reversed(content)
        glue.append('  ||  '.join(content))
    return glue

def assignment_details(session, tag):
    info = get_info(session, tag)
    attr = static.LABELS[static.TAGS[tag]]
    pkg = Info()
    print(attr)
    for i, content in zip(range(0, len(info)),info):
        cl = Info()
        print(content)
        for j in range(0, len(content)):
            setattr(cl, attr[j], content[j])
        setattr(pkg, content[0], cl)
    return pkg

def profile(session):
    info = get_info(session, 'INFO_GEN')[0]
    #Excluding contact information
    stu_info = info[:10]
    pkg = Info()
    for i in range(0, len(stu_info)):
        setattr(pkg, static.LABELS[5][i], stu_info[i])
    return pkg

class Info():
    def __tag__(self):
        return "xp_element"
