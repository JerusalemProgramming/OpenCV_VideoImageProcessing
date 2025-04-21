## IMPORT MODULES
import cv2

## BEGIN CHECK FILE TYPE
def fn_ResizeImageFrames(DictOfImageDataObjects):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #4A - RESIZE IMAGE FRAMES")

    ## DECLARE VARIABLES
    FileCounter = 1

    ## BEGIN FOR LOOP
    for k, ImageDataObject in DictOfImageDataObjects.items():

        ## DECLARE VARIABLES
        ImageFrameOriginal = ImageDataObject["ImageFrameOriginal"]
        WidthNew = ImageDataObject["WidthNew"]
        HeightNew = ImageDataObject["HeightNew"]

        ## RESIZE IMAGE FRAME
        ImageFrameResized = cv2.resize(ImageFrameOriginal, (WidthNew, HeightNew))
        
        ## GET SHAPE OF RESIZED IMAGE FRAME
        ImageFrameResizedShape = ImageFrameResized.shape

        ## SET NEW KEY / VALUE PAIR IN DICTIONARY OF IMAGE DATA OBJECTS
        ImageDataObject["ImageFrameResized"] = ImageFrameResized
        ImageDataObject["ImageFrameResizedShape"] = ImageFrameResizedShape

        ## INCREMENT FILE COUNTER
        FileCounter += 1

        ## ADD IMAGE DATA OBJECT TO DICTIONARY OF IMAGE DATA OBJECTS
        DictOfImageDataObjects[k] = ImageDataObject

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #4A - RESIZE IMAGE FRAMES")

    ## RETURN VARIABLES
    return(DictOfImageDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""