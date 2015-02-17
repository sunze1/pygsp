#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test suite for the modulename module of the pygsp package.
"""

import sys
import numpy as np
import scipy as sp
import numpy.testing as nptest
from scipy import sparse
from pygsp import utils, graphs

# Use the unittest2 backport on Python 2.6 to profit from the new features.
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class FunctionsTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_utils(self):

<<<<<<< HEAD
=======
        W = np.arange(64).reshape((8,8))
        W = sparse.lil_matrix(W)
        G = graphs.Graph(W, directed=False)
        # TODO choose values
        x = None
        y = None

>>>>>>> default_graphs
        def test_is_directed(G):
            self.assertFalse(utils.is_directed(G))

        def test_estimate_lmax(G):
            # TODO test with matlab
            mat_answser = None
            self.assertEqual(utils.estimate_lmax(G), mat_answser)

        def test_check_weights(W):
<<<<<<< HEAD
            pass
=======
            mat_answser = [False, False, False, True]
            self.assertEqual(utils.check_weights(W), mat_answser)
>>>>>>> default_graphs

        def test_create_laplacian(G):
            mat_answser = None
            self.assertEqual(utils.create_laplacian(G), mat_answser)

        def test_check_connectivity(G, **kwargs):
            self.assertTrue(utils.check_connectivity(G))

        def test_distanz(x, y):
            # TODO test with matlab
            mat_answser = None
            self.assertEqual(utils.distanz(x, y))

        # Doesn't work bc of python bug
        # test_is_directed(G)
        test_estimate_lmax(W)
        test_check_weights(W)
        test_create_laplacian(G)
        test_check_connectivity(G, **kwargs)
        test_distanz(x,y)

    def test_dummy(self):
        """
        Dummy test.
        """
        a = np.array([1, 2])
        b = utils.dummy(1, a, True)
        nptest.assert_almost_equal(a, b)


suite = unittest.TestLoader().loadTestsFromTestCase(FunctionsTestCase)


def run():
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    run()