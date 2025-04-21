## IMPORT MODULES
import os

## BEGIN CHECK FILE TYPE
def fn_CheckFileTypes(PathToDirectory):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #0 - CHECK FILE TYPES")

    ## DECLARE VARIABLES
    ListOfFileNamesInDirectory = []
    ListOfGIFs = []
    ListOfOthers = []
    SetOfExtensions = set()

    ## GET LIST OF FILE NAMES IN DIRECTORY
    ListOfFileNamesInDirectory = os.listdir(PathToDirectory)

    ## BEGIN FOR LOOP
    for FileName in ListOfFileNamesInDirectory:

        ## GET FILE EXTENSION (INCLUDING .DOT)
        _, FileExtension = os.path.splitext(FileName)

        if FileExtension:  ## IF A FILE EXTENSION EXISTS

            SetOfExtensions.add(FileExtension.lower())  ## ADD FILE NAME EXTENSION TO THE SET (lower case)

            if FileExtension == ".gif": ## IF A FILE EXTENSION IS A GIF

                ListOfGIFs.append(FileName) ## THEN ADD FILE NAME TO THE LIST OF GIF FILE NAMES

            else:
            
                ListOfOthers.append(FileName) ## THEN ADD FILE NAME TO THE LIST OF ALL OTHER FILE NAMES
            
    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    ## print("File extensions found:")
    ## for Extension in SetOfExtensions:
        
        ## TEST PRINT OUTPUT
        ## print(Extension)

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #0 - CHECK FILE TYPES")

    ## RETURN VARIABLES
    return(ListOfFileNamesInDirectory, ListOfGIFs, ListOfOthers, SetOfExtensions)

## END DEFINE FUNCTION