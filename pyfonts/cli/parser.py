from pyfonts import __version__
import argparse

parser = argparse.ArgumentParser(
    prog="pyfont",
    description="",
    argument_default=argparse.SUPPRESS
)

parser.add_argument(
    "-v", "--version",
    action="version",
    version=__version__
)

parser.add_argument(
    "-ls", "--list",
    action="store",
    help=""
)
