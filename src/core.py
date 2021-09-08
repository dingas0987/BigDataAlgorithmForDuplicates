from big_data_file_utils import *
from file_utils import *
import time

if __name__ == '__main__':
    test = 'sample_large.txt'
    test_output = 'sample_large_output.txt'
#    test = 'million word list.txt'
#    test_output = 'million word list res.txt'
    start = time.time()
    main(test, test_output)
    end = time.time()
    print(end - start)
    print("done")