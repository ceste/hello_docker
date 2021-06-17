import os
import pytest
from main import do_this

def test_do_this():

    name = 'abc'
    do_this(name)

    assert os.path.isfile('datamatrix_test_'+name+'.png')
