from unittest import TestCase

from cr2tool.cr2_metadata import Cr2Metadata
from tests.test_utils import TestUtils


class TestCr2Metadata(TestCase):
    def test_exposure_bias(self):
        md = Cr2Metadata(TestUtils.get_relative_file('./data_files/img_7562.cr2'))
        self.assertEquals(md.exposure_bias(), 0)

        md = Cr2Metadata(TestUtils.get_relative_file('./data_files/img_7563.cr2'))
        self.assertEquals(md.exposure_bias(), -2)

        md = Cr2Metadata(TestUtils.get_relative_file('./data_files/img_7564.cr2'))
        self.assertEquals(md.exposure_bias(), 2)
