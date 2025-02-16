#   Importing Python responsories
import sys
import requests as r

#   Importing responsories
from pythonping import ping
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, ArgumentError

class CommandlineInterface():

    '''
        The command line Interface
    '''

    def CommandLineOptions(self):

        '''Constructing the argparser'''
        #   Creating a argumentParser
        parser  = ArgumentParser(prog = 'Site Connectivity Checker', formatter_class= ArgumentDefaultsHelpFormatter, description= 'Site Connectivity Checker', epilog= 'by @krigjo25')

        #   Initializing command line arguments
        try :
            parser.add_argument('-p', '--ping', dest = 'ping', metavar = 'Ping', help ='Ping a website', nargs='+', default=[], type= str)
            parser.add_argument('-u', '--urls', dest = 'urls', metavar = 'URLs', nargs='+', default=[], type= str, help ='urls to check')
            parser.add_argument('-info', '--information', dest = 'info', help = '%(prog)s Information Center', action='store_true')

        #   Parsing through the arguments
            arg = parser.parse_args(sys.argv[1:])
        except (ArgumentError, Exception) as e: print(e)
        return arg

class SCChecker():

    '''
        Program Name : SiteConnectivity Checker
        Description : Checks site connectivity

        Developed by : @ krigjo25
        date :
    '''

    def ProgramInformation(self):

        '''
            #   Program information
            #   Program name, version, description

        '''

        name = 'Site Connectivity Checker'
        version = '0.0.1'


        description = '''Checking connection for websites'''
        return sys.exit(f'Program name : {name}\nDescription : {description}\nVersion : {version}')

    def PingConnection(self, urls):

        '''
        Ping a internett connection

        #   Ping through a list of websites
        #   Ping through given links of websites

        '''

        try:

            for i in urls:

                if str(i).endswith('.txt'):

                    with open(i, 'r') as f:

                        arg = f.read().split(' ')

                        for i in arg:
                            print(f'\nping {i}')
                            ping(i, verbose=True, interval= 1, timeout=5)

                else:
                    print(f'Pings {i}')
                    ping(i, verbose=True, interval= 1, timeout=5)

        except Exception as e: sys.exit(e)

        return

    def UrlParse(self, arg):

        '''

            #   Parse through txt file
            #   Parse through given links

        '''

        http = "https://"
        #   Opening up the document
        try :

            #  Reading documents
            for i in arg:

                #   Ensure the file is a text file
                if str(i).endswith('.txt'):

                    #   Open the file
                    with open(i, 'r') as f:

                        arg = f.read().strip(' ').split(' ')

                        #   Parse through the links
                        for i in arg:

                            #   Ensure the link is a valid link
                            if http not in i: i = f'{http}{i}'.replace(' ', '')

                            #   Send a request to the website
                            req = r.get(i, timeout=5)

                            # Ensures the status code is 200
                            if req.status_code == 200: print(f'{req.url} \U0001F44D')
                            else: print(f'{req.url} is \U0001F4F4')

                            req.close()

                else:
                    #  Ensure the link is a valid link
                    if http not in i: i = f'{http}{i}'.replace(' ', '')

                    #   Send a request to the website
                    req = r.get(i, timeout=5)
                    if req.status_code == 200: print(f'{req.url} \U0001F44D')
                    else: print(f'{req.url} \U0001F4F4')

                    req.close()

        except Exception as e:
            print(f'{i} \U0001F4F4')

    def main(self):

        arg = CommandlineInterface().CommandLineOptions()

        try:

            if arg.info : return self.ProgramInformation()
            elif arg.ping: return self.PingConnection(arg.ping)
            elif arg.urls: return self.UrlParse(arg.urls)

        except Exception as e: sys.exit(e)


if __name__ == '__main__':
    rp = SCChecker()
    rp.main()
