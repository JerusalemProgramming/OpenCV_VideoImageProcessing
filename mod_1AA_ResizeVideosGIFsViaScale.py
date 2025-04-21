## IMPORT MODULES
import cv2
import mod_00_GetDictKeyFromSavePath

## BEGIN CHECK FILE TYPE
def fn_ResizeVideosGIFsViaScale(DictOfVideoCaptureDataObjects, PathToDirectoryOriginals, PathToDirectorySaved):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #1AA - RESIZE VIDEOS GIFS VIA SCALE")

    ## CALL FUNCTION - GET DICT KEY TO VIDEO CAPTURE DATA OBJECT VIA FILE PATH TO FOR DESIRED "ORIGINAL" IMAGES TO BE RESIZED
    KEY_4_VideoCaptureDataObjectOriginals = mod_00_GetDictKeyFromSavePath.fn_GetDictKeyFromSavePath(PathToDirectoryOriginals)

    ## CALL FUNCTION - GET DICT KEY TO VIDEO CAPTURE DATA OBJECT VIA FILE PATH TO SAVE FILES
    KEY_4_VideoCaptureDataObjectResized = mod_00_GetDictKeyFromSavePath.fn_GetDictKeyFromSavePath(PathToDirectorySaved)
    
    ## DECLARE VARIABLES
    FileCounter = 1
    Scale = 1.33
    ListForVideoGIFFramesResized = []

    ## BEGIN FOR LOOP
    for k, VideoCaptureDataObject in DictOfVideoCaptureDataObjects.items():

        ## DECLARE VARIABLES
        ## N/A

        ## BEGIN FOR LOOP
        for ImageFrameOriginal in VideoCaptureDataObject[KEY_4_VideoCaptureDataObjectOriginals]: ##

            ## TEST PRINT OUTPUT
            ## print(ImageFrameOriginal)

            WidthNew = int(ImageFrameOriginal.shape[1] * Scale)
            HeightNew = int(ImageFrameOriginal.shape[0] * Scale)

            ## RESIZE IMAGE FRAME
            ImageFrameResized = cv2.resize(ImageFrameOriginal, (WidthNew, HeightNew), interpolation=cv2.INTER_AREA)

            ## APPEND 2D IMAGE FRAME TO LIST OF 2D IMAGE FRAMES
            ListForVideoGIFFramesResized.append(ImageFrameResized)

        ## END FOR LOOP

        ## UPDATE VIDEO CAPTURE DATA OBJECT
        VideoCaptureDataObject[KEY_4_VideoCaptureDataObjectResized] = ListForVideoGIFFramesResized

        ## RESET LIST OF 2D FRAMES FOR THE NEXT VIDEO/GIF FILE
        ListForVideoGIFFramesResized = []

        ## INCREMENT FILE COUNTER
        FileCounter += 1

        ## ADD VIDEO CAPTURE DATA OBJECT TO DICTIONARY OF VIDEO CAPTURE DATA OBJECTS
        DictOfVideoCaptureDataObjects[k] = VideoCaptureDataObject

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #1AA - RESIZE VIDEOS GIFS VIA SCALE")

    ## RETURN VARIABLES
    return(DictOfVideoCaptureDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""