import argparse
import settings
from garbler import garbler
from evaluator import evaluator

def main(args):
	if args.garbler:
		garbler(args)
	elif args.evaluator:
		evaluator(args)

def sanitize_inputs(parser):
	args = parser.parse_args()
	if not args.garbler and not args.evaluator:
		parser.error('Either -g or -e needs to be set.')
	if args.garbler and args.evaluator:
		parser.error('Can not be both garbler and evaluator!')
	if args.garbler and not args.circuit:
		parser.error('The garbler needs to supply the circuit file.')
	if args.bits and not args.identifiers:
		parser.error('-i must be supplied along -b')
	if args.identifiers and not args.bits:
		parser.error('-b must be supplied along -i')
	if args.identifiers and args.bits:
		if len(args.identifiers) != len(args.bits):
			parser.error('Must supply the same number of bits as identifiers')

def sanitize_optimizations(parser):
	args = parser.parse_args()
	if args.classical:
		if any([args.point_and_permute, args.grr3, args.free_xor, args.grr2, args.flexor, args.half_gates]):
			parser.error('Classical garbled circuits is not compatible with any optimization.')
	if args.free_xor and args.grr2:
		parser.error('FreeXOR is not compatible with GRR2.')
	if args.free_xor and args.flexor:
		parser.error('FreeXOR is not compatible with FleXOR.')
	if args.grr3 and args.grr2:
		parser.error('GRR3 is not compatible with GRR2.')
	if args.grr2 and args.half_gates:
		parser.error('GRR2 is not compatible with half gates.')
	if args.flexor and args.half_gates:
		parser.error('FleXOR is not compatible with half gates.')

	settings.CLASSICAL = args.classical
	settings.POINT_AND_PERMUTE = args.point_and_permute
	settings.GRR3 = args.grr3
	settings.FREE_XOR = args.free_xor
	settings.GRR2 = args.grr2
	settings.FLEXOR = args.flexor
	settings.HALF_GATES = args.half_gates


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Program to garble and evaluate a circuit.',
									 epilog='Example usage: gabes -g -c Desktop/test.circuit -a 192.08.12.33:1932 -i A B H -b 001')

	# General options
	parser.add_argument('-g', '--garbler', action='store_true', help="Set this flag to become the garbler")
	parser.add_argument('-e', '--evaluator', action='store_true', help="Set this flag to become the evaluator")
	parser.add_argument('-b', '--bits', metavar="bits", help="Include your private input bitstring to the circuit (e.g. 001011)")
	parser.add_argument('-i', '--identifiers', nargs='+', metavar="identifier", help="Indicate which input wires you supply to the circuit (e.g. -i A C D)")
	parser.add_argument('-c', '--circuit', metavar="file", help="Path of the file representing the circuit. Only the garbler needs to supply the file")
	parser.add_argument('-a', '--address', metavar="ip:port", help="IP address followed by the port number", required=True)

	# Optimization options
	parser.add_argument('-cl', '--classical', action='store_true', help="Set this flag for classical garbled circuits")
	parser.add_argument('-pp', '--point-and-permute', action='store_true', help="Set this flag to include point-and-permute")
	parser.add_argument('-grr3', '--grr3', action='store_true', help="Set this flag for GRR3 garbled circuits")
	parser.add_argument('-free', '--free-xor', action='store_true', help="Set this flag for free-xor garbled circuits")
	parser.add_argument('-grr2', '--grr2', action='store_true', help="Set this flag for GRR2 garbled circuits")
	parser.add_argument('-fle', '--flexor', action='store_true', help="Set this flag for flexor garbled circuits")
	parser.add_argument('-half', '--half-gates', action='store_true', help="Set this flag for half gates garbled circuits")

	sanitize_inputs(parser)
	sanitize_optimizations(parser)
	args = parser.parse_args()
	main(args)