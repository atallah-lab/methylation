# -*- coding: utf-8 -*-

import os

class Probe:
    """
    Holds Illumina 450k probe info for a single CpG site.
    """
    def __init__(self):
        self.id = None
        self. seq = None
        self.name = None
        self.chr = None
        self.cord = None
        self.strand = None
        self.gene = None
        self.refseq = None
        self.tour = None
        self.loc = None
        
class Interval:
    """
    Define a genomic interval by chromsome and strand orientation.
    """
    def __init__(self, chromosome, start, end, strand):
        self.chr = chromosome
        self.start = start
        self.end = end
        self.strand = strand

class Location:
    """
    Define a Probe location.
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
                new_probe.id = data[0]
                new_probe.name = data[1]
                new_probe.seq = data[13]
                new_probe.chr = str(data[11])
                new_probe.cord = int(data[12])
                new_probe.strand = data[16]
                new_probe.gene = data[21].split(";")
                new_probe.refseq = data[22]
                locs = data[23].split(";")
                list_locs = []
                for i in locs:
                    if i not in list_locs:
                        list_locs.append(i)

                new_probe.loc = list_locs

                new_probe.tour = data[25]
                newcpg = {new_probe.id: new_probe}
                self.probe.update(newcpg)

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

    def get_all_probes(self):
        """
        Return list of all probes.
        """
        probe_list = []
        for probe in self.probe.keys():
            probe_list.append(self.get_probe(probe))
        return probe_list
    
    def get_probes_by_list(self, list_of_ids):
        """
        Return a list of probes from a list of references.
        """
        out_list = []
        for probe_id in list_of_ids:
            out_list.append(self.get_probe(probe_id))

        return out_list
    
    def get_probe_refs_by_gene(self, gene_name):
        """
        Get all probe references associated with a gene.
        """
        probes = {k: self.probe[k] for k in self.probe if gene_name in self.probe[k].gene}
        return self.get_keys(probes.keys())

    def get_probe_refs_by_location(self, probe_loc):
        """
        Get all probe references associated with a genomic location.
        """
        probes = {k: self.probe[k] for k in self.probe if probe_loc in self.probe[k].loc}
        return self.get_keys(probes.keys())

    def get_keys(self, dic_keys):
        """
        Get Probe reference from probe dictionaries.
        """
        l = []
        for i in dic_keys:
            l.append(i)
        return l

    def get_probes_by_gene(self, gene_name):
        """
        Return list of probes for an associated gene.
        """
        return self.get_probes_by_list(self.get_probe_refs_by_gene(gene_name))

    def get_probes_by_location(self, loc):
        """
        Return list of probes from genomic location.
        """
        return self.get_probes_by_list(self.get_probe_refs_by_location(loc))

    def get_probes_by_cpg(self, cpg_loc):
        """
        Get a list probes from cpg location.
        FIXME
        """
        return self.get_probes_by_list(self.get_probes_by_cpg(cpg_loc))

    def get_probes_by_chr(self, chr_loc):
        """
        Get a list of probes within a certain genomic region
        FIXME
        """
        print (chr_loc.chr)
        probes = {k: self.probe[k] for k in self.probe if
                  self.probe[k].chr == chr_loc.chr}

    def get_probes_by_chr_and_loc(self, chr_loc):
        """
        Get a list of probes within a certain genomic region
        FIXME
        """
        chrom = chr_loc.chr
        start = int(chr_loc.start)
        end = int(chr_loc.end)
        
        #print (chrom, start, stop)

        probes = {k: self.probe[k] for k in self.probe if
                  self.probe[k].chr == chrom and start < self.probe[k].cord < end}
        return probes

    def get_probe_keys_by_chr_and_loc(self, chr_loc):
        """
        Get a list of probe reference *keys* within a genomic region
        FIXME
        """
        probes = self.get_probes_by_chr_and_loc(chr_loc)
        return self.get_keys(probes)

    def get_number(self):
        """
        Return total number of probes.
        """
        number = 0
        for probe_id in self.probe.keys():
            number += 1

        return number

    def get_coord(self, probe):
        """
        Get genomic coordinate of a single probe.
        """
        return probe.cord
    
    def get_sorted_probes_by_id(self):
        """
        Sort probes according to probe id.
        """
        sorted_keys = sorted(list(self.probe.keys()))
        return sorted_keys
    
    def get_sorted_probes_by_chr(self):
        """
        Sort probes according to probe id.
        """
        return sorted(self.get_all_probes(), key=lambda x: x.chr)
    
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
    with open('../../data/pickle/'+ name + '.pkl', 'wb+') as f:
        pickle.dump(obj, f)
        
def load_obj(name):
    with open('../../data/pickle/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)