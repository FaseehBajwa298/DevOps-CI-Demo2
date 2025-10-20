#!/usr/bin/env python3
import unittest
import sys
from io import StringIO
from hello import main


class TestHello(unittest.TestCase):
    
    def setUp(self):
        """Capture stdout for testing print statements"""
        self.held, sys.stdout = sys.stdout, StringIO()
    
    def tearDown(self):
        """Restore stdout"""
        sys.stdout = self.held
    
    def test_default_greeting(self):
        """Test default greeting without arguments"""
        # Mock sys.argv to have no arguments
        original_argv = sys.argv
        sys.argv = ['hello.py']
        
        try:
            main()
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "Hello, DevOps-CI-Demo2! Feature update is live.")
        finally:
            sys.argv = original_argv
    
    def test_custom_name_greeting(self):
        """Test greeting with custom name argument"""
        # Mock sys.argv with a name argument
        original_argv = sys.argv
        sys.argv = ['hello.py', 'Alice']
        
        try:
            main()
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "Hello, Alice! Feature update is live.")
        finally:
            sys.argv = original_argv
    
    def test_ci_greeting(self):
        """Test greeting specifically for CI"""
        original_argv = sys.argv
        sys.argv = ['hello.py', 'CI']
        
        try:
            main()
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, "Hello, CI! Feature update is live.")
        finally:
            sys.argv = original_argv


if __name__ == '__main__':
    print("Hello CI - Running unit tests!")
    unittest.main()