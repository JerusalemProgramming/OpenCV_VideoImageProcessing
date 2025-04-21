## IMPORT MODULES
import cv2

## BEGIN CHECK FILE TYPE
def fn_ConvertFrameGaussianBlur(DictOfVideoCaptureDataObjects):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #00 - CONVERT FRAME GAUSSIAN BLUR")

    ## DECLARE VARIABLES
    FileCounter = 1

    ## BEGIN FOR LOOP
    for k, VideoCaptureDataObject in DictOfVideoCaptureDataObjects.items():

        ## DECLARE VARIABLES
        ListForVideoGIFFramesGaussianBlur = []

        ## GET VARIABLES FROM VIDEO CAPTURE DATA OBJECT
        ListForVideoGIFFramesOriginals = VideoCaptureDataObject["ListForVideoGIFFramesRGB"] ## KEY FOR DICT

        ## BEGIN FOR LOOP
        for EachFrame in ListForVideoGIFFramesOriginals:

            ## CONVERT TO GRAYSCALE
            EachFrameGaussianBlur = cv2.GaussianBlur(EachFrame, (5,5), 0)

            ## APPEND EACH ABSTRACT FRAME TO LIST
            ListForVideoGIFFramesGaussianBlur.append(EachFrameGaussianBlur)

        ## END FOR LOOP
            
        ## UPDATE VIDEO CAPTURE DATA OBJECT
        VideoCaptureDataObject["ListForVideoGIFFramesGaussianBlur"] = ListForVideoGIFFramesGaussianBlur

        ## INCREMENT FILE COUNTER
        FileCounter += 1

        ## ADD VIDEO CAPTURE DATA OBJECT TO DICTIONARY OF VIDEO CAPTURE DATA OBJECTS
        DictOfVideoCaptureDataObjects[k] = VideoCaptureDataObject

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #00 - CONVERT FRAME GAUSSIAN BLUR")

    ## RETURN VARIABLES
    return(DictOfVideoCaptureDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""