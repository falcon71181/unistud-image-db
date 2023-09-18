# unistud-image-db

## Overview
A mini script to retrieve and display images from the university's (iykyk) database on a webpage. The valid input range for the API is currently unknown, so you can choose any range between 1 and 100,000. Hopefully, that should cover it ;)

## Usage
1. Clone this repository to your local machine.
```bash
git clone https://github.com/BugReportOnWeb/unistud-image-db.git
cd unistud-image-db
```

2. Install the dependencies
```bash
pip3 install -r requirements.txt
```

3. Change the `START` and `END` values in `main.py`.
```python
START = 53675  # Replace with your starting range value
END = 53725    # Replace with your ending range value
```

4. Run the script.
```bash
python3 main.py
```
The script will start scraping the data (if found) between the specified range.

4. Open the `index.html` file to see the result.
```bash
open index.html
```

## Dependencies
- [Jinja2 (3.1.2)](https://pypi.org/project/Jinja2/) - JA very fast and expressive template engine.
- [requests (2.31.0)](https://pypi.org/project/requests/) - Python HTTP for Humans.

## What's next?
To be honest, I'm not sure. Perhaps find a valid range for the current batch and fix the values accordingly, having it all on a server.
