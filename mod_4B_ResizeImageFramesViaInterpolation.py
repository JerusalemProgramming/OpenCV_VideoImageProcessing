## IMPORT MODULES
import cv2

## BEGIN CHECK FILE TYPE
def fn_ResizeImageFramesViaInterpolation(DictOfImageDataObjects):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #4B - RESIZE IMAGE FRAMES VIA INTERPOLATION")

    ## DECLARE VARIABLES
    FileCounter = 1

    ## BEGIN FOR LOOP
    for k, ImageDataObject in DictOfImageDataObjects.items():

        ## DECLARE VARIABLES
        ImageFrameOriginal = ImageDataObject["ImageFrameOriginal"]
        ## WidthNewDown = ImageDataObject["WidthNewDown"]
        ## HeightNewDown = ImageDataObject["HeightNewDown"]

        ## SCALING FACTORS FOR RESIZING
        ScaleDown = 0.3  
        ScaleUp = 1.1 

        ## RESIZE IMAGE (SCALE DOWN)
        ImageFrameResizedDown = cv2.resize(ImageFrameOriginal, None, fx=ScaleDown, fy=ScaleDown, interpolation=cv2.INTER_LINEAR)
        
        ## RESIZE IMAGE (SCALE UP)
        ImageFrameResizedUp = cv2.resize(ImageFrameOriginal, None, fx=ScaleUp, fy=ScaleUp, interpolation=cv2.INTER_LINEAR)

        ## cf.-> VS. RESIZE IMAGE FRAME VIA ASPECT RATIO --> EXACT PIXELS: W x H
        ## ImageFrameResized = cv2.resize(ImageFrameOriginal, (WidthNew, HeightNew))
        
        ## GET SHAPE OF RESIZED DOWN IMAGE FRAME
        ImageFrameResizedDownShape = ImageFrameResizedDown.shape

        ## GET SHAPE OF RESIZED UP IMAGE FRAME
        ImageFrameResizedUpShape = ImageFrameResizedUp.shape

        ## SET NEW KEY / VALUE PAIR IN DICTIONARY OF IMAGE DATA OBJECTS
        ## ImageDataObject["ImageFrameResized"] = ImageFrameResized ## NOT CREATED IN RESIZE VIA INTERPOLATION
        ImageDataObject["ImageFrameResizedDown"] = ImageFrameResizedDown
        ImageDataObject["ImageFrameResizedUp"] = ImageFrameResizedUp
        ## ImageDataObject["ImageFrameResizedShape"] = ImageFrameResizedShape ## NOT CREATED IN RESIZE VIA INTERPOLATION
        ImageDataObject["ImageFrameResizedDownShape"] = ImageFrameResizedDownShape
        ImageDataObject["ImageFrameResizedUpShape"] = ImageFrameResizedUpShape

        ## INCREMENT FILE COUNTER
        FileCounter += 1

        ## ADD IMAGE DATA OBJECT TO DICTIONARY OF IMAGE DATA OBJECTS
        DictOfImageDataObjects[k] = ImageDataObject

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #4B - RESIZE IMAGE FRAMES VIA INTERPOLATION")

    ## RETURN VARIABLES
    return(DictOfImageDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""