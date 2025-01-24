# SC Connectivity
This project is a Site Connectivity Checker that provide users the ability to check the connectivity status of websites by pinging them or parsing their URLs.

The project has been developed as the final project assignment for CS50P course
Please be aware, and respect the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/).
A demo for the console application can be watched at [Youtube : SC Connectivity](https://www.youtube.com/watch?v=j-iIdt9iBcY)

## Features
- Ping a website to check its connectivity.
- Parse URLs to check their validity.
- Command line interface for easy usage.

## Installation
1. Clone the repository:
```sh
# Using SSh 
ssh git@github.com:krigjo25/console-scconnectivity-py.git

# Using git bash
git clone https://github.com/krigjo25/console-scconnectivity-py.git

# Using Github Cli
gh repo clone console-scconnectivity-py
```

2. Navigate to the project directory
```sh
cd console-scconnectivity-py
```

3. Install the requirements
```sh
pip install -r requirements.txt
```

4. Run the file
```sh
python app.py
```

## Usage
To use the Site Connectivity Checker, run the following command:

```sh
python project.py [options]
```

### Options
- `-p`, `--ping`: Ping a website.
- `-u`, `--urls`: URLs to check.
- `-info`, `--information`: Display information about the program.

Example:
```sh
python project.py -p <google.com>
python project.py -u <google.com www.pypi.org>
```
Change the `<google.com>` or `<google.com www.pypi.org>` with desired webpage, and run the program.

## Tests
To run the tests, use the following command:

```sh
USEAGE : Type in your terminal pytest <strong>testing/</strong> In order to test the whole dictionary

USEAGE : Type in your terminal pytest <strong>test_intgame -s</strong> to see a more detailed test.

USEAGE : Type in your terminal pytest <strong>test_intgame -k "classname"</strong>, in order to test the classes
USEAGE : Type in your terminal pytest <strong>pytest --html=report.htm</strong>
```


## Credits

###  Libraries used
#### [argparse      - by Thomas Waldmann](https://pypi.org/project/argparse/)
#### [pythonping    - by Alessandro Maggio](https://pypi.org/project/pythonping/)
#### [requests      - by  Kenneth Reitz](https://requests.readthedocs.io/en/latest/)


## License
This project is licensed under [The Unlicense](./LICENCE).

## Notes from the developer
Created with love, for python programming,

Thanks for reading, and have a blessed day,<br>
@krigjo25


