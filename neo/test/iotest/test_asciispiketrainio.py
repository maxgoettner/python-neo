# encoding: utf-8
"""
Tests of io.asciisignalio
"""
from __future__ import absolute_import, division

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from ...io import AsciiSpikeTrainIO
import numpy

from .common_io_test import BaseTestIO


class TestAsciiSpikeTrainIO(BaseTestIO, unittest.TestCase, ):
    ioclass = AsciiSpikeTrainIO
    files_to_download = [ 'File_ascii_spiketrain_1.txt',
                            ]
    files_to_test = files_to_download


if __name__ == "__main__":
    unittest.main()
