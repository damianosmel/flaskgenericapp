import configparser
from flask import render_template

def generate_documentation():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    elements = []
    for enumeration,item in enumerate(config["Documentation"]):
        if config["Documentation"][item]:
            title,body = config["Documentation"][item].split("_-_")
            elements.append((str(enumeration),title,body))
    html_fragment = render_template("accordion_element.html",elements=elements)
    return html_fragment


def generate_static_documentation():
    return render_template("documentation.html")