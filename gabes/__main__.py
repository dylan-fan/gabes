if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Program to garble and evaluate a circuit.',
									 epilog='Example usage: gabes -g -c Desktop/test.circuit -a 192.08.12.33:1932')
	parser.add_argument('-g', '--garbler', action='store_true', help="Set this flag to become the garbler.")
	parser.add_argument('-e', '--evaluator', action='store_true', help="Set this flag to become the evaluator.")
	parser.add_argument('-a', '--address', metavar="ip:port", help="IP address followed by the port number.", required=True)
	parser.add_argument('-c', '--circuit', metavar="file", help="Path of the file representing the circuit.", required=True)
	args = parser.parse_args()
	if not args.garbler and not args.evaluator:
		parser.error('Either -g or -e needs to be set.')
	if args.garbler and args.evaluator:
		parser.error('Can not be both garbler and evaluator!')
	main(args)