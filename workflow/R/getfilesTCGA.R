# Functions provided by TCGAbiolinks to download DNA methylation (and other) data from 
# the GDC open database.

# May need to install the following library
# BiocManager::install(c("TCGAbiolinks"), update = TRUE, ask = FALSE)

 library(TCGAbiolinks)
 library(SummarizedExperiment)

# NOTE: The data in the legacy database has been aligned to hg19
#-----------------------------------
# DNA methylation
# ----------------------------------
query.met.lusc <- GDCquery(project = "TCGA-LUSC", 
                           legacy = TRUE, 
                           data.category = "DNA methylation",
                           platform = "Illumina Human Methylation 450",
                           barcode = c("TCGA-43-6771-01A-11D-1818-05", "TCGA-43-6771-11A-01D-1818-05"))
 GDCdownload(query.met.lusc)

met.lusc.450 <- GDCprepare(query = query.met.lusc,
                        save = TRUE,
                        save.filename = "LUSCmet-paired.rda" ,
                        summarizedExperiment = TRUE)

head(assay(met.lusc.450))

length(row.names(met.lusc.450))

met.lusc.450 <- subset(met.lusc.450,subset = (rowSums(is.na(assay(met.lusc.450))) == 0))

length(row.names(met.lusc.450)) # removes NA rows

# TCGA-43-6771-01A = Tumor
# TCGA-43-6771-11A = Normal

result <- TCGAanalyze_DMR(met.lusc.450, groupCol = "barcode", 
                          group1 = "TCGA-43-6771-11A-01D-1818-05",
                          group2 = "TCGA-43-6771-01A-11D-1818-05")

#idx1 <- which(colData(met.lusc.450)[,"barcode"] == "TCGA-43-6771-11A-01D-1818-05")
#idx2 <- which(colData(met.lusc.450)[,"barcode"] == "TCGA-43-6771-01A-11D-1818-05")
