import os


class TestUtils:
    @staticmethod
    def get_relative_file(filename):
        return os.path.join(os.path.dirname(__file__), filename)
