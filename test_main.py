import os
import pytest
from utils import do_this

def test_do_this():

    name = 'abc'
    do_this(name)

    assert os.path.isfile('./static/images/datamatrix_test_'+name+'.png')
