#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse


def options():
    parser = argparse.ArgumentParser()
    return parser.parse_args()


def main():
    args = options()


if __name__ == "__main__":
    main()
