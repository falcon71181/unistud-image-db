from urllib.request import urlopen
import os

URL = "https://punjab.chitkara.edu.in/Storage/Images/Student/";
START = 53675
END = 53725

def scrap(num):
    value = (num - START) + 1
    percentage = (value / length) * 100

    print(f"Status: {round(percentage, 2)}%");

    main_url = URL + f"{num}.jpg"

    try:
        page = urlopen(main_url) 
        image = num
    except Exception:
        image = -1;

    return image


def main():
    image_file = open("./images.db", "w")
    length = END - START

    for num in range(START, END):
        os.system('clear')
        print(f"Extracting images from {START} - {END}")
        image = scrap(num)

        if (image != -1):
            image_file.write(f"{image} \n")

    print(f"Extration completed")
    image_file.close();


if __name__ == "__main__":
    main()

