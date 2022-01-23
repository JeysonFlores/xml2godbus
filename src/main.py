import click
from interface import *


@click.command()
@click.option("--xml", help="A valid XML file")
def main(xml):
    """Simple program that greets NAME for a total of COUNT times."""
    if not xml:
        print("Error: You must provide an XML file")
        exit()
    try:
        iface = Interface(xml)
    except FileNotFoundError:
        print("The given file wasn't found in the path you gave")
        exit()
    except UnboundLocalError:
        print("Invalid XML file")
        exit()
    except Exception:
        print("There was an error parsing the file")
        exit()
    try:
        iface.generate_file()
    except Exception:
        print("Something went wrong saving the file")
        exit()


def start():
    main()
