from methylator.feature import Feature, Probe, Interval, Location, CpG_location

def get_probes(annotations, probes_ids):
    """
    Return a list of probes from probe ids
    """
    return annotations.get_probes(probes_ids)


def get_probes_from_feature(probes_ids, filter_val):
    """
    Return probes based on a feature.
    """
    probes = probes_ids
    out_probes = []
    if filter_val.feature_title == "Location":
        out_probes = [probe for probe in probes if filter_val.feature in probe.loc]
        print("Location")
        return out_probes
    elif filter_val.feature_title == "cpg_loc":
        print("CPG")
        out_probes = [probe for probe in probes if filter_val.feature in probe.tour]
        return out_probes
    elif filter_val.feature_title == "gene":
        out_probes = [probe for probe in probes if filter_val.feature in probe.gene]
        return out_probes
    elif filter_val is None:
        return None