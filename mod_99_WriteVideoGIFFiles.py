## IMPORT MODULES
import os
import cv2
import numpy as np
import imageio
import mod_00_GetDictKeyFromSavePath

## BEGIN CHECK FILE TYPE
def fn_WriteVideoGIFFiles(DictOfVideoCaptureDataObjects, PathToDirectorySaved):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #99B - WRITE ANIMATED GIF FILES")

    ## CALL FUNCTION - GET DICT KEY TO VIDEO CAPTURE DATA OBJECT VIA FILE PATH TO SAVE FILES
    KEY_4_VideoCaptureDataObject = mod_00_GetDictKeyFromSavePath.fn_GetDictKeyFromSavePath(PathToDirectorySaved)

    print(f"TEST HERE: {KEY_4_VideoCaptureDataObject}")
    ## "ListForVideoGIFFramesThresholdAdaptive_Gaussian"
    ## "ListForVideoGIFFramesThresholdAdaptive_Mean"

    ## DECLARE VARIABLES
    FileCounter = 1

    ## IF FOLDER FOR RESIZED IMAGES DOES NOT EXIST...
    if not os.path.exists(PathToDirectorySaved):

        ## THEN CREATE THE FOLDER
        os.makedirs(PathToDirectorySaved)

    ## BEGIN FOR LOOP
    for k, VideoCaptureDataObject in DictOfVideoCaptureDataObjects.items():

        ## DECLARE VARIABLES
        FileName = VideoCaptureDataObject["FileName"]
        FrameCount = VideoCaptureDataObject["FrameCount"]
        FPS = VideoCaptureDataObject["FPS"]
        Duration = VideoCaptureDataObject["Duration"] ## IN MILLISECONDS

        ## IF LIST OF 2D IMAGE FRAMES FOR ANIMATED GIF EXIST...        
        if VideoCaptureDataObject[KEY_4_VideoCaptureDataObject] is not None: ## List of ## <class 'numpy.ndarray'>

            ## THEN CREATE A SPECIFIC PATH FOR EACH VIDEO/GIF FILE NAME
            PathToCopyOfOriginalGIF = f"{PathToDirectorySaved}{FileName}"

            ## THEN GET THE LIST OF 2D IMAGE FRAMES FOR EACH VIDEO
            ListForVideoGIFFrames4Export = VideoCaptureDataObject[KEY_4_VideoCaptureDataObject] ## type() == <class 'list'> of ## <class 'numpy.ndarray'>

            ## CREATE LIST OF FRAMES (I.E. LIST OF NUMPY ARRAYS)
            ALL_FRAMES = ListForVideoGIFFrames4Export ## type() == <class 'list'> of <class 'numpy.ndarray'>

            ## SAVE ANIMATED GIF 
            ## mimsave(save_name_gif, pics_list, 'GIF', fps=fps, loop=loop)
            imageio.mimsave(PathToCopyOfOriginalGIF, ALL_FRAMES, fps=FPS, format='GIF', loop=0)
            ## imageio.imwrite(PathToCopyOfOriginalGIF, ALL_FRAMES, duration=30, format='GIF', loop=0)

            ## TEST PRINT OUTPUT
            print(f"Duration: {Duration} ms")
            print(f"FrameCount: {FrameCount}")
            print(f"FPS: {FPS}")
            
        else:

            pass
            
        ## INCREMENT FILE COUNTER
        FileCounter += 1

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #99B - WRITE ANIMATED GIF FILES")

    ## RETURN VARIABLES
    return(DictOfVideoCaptureDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""