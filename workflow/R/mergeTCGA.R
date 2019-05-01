# Combine two JHU tab-delimited files into one GenomicRatioSet object. 

library(minfi)

source("../workflow/combineTCGAfiles.R")

jhu_1 <- '../data/johnshopkins-data/TEST/GBM_NORMAL-short.txt'
jhu_2 <- '../data/johnshopkins-data/TEST/GBM_TUMOR-short.txt'

grset1_from_TCGA <- readTCGA(jhu_1)
grset2_from_TCGA <- readTCGA(jhu_2)

#p <- intersect(featureNames(grset1_from_TCGA), featureNames(grset2_from_TCGA))
#q <- intersect(sampleNames(grset1_from_TCGA), sampleNames(grset2_from_TCGA))

gr.common <- intersect(granges(grset1_from_TCGA), granges(grset2_from_TCGA))

combined <- combineTCGAfiles(grset1_from_TCGA, grset2_from_TCGA)
combined