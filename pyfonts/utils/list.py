import subprocess
import tqdm
from terminaltables import AsciiTable

fonts = subprocess.run(["fc-list"], capture_output=True, text=True).stdout.split("\n")


def get():
    table_data = [["utils"]]
    loader = tqdm.tqdm(total=100, desc="Search utils....", leave=False)
    fonts_filter = set()

    for font in fonts:
        fields = font.split(":")

        if len(fields) <= 2:
            fonts_filter.add(fields[0])

    for i, font in enumerate(fonts_filter):
        loader.update(i * 100 / len(fonts_filter))
        table_data.append([font.replace("/usr/share/utils/", "")])

        loader.close()

    table_data = AsciiTable(table_data)
    return table_data.table
