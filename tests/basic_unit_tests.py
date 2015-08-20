"""Do some basic tests."""

import unittest

class TestBasics(unittest.TestCase):
    """Test the basics of the jicgeometry package."""

    def test_import_package(self):
        # This throws an error if the module cannot be imported.
        import jicgeometry

    def test_version(self):
        import jicgeometry
        self.assertTrue(isinstance(jicgeometry.__version__, str))


