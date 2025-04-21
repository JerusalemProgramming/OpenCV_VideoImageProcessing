## IMPORT MODULES
import cv2

## BEGIN CHECK FILE TYPE
def fn_ConvertFrameBGR2GRAY(DictOfVideoCaptureDataObjects):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #00 - CONVERT FRAME FROM BGR TO GRAYSCALE")

    ## DECLARE VARIABLES
    FileCounter = 1

    ## BEGIN FOR LOOP
    for k, VideoCaptureDataObject in DictOfVideoCaptureDataObjects.items():

        ## DECLARE VARIABLES
        ListForVideoGIFFramesGRAY = []

        ## GET VARIABLES FROM VIDEO CAPTURE DATA OBJECT
        ListForVideoGIFFramesBGR = VideoCaptureDataObject["ListForVideoGIFFramesBGR"]

        ## BEGIN FOR LOOP
        for EachFrame in ListForVideoGIFFramesBGR:

            ## CONVERT TO GRAYSCALE
            EachFrameGray = cv2.cvtColor(EachFrame, cv2.COLOR_BGR2GRAY)

            ## APPEND EACH GRAY FRAME TO LIST
            ListForVideoGIFFramesGRAY.append(EachFrameGray)

        ## END FOR LOOP
            
        ## UPDATE VIDEO CAPTURE DATA OBJECT
        VideoCaptureDataObject["ListForVideoGIFFramesGRAY"] = ListForVideoGIFFramesGRAY

        ## INCREMENT FILE COUNTER
        FileCounter += 1

        ## ADD VIDEO CAPTURE DATA OBJECT TO DICTIONARY OF VIDEO CAPTURE DATA OBJECTS
        DictOfVideoCaptureDataObjects[k] = VideoCaptureDataObject

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #00 - CONVERT FRAME FROM BGR TO GRAYSCALE")

    ## RETURN VARIABLES
    return(DictOfVideoCaptureDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""