from __future__ import print_function
import RMF
import unittest

class Tests(unittest.TestCase):

    def test_chain(self):
        """Test the Chain decorator"""
        b = RMF.BufferHandle()
        rmf = RMF.create_rmf_buffer(b)

        rmf.add_frame('zero', RMF.FRAME)
        rt = rmf.get_root_node()

        cf = RMF.ChainFactory(rmf)
        c0 = rt.add_child("c0", RMF.REPRESENTATION)
        c1 = rt.add_child("c1", RMF.REPRESENTATION)
        c = cf.get(c0)
        # Check defaults
        self.assertEqual(c.get_chain_type(), 'UnknownChainType')
        self.assertEqual(c.get_sequence(), '')
        # Check setters
        c.set_chain_type('LPolypeptide')
        c.set_sequence('CGY')
        c.set_chain_id('X')

        # Check both const and non-const getters
        self.check_rmf(cf, c0, c1)
        self.check_rmf(RMF.ChainConstFactory(rmf), c0, c1)

    def check_rmf(self, cf, c0, c1):
        self.assertTrue(cf.get_is(c0))
        self.assertFalse(cf.get_is(c1))
        c = cf.get(c0)
        self.assertEqual(c.get_chain_type(), 'LPolypeptide')
        self.assertEqual(c.get_sequence(), 'CGY')
        self.assertEqual(c.get_chain_id(), 'X')

if __name__ == '__main__':
    unittest.main()
