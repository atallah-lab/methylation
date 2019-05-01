# #################
# ##### methylation
# #################

 library(minfi)

 setwd("/Users/geraldmccollam/2019Code/Atallah/methylation/data")

# Example directory in which untarred data will be stored.
 dir.create('meth_data_tcga')
 
# Download Lung Squamous Cell Carcinoma (LUSC) methylation data.
 cancerType = "LUSC"
 downloadTCGA(cancerTypes = cancerType,
              dataSet = "Merge_methylation__humanmethylation27",
              destDir = "meth_data_tcga")
 
# Shorten path of subdirectory with LUSC methylation data
 list.files(path = "meth_data_tcga", full.names = TRUE) %>%
     file.rename(to = file.path("meth_data_tcga", paste0(cancerType, ".methylation")))

# Remove manifest.txt file
 list.files(path = "meth_data_tcga", full.names = TRUE, 
            recursive = TRUE, pattern = "MANIFEST") %>%
            file.remove()
 
# Read LUSC methylation data
 path <- list.files(path = "meth_data_tcga", full.names = TRUE, recursive = TRUE)
 LUSC.methylation <- readTCGA(path, dataType = "methylation")
 