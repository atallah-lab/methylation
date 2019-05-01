# See https://support.bioconductor.org/p/81964/ for more details

library(minfiData)

## 1. create two different GenomicRatioSets. First, create two MethylSets:
a <- MsetEx[1:100, ]
b <- MsetEx[50:120, ]

sampleNames(b) <- paste0("set", 1:6)
a_gr <- mapToGenome(ratioConvert(a, what="beta"))
b_gr <- mapToGenome(ratioConvert(b, what="beta"))

## 2. finding the common probe and subsetting the sets
p <- intersect(featureNames(b), featureNames(a))
a_sub <- a_gr[p, ]
b_sub <- b_gr[p, ]

## Combine the phenotype data and beta or M-values
## Note that the phenotype data (pData) is a data
## frame (or DataFrame) with samples as rows, variables as columns
pdata <- rbind(pData(a_sub), pData(b_sub)) 
beta <- cbind(getBeta(a_sub), getBeta(b_sub))
com <- GenomicRatioSet(gr = granges(a_sub), Beta=beta, 
                       M=NULL, CN=NULL, pData=pdata, annotation=annotation(a_sub))