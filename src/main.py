#!/bin/python3

import argparse

from hr_challenges import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("challenge")
    parser.add_argument('data', metavar='N', type=int, nargs='+', help='inputs')
    args = parser.parse_args()
    print(args.challenge)
    cClass = entity_factory(args.challenge)
    challenge = cClass(len(args.data), args.data)
    challenge.evaluate()
