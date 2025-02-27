import IMP.test
import sys
import os
import re


class EM3DDockApplicationTest(IMP.test.ApplicationTestCase):

    def test_simple(self):
        """Simple test of EM3D single PDB score application"""
        p = self.run_application('em3d_single_score',
                                 ['-r', '4.0', '-d', '1.0',
                                  self.get_input_file_name('mini.pdb'),
                                  self.get_input_file_name('mini-4.0.mrc')])
        out, err = p.communicate()
        sys.stderr.write(err)
        self.assertApplicationExitedCleanly(p.returncode, err)

        m = re.search('Best\s+score\s+=\s+-([\d\.]+)\r?', err)
        self.assertIsNotNone(m, msg="Score output not found in " + str(err))
        self.assertAlmostEqual(float(m.group(1)), 0.13, delta=0.02)

        os.unlink('em_fit_mini.res')
        os.unlink('em_fit_mini.pdb')

    def test_simple_score(self):
        """Simple test of EM3D score application"""
        p = self.run_application('em3d_score',
                                 [self.get_input_file_name('2p4e.pdb'),
                                  self.get_input_file_name('fab.pdb'),
                                  self.get_input_file_name('transforms10'),
                                  self.get_input_file_name('complex.mrc')])

        out, err = p.communicate()
        sys.stderr.write(err)
        self.assertApplicationExitedCleanly(p.returncode, err)

        # count the number of lines in output file
        fin = open('em3d_score.res', 'r')
        text = fin.read()
        fin.close()
        number_of_lines = text.count('\n')
        self.assertEqual(number_of_lines, 13)
        os.unlink('em3d_score.res')

if __name__ == '__main__':
    IMP.test.main()
