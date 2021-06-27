import argparse
from pystrich.datamatrix import DataMatrixEncoder
from secret import SECRET
import json

def do_this(name):

    print(f'Hello {name}')

    encoder = DataMatrixEncoder(name)
    encoder.save('./static/images/datamatrix_test_'+name+'.png')
    print(encoder.get_ascii())

    print('your secret is:',SECRET)

    print('Docker auto build and auto push to Docker Hub added!!')

    print('CI/CD workflow added!!')

    # output = '{"output":"Hi, "'+name+'"}'
    # print(json.dumps(output))
