# SC Connectivity

This project is a Site Connectivity Checker that provide users the ability to check the connectivity status of websites by pinging them or parsing their URLs.

The project has been developed as the final project assignment for CS50P course
Please be aware, and respect the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/).
A demo for the console application can be watched at [Youtube](https://www.youtube.com/watch?v=j-iIdt9iBcY)
01.12-22

## Features

- Ping a website to check its connectivity.
- Parse URLs to check their validity.
- Command line interface for easy usage.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/krigjo25/console-scconnectivity-py.git
    ```
2. Navigate to the project directory:
    ```sh
    cd console-scconnectivity-py
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
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
python project.py -p google.com
python project.py -u google.com www.pypi.org
```

## Running Tests

To run the tests, use the following command:

```sh
pytest test_project.py
```

##  Notes from the developer

Developed with love by @kigjo25<br>

## Credits

###  Libraries used

#### [argparse      - by Thomas Waldmann](https://pypi.org/project/argparse/)
#### [pythonping    - by Alessandro Maggio](https://pypi.org/project/pythonping/)
#### [requests      - by  Kenneth Reitz](https://requests.readthedocs.io/en/latest/)
#### [sys           - by the python developer team](https://docs.python.org/3/library/sys.html)


## License

This project is licensed under [The Unlicense](./LICENCE).
For more information, please refer to <https://unlicense.org>.

