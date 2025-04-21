## IMPORT MODULES
import cv2

## BEGIN CHECK FILE TYPE
def fn_ConvertFrameRGB2BGR(DictOfVideoCaptureDataObjects):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #00 - CONVERT FRAME FROM RGB TO BGR")

    ## DECLARE VARIABLES
    FileCounter = 1

    ## BEGIN FOR LOOP
    for k, VideoCaptureDataObject in DictOfVideoCaptureDataObjects.items():

        ## DECLARE VARIABLES
        ListForVideoGIFFramesBGR = []

        ## GET VARIABLES FROM VIDEO CAPTURE DATA OBJECT
        ListForVideoGIFFramesRGB = VideoCaptureDataObject["ListForVideoGIFFramesRGB"]

        ## BEGIN FOR LOOP
        for EachFrame in ListForVideoGIFFramesRGB:

            ## CONVERT TO BGR
            EachFrameBGR = cv2.cvtColor(EachFrame, cv2.COLOR_RGB2BGR)

            ## APPEND EACH BGR FRAME TO LIST
            ListForVideoGIFFramesBGR.append(EachFrameBGR)

        ## END FOR LOOP
            
        ## UPDATE VIDEO CAPTURE DATA OBJECT
        VideoCaptureDataObject["ListForVideoGIFFramesBGR"] = ListForVideoGIFFramesBGR

        ## INCREMENT FILE COUNTER
        FileCounter += 1

        ## ADD VIDEO CAPTURE DATA OBJECT TO DICTIONARY OF VIDEO CAPTURE DATA OBJECTS
        DictOfVideoCaptureDataObjects[k] = VideoCaptureDataObject

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #00 - CONVERT FRAME FROM RGB TO BGR")

    ## RETURN VARIABLES
    return(DictOfVideoCaptureDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""