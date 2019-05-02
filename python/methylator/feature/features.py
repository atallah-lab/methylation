class Feature:
    """
    Parses features (functional regions) associated with probes.

    Feature codes:
        TSS200 is the region from TSS to − 200 nt upstream.
        TSS1500 covers − 200 to − 1500 nt upstream of TSS
    """

    def __init__(self, feature):
        self.feature_title = None
        self.feature = None
        if feature in ["Body", "TSS200", "TSS1500", "5'UTR", "3'UTR", "Exon"]:
            self.feature_title = "Location"
            self.feature = feature
        elif feature in ["Island", "N_Shore", "S_Shore", "N_Shelf", "S_Shelf"]:
            self.feature_title = "cpg_loc"
            self.feature = feature
        else:
            self.feature_title = "gene"
            self.feature = feature


class Probe:
    """
    Holds probe info.
    """
    def __init__(self):
        self.id = None
        self.seq = None
        self.name = None
        self.chr = None
        self.cord = None
        self.strand = None
        self.gene = None
        self.refseq = None
        self.beta = None
        self.tour = None
        self.loc = None

class SNP:
    """
    Defines SNPs in probes. Used to filter probes.
    """

    def __init__(self):
        self.probeid = None
        self.snpid = None