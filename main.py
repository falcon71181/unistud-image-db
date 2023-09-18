import os
import requests
from jinja2 import Environment, FileSystemLoader
from concurrent.futures import ThreadPoolExecutor

URL = "https://punjab.chitkara.edu.in/Storage/Images/Student/"
INDEX_URL = f"file://{os.getcwd()}/index.html"

START = 53675
END = 53725

MAX_THREADS = 300
def scrap_image(num):
    main_url = f"{URL}{num}.jpg"
    try:
        response = requests.get(main_url)
        if response.status_code == 200:
            return num
    except requests.exceptions.RequestException:
        pass
    return -1

def create_html_page(images):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
    html_content = template.render(images=images)
    with open('index.html', 'w') as html_file:
        html_file.write(html_content)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    images = []

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [executor.submit(scrap_image, num) for num in range(START, END + 1)]
        
        clear_screen()
        print(f"Extracting images from {START} - {END}")
        
        for future in futures:
            image_value = future.result()
            if image_value != -1:
                images.append({"src": f"{URL}{image_value}.jpg", "value": image_value})

    create_html_page(images)

    print(f"Extraction completed. Open: {INDEX_URL}")

if __name__ == "__main__":
    main()
