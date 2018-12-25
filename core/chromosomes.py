from abc import ABC, abstractmethod


class Node(ABC):
    """
    This should be the abstract class that is a "node"
    in a chromosome. For example, in a module
    chromosome, this would represent a layer in an NN.
    In a blueprint chromosome, this would represent which
    module is being pointed to.
    """
    pass


class Chromosome(ABC):
    """
    This should be the abstract class that is a chromosome.
    Both module and blueprint chromosomes should inherit from
    this class.
    """
    pass
