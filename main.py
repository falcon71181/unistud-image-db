from urllib.request import urlopen
import os

URL = "https://punjab.chitkara.edu.in/Storage/Images/Student/";
INDEX_URL = f"file://{os.getcwd()}/index.html"

START = 53675
END = 53725
SIZE = (END - START) + 1

BOILERPLATE_START = '''<DOCKTYPE html><html><head><title>Images</title>
<link href='./style.css' rel='stylesheet' /></head><body><div class='container'>'''
BOILERPLATE_END = "<div></body></html>"

def scrap(num):
    relative_value = (num - START) + 1
    percentage = (relative_value / SIZE) * 100

    print(f"Status: {round(percentage, 2)}%");

    main_url = URL + f"{num}.jpg"

    try:
        page = urlopen(main_url) 
        image = num
    except Exception:
        image = -1;

    return image

def main():
    images_section = ""

    for num in range(START, END + 1):
        os.system('clear')
        print(f"Extracting images from {START} - {END}")

        image_value = scrap(num)

        if (image_value != -1):
            images_section += f"<img src='{URL}/{image_value}.jpg' />"

    with open("./index.html", "w") as image_file:
        image_file.write(BOILERPLATE_START + images_section + BOILERPLATE_END)

    print(f"Extration completed. Open: {INDEX_URL}")


if __name__ == "__main__":
    main()

