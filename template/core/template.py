import os
import logging


class Template(object):

    def __init__(self, input, output):
        self.__input = input
        self.__output = output

    def run(self):
        return self.__input
