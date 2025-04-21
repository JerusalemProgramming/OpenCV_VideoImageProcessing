## IMPORT MODULES
import cv2

## BEGIN CHECK FILE TYPE
def fn_ConvertFrameRGB2HSV(DictOfVideoCaptureDataObjects):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #00 - CONVERT FRAME FROM RGB TO HSV")

    ## DECLARE VARIABLES
    FileCounter = 1

    ## BEGIN FOR LOOP
    for k, VideoCaptureDataObject in DictOfVideoCaptureDataObjects.items():

        ## DECLARE VARIABLES
        ListForVideoGIFFramesHSV = []

        ## GET VARIABLES FROM VIDEO CAPTURE DATA OBJECT
        ListForVideoGIFFramesRGB = VideoCaptureDataObject["ListForVideoGIFFramesRGB"]

        ## BEGIN FOR LOOP
        for EachFrame in ListForVideoGIFFramesRGB:

            ## CONVERT TO GRAYSCALE
            EachFrameHSV = cv2.cvtColor(EachFrame, cv2.COLOR_RGB2HSV)

            ## APPEND EACH GRAY FRAME TO LIST
            ListForVideoGIFFramesHSV.append(EachFrameHSV)

        ## END FOR LOOP
            
        ## UPDATE VIDEO CAPTURE DATA OBJECT
        VideoCaptureDataObject["ListForVideoGIFFramesHSV"] = ListForVideoGIFFramesHSV

        ## INCREMENT FILE COUNTER
        FileCounter += 1

        ## ADD VIDEO CAPTURE DATA OBJECT TO DICTIONARY OF VIDEO CAPTURE DATA OBJECTS
        DictOfVideoCaptureDataObjects[k] = VideoCaptureDataObject

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #00 - CONVERT FRAME FROM RGB TO HSV")

    ## RETURN VARIABLES
    return(DictOfVideoCaptureDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""