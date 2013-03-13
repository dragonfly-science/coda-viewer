from codaparser import CodaResults, CODAFormatException
from nose.tools import ok_, eq_, assert_almost_equal, raises
import os

bad_coda_directory = "this_is_not_a_directory"
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
good_coda_directory = basedir + '/testdata/dolphins'


def test_variable_list():
    coda = CodaResults(good_coda_directory)
    ok_('tau.eta' in coda.variables)
    

def test_chain_one():
    coda = CodaResults(good_coda_directory)
    data = coda.get_data('lambda')
    assert_almost_equal(data[5], 2.11997, 5)
    assert_almost_equal(data[4999], 2.27574, 5)
    data = coda.get_data('beta.lambda[3]')
    assert_almost_equal(data[0], -7.92222, 5)
    

@raises(CODAFormatException)
def test_assert_on_bad_coda_directory():
    CodaResults(bad_coda_directory)