## IMPORT MODULES
import cv2
import numpy as np
## import matplotlib.pyplot as plt

## BEGIN DEFINE FUNCTION: OPEN LIST OF MULTIPLE VIDEO (GIF) FILES
def fn_OpenFilesVideos(ListOfGIFs, PathToDirectoryOriginals):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #1A - OPEN FILES VIDEOS GIFs")

    ## DECLARE VARIABLES
    DictOfVideoCaptureDataObjects = {} ## {1: { }, 2: { }, 3: { } }
    VideoCaptureDataObject = {}
    ListForVideoGIFFramesBGR = [] ## CONVERT TO NUMPY ARRAY AFTER COMPLETE
    ListTemp = [] ## FOR CONVERTING TO A TUPLE TO CONTAIN INDIVIDUAL IMAGE FRAME DATA
    FileCounter = 1 ## VideoCounter

    ## BEGIN FOR LOOP
    for FileName in ListOfGIFs:

        print(f"\nVIDEO #: {FileCounter}")

        ## OPEN VIDEO FILE
        cap = cv2.VideoCapture(f"{PathToDirectoryOriginals}{FileName}")

        ## CHECK IF VIDEO FILE OPENED SUCCESSFULLY
        if cap.isOpened():

            print("Video file opened successfully!")
            print(f"cap: {cap}")
        
        ## GET VIDEO PROPERTIES
        ## GET FRAME COUNT
        FrameCount= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  ## GET TOTAL NUMBER OF FFRAMES IN THE VIDEO

        ## GET FPS
        fps = cap.get(cv2.CAP_PROP_FPS)  ## GET FRAMES PER SECOND (FPS)

        ## GET FRAME WIDTH
        FrameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        ## GET FRAME HEIGHT
        FrameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        ## DEFINE CODEC, AND CREATE VIDEOWRITER OBJECT
        ## fourcc = cv2.VideoWriter_fourcc(*"MP4V") ## MP4V = .mp4; XVID = .avi
        ## out = cv2.VideoWriter("images/output.mp4", fourcc, 12, (FrameWidth, frame_height)) ## FILE NAME; FourCC Codex; FPS; Frame Size WxH; isColor

        ## TEST PRINT OUTPUT
        print(f"""
            FileName: {FileName}
            FrameCount: {FrameCount}
            FPS: {fps}
            H = {FrameHeight}
            W = {FrameWidth}
            """)
        
        ## TEST PRINT OUTPUT
        ## print(dir(cap))
        
        ## ADD VALUES TO VIDEO CAPTURE DATA OBJECT
        VideoCaptureDataObject["VideoCounter"] = FileCounter
        VideoCaptureDataObject["PathToDirectoryOriginals"] = PathToDirectoryOriginals
        VideoCaptureDataObject["PathToDirectoryGIFsBGRCopies"] = None
        VideoCaptureDataObject["PathToDirectoryGIFsResized"] = None
        VideoCaptureDataObject["PathToDirectoryGIFsThresholdAdaptive_Mean"] = None
        VideoCaptureDataObject["PathToDirectoryGIFsThresholdAdaptive_Gaussian"] = None
        
        VideoCaptureDataObject["FileName"] = FileName
        VideoCaptureDataObject["FrameCount"] = FrameCount 
        VideoCaptureDataObject["FPS"] = fps 
        VideoCaptureDataObject["FrameWidth"] = FrameWidth
        VideoCaptureDataObject["FrameHeight"] = FrameHeight
        VideoCaptureDataObject["AspectRatioOriginal"] = None

        VideoCaptureDataObject["ListForVideoGIFFramesBGR"] = None 
        VideoCaptureDataObject["NPArrayForVideoGIFFramesBGR"] = None
        
        VideoCaptureDataObject["ListForVideoGIFFramesResized"] = None
        VideoCaptureDataObject["NPArrayForVideoGIFFramesResized"] = None
        
        VideoCaptureDataObject["ListForVideoGIFFramesThreshold"] = None
        VideoCaptureDataObject["ListForVideoGIFFramesThreshold_INV"] = None

        VideoCaptureDataObject["ListForVideoGIFFramesThresholdAdaptive_Mean"] = None
        VideoCaptureDataObject["ListForVideoGIFFramesThresholdAdaptive_Gaussian"] = None


        ## TEST PRINT OUTPUT
        print(VideoCaptureDataObject["VideoCounter"])
        print(VideoCaptureDataObject["FileName"])
        print(VideoCaptureDataObject["FrameCount"]) 
        print(VideoCaptureDataObject["FPS"])
        print(VideoCaptureDataObject["FrameWidth"])
        print(VideoCaptureDataObject["FrameHeight"])
        print(VideoCaptureDataObject["AspectRatioOriginal"])

        ## BEGIN WHILE LOOP
        while True:

            ## READ FRAME
            ret, VideoCaptureFrame = cap.read() ## ret=BOOLEAN (AKA: IsTrue), frame=SINGLE SCREENFRAME

            ## CONVERT RGB TO BGR
            ## BELOW

            ## BEGIN IF / ELSE
            if not ret: ## IF A VIDEO FRAME IMAGE IS NOT RETURNED, THEN BOOLEAN BECOMES FALSE AFTER THE LAST FRAME

                ## TEST PRINT OUTPUT
                print("End of video or error occurred.")

                ## CONVERT LIST OF VIDEO GIF FRAMES TO NUMPY ARRAY 
                NPArrayForVideoGIFFramesBGR = np.concatenate(ListForVideoGIFFramesBGR, axis=None) ## FOR LIST OF ARRAYS WITH DIFFERENT SHAPES
                
                ## TEST PRINT OUTPUT
                print(f"Length of NPArrayForVideoGIFFramesBGR: {len(NPArrayForVideoGIFFramesBGR)}")
                print(f"NPArrayForVideoGIFFramesBGR: {NPArrayForVideoGIFFramesBGR}")

                ## UPDATE THE VIDEO CAPTURE DATA OBJECT WITH THE ARRAY OF VIDEO / GIF FRAMES
                VideoCaptureDataObject["NPArrayForVideoGIFFramesBGR"] = NPArrayForVideoGIFFramesBGR

                ## UPDATE THE VIDEO CAPTURE DATA OBJECT WITH LIST OF VIDEO / GIF FRAMES
                VideoCaptureDataObject["ListForVideoGIFFramesBGR"] = ListForVideoGIFFramesBGR ## LENGTH = TOTAL NUMBER OF FRAMES IN THE ANIMATED GIF

                ## EXAMPLE: DictOfVideoCaptureDataObjects[1]['ListForVideoGIFFramesBGR'][0] == SINGLE 2D FRAME FOR TOTAL NUMBER OF FRAMES; DICT 1-INDEXED; LIST 0-INDEXED;
                ## EXAMPLE: DictOfVideoCaptureDataObjects[1]['ListForVideoGIFFramesBGR'][1] == SINGLE 2D FRAME FOR TOTAL NUMBER OF FRAMES; DICT 1-INDEXED; LIST 0-INDEXED;

                ## RESET LIST/ARRAY AND NUMPY ARRAY
                ListForVideoGIFFramesBGR = []
                NPArrayForVideoGIFFramesBGR = None

                ## EXIT THE WHILE LOOP CURRENT ITERATION AND MOVE ON TO NEXT VIDEO/GIF FILE
                break

            ## END IF / ELSE

            ## CONVERT EACH FRAME FROM RGB TO BGR FOR OPEN CV
            ## EachFrameBGR = cv2.cvtColor(VideoCaptureFrame, cv2.COLOR_RGB2BGR)

            ## APPEND EACH VIDEO CAPTURE FRAME TO THE LIST/NP-ARRAY
            ListForVideoGIFFramesBGR.append(VideoCaptureFrame)
        
            """
            ## SHOW THE FRAME - FREEZES THE PROGRAM WITH ANIMATED GIFS
            cv2.imshow("VideoCaptureFrame", VideoCaptureFrame)
            """

            ## WAIT FOR 1ms FOR KEYPRESS TO CONTINUE OR EXIT IF q IS PRESSED
            ## BEGIN IF / ELSE
            if cv2.waitKey(1) & 0xFF == ord('q'):

                break

            ## END IF/ELSE
        
            ## TEST PRINT OUTPUT
            ## print(f"VideoCaptureFrame: {VideoCaptureFrame}")

        ## END WHILE LOOP

        ## UPDATE THE DICTIONARY OF VIDEO CAPTURE DATA OBJECTS FOR THAT FILE COUNTER NUMBER WITH THAT INDIVIDUAL V.C.D.O.
        DictOfVideoCaptureDataObjects[FileCounter] = VideoCaptureDataObject

        ## RELEASE EVERYTHING
        cap.release()
        ## out.release()
        cv2.destroyAllWindows()

        ## RESET 
        VideoCaptureDataObject = {}

        ## INCREMENT COUNTER
        FileCounter += 1
    
    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #1A - OPEN FILES VIDEOS GIFs")

    ## RETURN VARIABLES
    return(DictOfVideoCaptureDataObjects)

## END DEFINE FUNCTION: OPEN LIST OF MULTIPLE VIDEO (GIF) FILES