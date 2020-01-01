#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

def cube(value):
    result = value*3
    return result

def minus(value):
    result = value*3 - 2*value
    return result

def main():
    print minus(10)
    #print minus('Test')

    print cube(2)
    print cube('Hello')

if __name__ == '__main__':
    main()
