# Load eul1db LINE-1 data
library(rtracklayer)
library(IlluminaHumanMethylation450kanno.ilmn12.hg19) 
library(IlluminaHumanMethylation450kmanifest)

setwd("/Users/geraldmccollam/2019Code/Atallah/methylation") # set this relative to your installation.

# MRIPs (meta-retrotransposon insertion polymorphisms) 
# are virtual insertions obtained by merging overlapping 
# or close SRIPs, which are likely to correspond to the 
# same retrotransposition event.
mrip_track <- import("./data/eul1db-data/eul1db_mrip.bed", format="bed") # class is GenomicRanges
# srip_track <- import("eul1db_srip.bed", format="bed") # raises IRanges error, negative widths

ann450k = getAnnotation(IlluminaHumanMethylation450kanno.ilmn12.hg19)

# Returns a Granges object with overlap between the mrip_track and CpG's.  
# and 