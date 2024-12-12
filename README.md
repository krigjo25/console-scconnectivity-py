# SC Connectivity

##  Overview
This program has functions to check wheter a webpage is up and running or not
The program was created at 01.12-22 as a final project for cs50p course.
[SCConnectivity](https://www.youtube.com/watch?v=j-iIdt9iBcY)

##  Description
The Website Connectivity tool provides a few options through the command-line interface.
By default, the application will run the connectivity checks synchronosuly. In other words the app performs the checks one after another. The behavior can not be changed in this version.

###  How to
Below is a guide on how to use the prorgam.
```sh
python  app.py -h or --help                     # To view the help page
python  app.py -info or --information           # To show information about the program
python  app.py -u [arg,arg]or --urls[arg,arg]   # Provides the user one or more target URLS 
python  app.py -p or --ping                     # Ping one or more target URLs

```

- `-u` or `--urls` allows the user to provide one or more target URLs at the command line or supply a file containing a list of URLs to check.
- `-p` or `--ping` allows the user to ping a webpage or multiple webpages or a file containing webpages.
- `-help` or `--help` to view the help page.
- `-info` or `--information` allows the user to view the program's information.


## Credits

##  Notes from the developer

Project developed with love for python by @kigjo25<br>

###  Libraries used

#### [argparse      - by Thomas Waldmann](https://pypi.org/project/argparse/)
#### [pythonping    - by Alessandro Maggio](https://pypi.org/project/pythonping/)
#### [requests      - by  Kenneth Reitz](https://requests.readthedocs.io/en/latest/)
#### [sys           - by the python developer team](https://docs.python.org/3/library/sys.html)

## Licence
See LICENCE file for more details

Thanks for reading, In gloria excelsius deo
@krigjo25