import os


class ParseConfig:
    def __init__(self):
        pass


class Group:
    """
    Create a new Group.
    """

    def __init__(self, list_of_samples):
        pass


class Sample:
    """
    Sample data object.
    """
    def __init__(self, name=None, probes=None):
        pass


class ParseBatch:
    """
    Parse a series of data samples given a path to a folder.
    """

    def __init__(self, folder, delim="\t", beta_header=""):
        pass

    def get_samples(self):
        """
        Return all sample objects created from all files
        """
        pass


class ParseFile:
    """
    Automatically find and parse CpG groups from a supplied file.
    """

    def __init__(self, filename, delim="\t", beta_header=""):
        pass

    def get_samples(self):
        """
        Returns groups in this file.
        """
        pass

    def check_file(self, filename):
        """
        Check input filename
        """
        return os.path.isfile(os.path.abspath(filename))


def get_beta_by_id(sample):
    """
    Get beta value by id.
    """
    pass

def get_all_beta(sample):
    """
    Get all beta values.
    """
    pass


def get_beta_avg(probe_id, samples, verbose=False):
    """
    Get AVG beta values.
    """
    beta_val = []


def get_probes_avg(probe_id_list, sample):
    """
    Get AVG beta values from a list of probes
    """
    pass


def get_genes_from_probes(plist):
    """

    Get gene names and number of probes associated with each gene.
    """
    pass


def export_data(file_name, samples, probes):
    """
    Export data to data table
    """
    pass
