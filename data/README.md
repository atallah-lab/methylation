## Data Directory

##### This directory holds data files specific to methylation analysis that are separate from the tutorials. The contents in johnshopkins-data constitute a 'minimum viable dataset'. Here we have whole-genome methylation data from tumour/normal pairs within colon, lung, and brain tissues. The directories and files included are:

* __eul1db-data__ - Human-specific L1 (L1-HS) insertion data taken from [__euL1db__](http://euL1db.unice.fr) database. This database provides a curated summary of L1HS insertion polymorphisms identified in healthy and pathological human samples and published in peer-reviewed journals. A key feature of __euL1db__ is its sample-wise organization. L1HS insertions are connected to samples, individuals, families and clinical conditions.  

* __johnshopkins-data__ - Johns Hopkins has provided methylation array data from the Illumina 450k platform. The codes for available JH studies are TCGA-GBM (glioblastoma multiforme), TCGA-COAD (colon carcinoma), TCGA-LUAD (lung adenocarcinoma), TCGA-LUSC (lung squamous cell carcinoma). These data may be accessed from TCGA [at this link](https://bit.ly/2W7e1xe). This will get you to the right area to start you search. The specific data used here (may change) are organized in the following way:

    - __COAD__-PAIRED-SAMPLE-sample-sheet.2019-03-18.tsv - represents a matched normal/colon cancer pair. The sample sheet is not the data itself but a reference to it.

    - __GBM__-PAIRED-SAMPLE-sample-sheet.2019-03-18.tsv - a matched normal/glioblastoma  pair.

    - __LUAD__-PAIRED-SAMPLE-sample-sheet.2019-03-18.tsv - a matched normal/adenocarcinoma  pair.

    - __LUSC__-PAIRED-SAMPLE-sample-sheet.2019-03-18.tsv - a matched normal/squamous cell pair.   

* __tcga-data__ - Other 'non-JHU' datasets derived from TCGA (The Cancer Genome Atlas). 

* __L1Ta-SOMATIC-ANNOTATION__

* __dmrs_B1000_c02.Rda__