import argparse
from pystrich.datamatrix import DataMatrixEncoder
from secret import SECRET

def do_this(name):

    print(f'Hello {name}')

    encoder = DataMatrixEncoder(name)
    encoder.save('./datamatrix_test_'+name+'.png')
    print(encoder.get_ascii())

    print('your secret is:',SECRET)

    print('Docker auto build and auto push to Docker Hub added!!')

    print('CI/CD workflow added!!')


if __name__== '__main__':


	parser = argparse.ArgumentParser()
	parser.add_argument("--name", "-n", help="set your name", required=True)
	args = parser.parse_args()

	name = args.name

	do_this(name)
