import argparse
from utils import do_this


if __name__== '__main__':


	parser = argparse.ArgumentParser()
	parser.add_argument("--name", "-n", help="set your name", required=True)
	args = parser.parse_args()

	name = args.name

	do_this(name)
