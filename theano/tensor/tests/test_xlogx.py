from theano.tensor.xlogx import xlogx

import unittest

import theano
from theano.tensor import as_tensor
import test_basic as TT

import random
import numpy.random

class T_XlogX(unittest.TestCase):
    def test0(self):
        x = as_tensor([1, 0])
        y = xlogx(x)
        f = theano.function([], [y])
        self.failUnless(numpy.all(f() == numpy.asarray([0, 0.])))
    def test1(self):
#        class Dummy(object):
#            def make_node(self, a):
#                return [xlogx(a)[:,2]]
        TT.verify_grad(self, xlogx, [numpy.random.rand(3,4)])


if __name__ == '__main__':
    unittest.main()
