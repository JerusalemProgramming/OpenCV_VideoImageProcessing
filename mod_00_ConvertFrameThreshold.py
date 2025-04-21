## IMPORT MODULES
import cv2
import PIL

## BEGIN CHECK FILE TYPE
def fn_ConvertFrameThreshold(DictOfVideoCaptureDataObjects, Threshold):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #00 - CONVERT FRAME THRESHOLD")

    ## DECLARE VARIABLES
    FileCounter = 1

    ## BEGIN FOR LOOP
    for k, VideoCaptureDataObject in DictOfVideoCaptureDataObjects.items():

        ## DECLARE VARIABLES
        ListForVideoGIFFramesThreshold = []
        ListForVideoGIFFramesThreshold_INV = []

        ## GET VARIABLES FROM VIDEO CAPTURE DATA OBJECT
        ListForVideoGIFFramesGRAY = VideoCaptureDataObject["ListForVideoGIFFramesGRAY"]

        ## BEGIN FOR LOOP
        for EachFrame in ListForVideoGIFFramesGRAY:

            ## CONVERT FRAME THRESHOLD
            ## EachFrame = cv2.cvtColor(EachFrame, cv2.COLOR_BGR2RGB) ## type(EachFrame) == <class 'numpy.ndarray'>
            Threshold, EachFrame = cv2.threshold(EachFrame, Threshold, 255, cv2.THRESH_BINARY) ## Threshold = 150

            ## CONVERT FRAME THRESHOLD - INVERSE
            Threshold_INV, EachFrame_INV = cv2.threshold(EachFrame, Threshold, 255, cv2.THRESH_BINARY_INV) ## Threshold = 150
            
            ## APPEND IMAGE FRAME TO LIST SEQUENCE OF 2D FRAMES
            ListForVideoGIFFramesThreshold.append(EachFrame)
            ListForVideoGIFFramesThreshold_INV.append(EachFrame_INV)

        ## END FOR LOOP
            
        ## UPDATE VIDEO CAPTURE DATA OBJECT
        VideoCaptureDataObject["ListForVideoGIFFramesThreshold"] = ListForVideoGIFFramesThreshold
        VideoCaptureDataObject["ListForVideoGIFFramesThreshold_INV"] = ListForVideoGIFFramesThreshold_INV

        ## INCREMENT FILE COUNTER
        FileCounter += 1

        ## ADD VIDEO CAPTURE DATA OBJECT TO DICTIONARY OF VIDEO CAPTURE DATA OBJECTS
        DictOfVideoCaptureDataObjects[k] = VideoCaptureDataObject

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #00 - CONVERT FRAME CONVERT FRAME THRESHOLD")

    ## RETURN VARIABLES
    return(DictOfVideoCaptureDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""