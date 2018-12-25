from abc import ABC, abstractmethod

import numpy as np


class Node(ABC):
    """
    This should be the abstract class that is a "node"
    in a chromosome. For example, in a module
    chromosome, this would represent a layer in an NN.
    In a blueprint chromosome, this would represent which
    module is being pointed to.
    """

    HISTORICAL_MARKER = 1

    def __init__(self):
        # Save what this Node should be marked as
        self._marker = Node.HISTORICAL_MARKER

        # Update the marker count
        Node.HISTORICAL_MARKER += 1

    def _bit_flip_mutation(self, value):
        """
        A simple Node mutation that just flips whichever
        boolean value to the opposite
        :param value: The value to be flipped, bool
        :return: The new value, bool
        """
        return not value

    def _gaussian_mutation(self, mean=0.0, std_dev=1.0):
        """
        Draws a real-valued number from a Gaussian distribution
        :param mean: The mean value (middle value)
        :param std_dev: The scale of the Gaussian (standard dev)
        :return: A random value drawn from the normal distribution
        """
        return np.random.normal(loc=mean, scale=std_dev)

    def _uniform_mutation(self, lower=-1.0, upper=1.0):
        """
        Draws a real-valued number from a uniform distribution
        :param lower: The lower bound for the distribution
        :param upper: The upper bound for the distribution
        :return: A random value drawn from the uniform distribution
        """
        return np.random.uniform(lower, upper)


class Chromosome(ABC):
    """
    This should be the abstract class that is a chromosome.
    Both module and blueprint chromosomes should inherit from
    this class.
    """
    pass


