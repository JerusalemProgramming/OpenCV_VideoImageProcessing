## IMPORT MODULES
import cv2
import PIL

## BEGIN CHECK FILE TYPE
def fn_ConvertFrameThresholdAdaptive_Mean(DictOfVideoCaptureDataObjects):

    """
        DOC STRING HERE - ERROR WITH THIS FUNCTION
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #00 - CONVERT FRAME THRESHOLD ADAPTIVE MEAN")

    ## DECLARE VARIABLES
    FileCounter = 1

    ## BEGIN FOR LOOP
    for k, VideoCaptureDataObject in DictOfVideoCaptureDataObjects.items():

        ## DECLARE VARIABLES
        ListForVideoGIFFramesThresholdAdaptive_Mean = []

        ## GET VARIABLES FROM VIDEO CAPTURE DATA OBJECT
        ListForVideoGIFFramesGRAY = VideoCaptureDataObject["ListForVideoGIFFramesGRAY"]

        ## BEGIN FOR LOOP
        for EachFrame in ListForVideoGIFFramesGRAY:

            ## CONVERT FRAME THRESHOLD - ADAPTIVE
            EachFrame_ThresholdAdaptive = cv2.adaptiveThreshold(EachFrame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
            
            ## APPEND IMAGE FRAME TO LIST SEQUENCE OF 2D FRAMES
            ListForVideoGIFFramesThresholdAdaptive_Mean.append(EachFrame_ThresholdAdaptive)

        ## END FOR LOOP
            
        ## UPDATE VIDEO CAPTURE DATA OBJECT
        VideoCaptureDataObject["ListForVideoGIFFramesThresholdAdaptive_Mean"] = ListForVideoGIFFramesThresholdAdaptive_Mean

        ## INCREMENT FILE COUNTER
        FileCounter += 1

        ## ADD VIDEO CAPTURE DATA OBJECT TO DICTIONARY OF VIDEO CAPTURE DATA OBJECTS
        DictOfVideoCaptureDataObjects[k] = VideoCaptureDataObject

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #00 - CONVERT FRAME CONVERT FRAME THRESHOLD ADAPTIVE MEAN")

    ## RETURN VARIABLES
    return(DictOfVideoCaptureDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""