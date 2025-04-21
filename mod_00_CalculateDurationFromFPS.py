## IMPORT MODULES
import cv2

## BEGIN CHECK FILE TYPE
def fn_CalculateDurationFromFPS(DictOfVideoCaptureDataObjects):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #00 - CALCULATE DURATION IN MILLISECONDS FROM FPS")

    ## DECLARE VARIABLES
    FileCounter = 1

    ## BEGIN FOR LOOP
    for k, VideoCaptureDataObject in DictOfVideoCaptureDataObjects.items():

        ## DECLARE VARIABLES
        ## N/A

        ## GET VARIABLES FROM VIDEO CAPTURE DATA OBJECT
        FrameCount = VideoCaptureDataObject["FrameCount"]
        FPS = VideoCaptureDataObject["FPS"]

        ## CALCULATE MILLISECONDS FROM FRAME COUNT AND FPS
        Milliseconds = (FrameCount * 1000) / FPS

        ## UPDATE VIDEO CAPTURE DATA OBJECT
        VideoCaptureDataObject["Duration"] = Milliseconds

        ## INCREMENT FILE COUNTER
        FileCounter += 1

        ## ADD VIDEO CAPTURE DATA OBJECT TO DICTIONARY OF VIDEO CAPTURE DATA OBJECTS
        DictOfVideoCaptureDataObjects[k] = VideoCaptureDataObject

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #00 - CALCULATE DURATION IN MILLISECONDS FROM FPS")

    ## RETURN VARIABLES
    return(DictOfVideoCaptureDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""