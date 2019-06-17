import os
import _pickle as pickle

class Probe:
    """
    Holds Illumina 450k probe info for a single CpG site.
    """
    def __init__(self):
        self.id = None
        self.seq = None
        self.name = None
        self.chr = None
        self.gene = None
        self.strand = None
        self.refseq = None
        self.feature = None
        self.tour = None
        self.hg19_cord = None
        self.hg38_cord = None
        self.GDC_gene = None
        self.GDC_cgi_cord = None
        self.GDC_beta_normal =  None 
        self.GDC_beta_tumor = None 
        self.GDC_gene_type = None

class Interval:
    """
    Define a genomic interval by chromsome and strand orientation.
    """
    def __init__(self, chromosome, start, end, strand):
        self.chr = chromosome
        self.start = start
        self.end = end
        self.strand = strand

class Feature:
    """
    Define a Probe feature.
    """
    BODY = "Body"
    TSS200 = "TSS200"
    TSS1500 = "TSS1500"
    UTR5 = "5'UTR"
    UTR3 = "3'UTR"
    EXON = "Exon"

class CpG_location:
    """
    Defines a CpG location.
    """
    ISLAND = "Island"
    NSHORE = "N_Shore"
    SSHORE = "S_Shore"
    NSHELF = "N_Shelf"
    SSHELF = "S_Shelf"
    
class SNP:
    """
    Defines the SNPs in probes. Used to filter probes.
    """

    def __init__(self):
        self.probeid = None
        self.snpid = None
    
class Annotate_Methyl_450k(object):
    """
    Parse and hold information about Illumina probe and GDC Experiment.
    """

    def __init__(self, filepath):
        try:
            with open(filepath, 'rb') as f:
                self.probe = pickle.load(f)
        except (FileNotFoundError, IOError):
            pass

    def get_number(self):
        """
        Return total number of probes.
        """
        number = 0
        for probe_id in self.probe.keys():
            number += 1

        return number

    def get_probe(self, probe_id): #WORKS
        """
        Return probe info associated with an reference.
        """
        try:
            probe = self.probe[probe_id]
        except Exception as ex:
            probe = None
            print("WARNING: No probe with ref-id of %s found." % probe_id)
        return probe