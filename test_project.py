#   Importing responsories
import argparse
import pytest


#   Importing the test subject
from project import CommandlineInterface, SCChecker

class TestParser():
    '''
    Class to test the argument parser functionality.
    '''

    def Setup(self, cmd):
        '''
        Set up the argument parser with the given command line arguments.
        
        Args:
            cmd (list): List of command line arguments.
        
        Returns:
            Namespace: Parsed arguments.
        '''
        #   Creating a parser
        parser  = argparse.ArgumentParser(prog = 'Site Connectivity Checker', formatter_class= argparse.ArgumentDefaultsHelpFormatter, description= 'Site Connectivity Checker', epilog= 'by @krigjo25')

        #   Initializing command line arguments
        parser.add_argument('-p', '--ping', dest = 'ping', help ='Ping a website', action = 'append')
        parser.add_argument('-u', '--urls', dest = 'urls', metavar = 'URLs', nargs='+', default=[], type= str, help ='urls to check')
        parser.add_argument('-info', '--information', dest = 'info', help = '%(prog)s Information Center', action='store_true')

        return parser.parse_args(cmd)

    def test_parser(self):
        '''
        Test various command line argument combinations to ensure the parser works correctly.
        '''
        #   Strings to be tested
        url = 'www.cs50.harvard.edu/'
        urls = ['www.vg.no', 'smp.no']
        path = 'test.txt'

        #   Testing commands

        assert self.Setup(['-info'])
        assert self.Setup(['-p', url])
        assert self.Setup(['-u', url])
        assert self.Setup(['-u', urls])
        assert self.Setup(['-u', path])
        assert self.Setup(['-p', path])

        assert self.Setup(['--ping', url])
        assert self.Setup(['--urls', url])
        assert self.Setup(['--ping', path])
        assert self.Setup(['--urls', urls])
        assert self.Setup(['--urls', path])
        assert self.Setup(['--information'])

        return

    def test_RaiseSystemExit(self):
        '''
        Test that the parser raises a SystemExit exception when the help flag is used.
        '''
        with pytest.raises(SystemExit):
            self.Setup(['--help'])

        return


class TestProject:
    '''
    Class to test the functionality of the SCChecker project.
    '''

    def test_PingConnection(self):
        '''
        Test the PingConnection method with various inputs.
        '''
        url = ['google.com']
        urls = ['google.com', 'www.pypi.org']
        path = ['test.txt']
        paths = ['demo.txt', 'test.txt']

        p = SCChecker()

        p.PingConnection(url)
        p.PingConnection(urls)
        p.PingConnection(path)
        p.PingConnection(paths)

        return

    def test_UrlConnection(self):
        '''
        Test the UrlParse method with various inputs.
        '''
        url = ['google.com']
        urls = ['google.com', 'www.pypi.org']
        path = ['test.txt']
        paths = ['demo.txt', 'test.txt']

        p = SCChecker()

        p.UrlParse(url)
        p.UrlParse(urls)
        p.UrlParse(path)
        p.UrlParse(paths)

        return