## IMPORT MODULES
import cv2
import PIL

## BEGIN CHECK FILE TYPE
def fn_ConvertFrameRGB2PILImage(DictOfVideoCaptureDataObjects):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #00 - CONVERT FRAME FROM RGB TO PIL IMAGE (RGB FORMAT)")

    ## DECLARE VARIABLES
    FileCounter = 1

    ## BEGIN FOR LOOP
    for k, VideoCaptureDataObject in DictOfVideoCaptureDataObjects.items():

        ## DECLARE VARIABLES
        ListForVideoGIFFramesPIL = []

        ## GET VARIABLES FROM VIDEO CAPTURE DATA OBJECT
        ListForVideoGIFFramesRGB = VideoCaptureDataObject["ListForVideoGIFFramesRGB"]

        ## BEGIN FOR LOOP
        for EachFrame in ListForVideoGIFFramesRGB:

            ## CONVERT BGR (FROM OPENCV DEFAULT FORMAT) TO RGB (COMMON FORMAT) TO SAVE VIA IMAGEIO
            ## EachFrame = cv2.cvtColor(EachFrame, cv2.COLOR_BGR2RGB) ## type(EachFrame) == <class 'numpy.ndarray'>

            ## CONVERT TO PIL IMAGE FORMAT   
            EachFrame = PIL.Image.fromarray(EachFrame) ## type(EachFrame) == <class 'PIL.Image.Image'>
            
            ## APPEND IMAGE FRAME TO LIST SEQUENCE OF 2D FRAMES
            ListForVideoGIFFramesPIL.append(EachFrame)

        ## END FOR LOOP
            
        ## UPDATE VIDEO CAPTURE DATA OBJECT
        VideoCaptureDataObject["ListForVideoGIFFramesPIL"] = ListForVideoGIFFramesPIL

        ## INCREMENT FILE COUNTER
        FileCounter += 1

        ## ADD VIDEO CAPTURE DATA OBJECT TO DICTIONARY OF VIDEO CAPTURE DATA OBJECTS
        DictOfVideoCaptureDataObjects[k] = VideoCaptureDataObject

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #00 - CONVERT FRAME FROM RGB TO PIL IMAGE (RGB FORMAT)")

    ## RETURN VARIABLES
    return(DictOfVideoCaptureDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""