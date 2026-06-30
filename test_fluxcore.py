# test_fluxcore.py
"""
Tests for FluxCore module.
"""

import unittest
from fluxcore import FluxCore

class TestFluxCore(unittest.TestCase):
    """Test cases for FluxCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FluxCore()
        self.assertIsInstance(instance, FluxCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FluxCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
