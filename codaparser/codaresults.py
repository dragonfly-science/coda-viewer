import os
from exceptions import BaseException, NotImplementedError
from itertools import islice
from numpy import array, float32


class CODAFormatException(BaseException):
    pass

def valid_coda_directory(directory):
    '''
    Takes a directory as an argument and ensures that it contains CODA files.
    
    Throws a CODAFormatException if the input argument does not represent a 
    valid CODA directory.
    '''
    if not os.path.isdir(directory):
        raise CODAFormatException('%s is not a directory' % directory)
    indexfile = directory + '/CODAindex.txt'
    firstchain = directory + '/CODAchain1.txt'
    required_files = [indexfile, firstchain]
    for requirement in required_files:
        if not os.path.isfile(requirement):
            raise CODAFormatException('%s does not contain a %s file' %
                                      directory, requirement)
    

class CodaResults(object):
    '''
    class that contains all the information about a CODA result set and has the 
    ability to access all the data.
    '''
    def __init__(self, result_directory):
        'takes a directory containing CODA files as input'
        valid_coda_directory(result_directory)
        self.indexpath = result_directory + '/CODAindex.txt'
        self.directory = result_directory
        self.parse_coda_index_file()
        
    def parse_coda_index_file(self):
        with open(self.indexpath) as index_file:
            tmp = [line.split() for line in index_file.readlines()]
            self.params_dict = {l[0]:{'start':l[1], 'end':l[2]} for l in tmp}
            
    @property
    def variables(self):
        return self.params_dict.keys()
        
    def get_data(self, variable, chain=1):
        if not variable in self.params_dict:
            raise CODAFormatException('%s in not a valid variable' % variable)
        # currently only support chain=1
        if chain != 1:
            raise NotImplementedError
        with open(self.directory + '/CODAchain%i.txt' % chain) as chain_file:
            pos = self.params_dict[variable]
            start = int(pos['start']) - 1 # file's line count starts at 1
            end = int(pos['end']) 
            var_iter = islice(chain_file, start, end)
            return array([float(l.split()[1]) for l in list(var_iter)], 
                         dtype=float32)
        
        
    