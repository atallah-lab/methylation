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