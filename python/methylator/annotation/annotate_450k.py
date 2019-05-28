import os

class Probe:
    """
    Holds Illumina 450k probe info for a single CpG site.
    """
    def __init__(self):
        self.id = None
        self.seq = None
        self.name = None
        self.chr = None
        self.hg19_cord = None
        self.strand = None
        self.gene = None
        self.refseq = None
        self.tour = None
        self.feature = None
        
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
    
class Annotate_450k:
    """
    Parse and hold information about Illumina probes.
    """

    def __init__(self):        
        for i in open(anno_file, mode="r"):
            self.ann = os.path.join("../../data/", i.strip("\n").strip("\r"))

        self.probe = {}
        self.__run__()

    def __run__(self):
        """
        A static function to setup the Probe classes.
        """
        for i in open(self.ann, mode="r"):
            if i.startswith("cg"):
                data = i.split(",")
                # Assign probe information.
                new_probe = Probe()
                new_probe.id = data[0]                 # ID
                new_probe.name = data[1]               # name
                new_probe.seq = data[13]               # sequence prior to bi-sulfite conv.
                new_probe.chr = str(data[11])          # chromosome
                new_probe.hg19_cord = int(data[12])    # chromosomal coordinates of the CpG.
                new_probe.strand = data[16]            # strand
                new_probe.gene = data[21].split(";")   # UCSC_RefGene_Name
                new_probe.refseq = data[22]            # UCSC_RefGene_Accession
                features = data[23].split(";")         # UCSC_RefGene_Group
                list_features = []
                for i in features:
                    if i not in list_features:
                        list_features.append(i)

                new_probe.feature = list_features

                new_probe.tour = data[25]              # Relation_to_UCSC_CpG_Island
                newcpg = {new_probe.id: new_probe}
                self.probe.update(newcpg)

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

    def remove_snp_probes(self):
        """
        Removes all SNPs associated with probes.
        """
        snp_list = []
        snp_file = open("../../data/humanmethylation450_dbsnp137.snpupdate.table.v2.sorted.txt", "r")
        for line in snp_file:
            if line.startswith("cg"):
                line = line.strip("\n").strip("\r").split("\t")
                new_snp = SNP()
                new_snp.probeid = line[0]
                new_snp.snpid = line[1]
                snp_list.append(new_snp)

        for snp in snp_list:
            self.probe.pop(snp.probeid)

anno_file = os.path.abspath("../../data/config.ini") # Illumina probe manifest. Note: This (large) file is not 
                                                     # in the repository.
# Functions to save/load dictionary objects. 

import _pickle as pickle

def save_obj(obj, name):
    print('saving ' + name + ' ...')
    with open('../../data/pickle/'+ name + '.pkl', 'wb+') as f:
        pickle.dump(obj, f)
        
def load_obj(name):
    print('loading ' + name + ' ...')
    with open('../../data/pickle/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)