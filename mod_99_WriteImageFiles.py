## IMPORT MODULES
import os
import cv2

## BEGIN CHECK FILE TYPE
def fn_WriteImageFiles(PathToDirectoryResized, PathToDirectoryResizedDown, PathToDirectoryResizedUp, DictOfImageDataObjects):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #99 - WRITE IMAGE FILES")

    ## DECLARE VARIABLES
    FileCounter = 1

    ## IF FOLDER FOR RESIZED IMAGES DOES NOT EXIST...
    if not os.path.exists(PathToDirectoryResized):

        ## THEN CREATE THE FOLDER
        os.makedirs(PathToDirectoryResized)

    ## IF FOLDER FOR RESIZED DOWN IMAGES DOES NOT EXIST...
    if not os.path.exists(PathToDirectoryResizedDown):

        ## THEN CREATE THE FOLDER
        os.makedirs(PathToDirectoryResizedDown)

    ## IF FOLDER FOR RESIZED UP IMAGES DOES NOT EXIST...
    if not os.path.exists(PathToDirectoryResizedUp):

        ## THEN CREATE THE FOLDER
        os.makedirs(PathToDirectoryResizedUp)

    ## BEGIN FOR LOOP
    for k, ImageDataObject in DictOfImageDataObjects.items():

        ## DECLARE VARIABLES
        FileName = ImageDataObject["FileName"]
        
        if ImageDataObject["ImageFrameResized"] is not None:
            
            PathToImageResized = f"{PathToDirectoryResized}{FileName}"

            ImageFrameResized = ImageDataObject["ImageFrameResized"]
           
            ## SAVE COPY TO DISK IN SEPARATE FOLDER WITH SAME FILE NAME
            cv2.imwrite(PathToImageResized, ImageFrameResized)

        else:

            pass

        if ImageDataObject["ImageFrameResizedDown"] is not None:

            PathToImageResizedDown = f"{PathToDirectoryResizedDown}{FileName}"
            
            ImageFrameResizedDown = ImageDataObject["ImageFrameResizedDown"]

            ## SAVE COPY TO DISK IN SEPARATE FOLDER WITH SAME FILE NAME
            cv2.imwrite(PathToImageResizedDown, ImageFrameResizedDown)
        
        else:

            pass

        if ImageDataObject["ImageFrameResizedUp"] is not None:

            PathToImageResizedUp = f"{PathToDirectoryResizedUp}{FileName}"
            
            ImageFrameResizedUp = ImageDataObject["ImageFrameResizedUp"]          

            ## SAVE COPY TO DISK IN SEPARATE FOLDER WITH SAME FILE NAME
            cv2.imwrite(PathToImageResizedUp, ImageFrameResizedUp)

        else:

            pass
        
        ## INCREMENT FILE COUNTER
        FileCounter += 1

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #99 - WRITE IMAGE FILES")

    ## RETURN VARIABLES
    return(DictOfImageDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""