# R function to combine two GenomicRatoSets. 
# This function emulates a full outer join on two matrix objects.

combineTCGAfiles <- function (object1, object2,
            outType = "IlluminaHumanMethylation450k",
            verbose = TRUE) {

    outType <- match.arg(outType)
    array1 <- annotation(object1)["array"]
    array2 <- annotation(object2)["array"]
    if (array1 == array2) outType <- array1
    object1 <- convertArray(object1, outType = outType, verbose = verbose)
    object2 <- convertArray(object2, outType = outType, verbose = verbose)
    colData1 <- colData(object1)
    colData2 <- colData(object2)
    colData1$ArrayTypes <- array1
    colData2$ArrayTypes <- array2
    colData1 <- colData(object1)
    colData2 <- colData(object2)
    by <- c("row.names", intersect(names(colData1), names(colData2)))
    colData.merged <- merge(colData1, colData2, all = TRUE, by = by)
    colData(object1) <- colData.merged[match(
        x = colnames(object1),
        table = colData.merged[, "Row.names"]), ]
    colData(object2) <- colData.merged[match(
        x = colnames(object2),
        table = colData.merged[, "Row.names"]), ]
    gr.common <- intersect(granges(object1), granges(object2))
    object1 <- sort(subsetByOverlaps(object1, gr.common))
    object2 <- sort(subsetByOverlaps(object2, gr.common))
    GRset <- cbind(object1, object2)
    colnames(GRset) <- GRset$Row.names
    GRset$Row.names <- NULL
    GRset
}