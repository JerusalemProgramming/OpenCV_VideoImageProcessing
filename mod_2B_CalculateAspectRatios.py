## IMPORT MODULES
import cv2
import mod_2A_CalculateAspectRatio

## BEGIN CHECK FILE TYPE
def fn_CalculateAspectRatios(DictOfImageDataObjects):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #2B - CALCULATE ASPECT RATIOS")

    ## DECLARE VARIABLES
    FileCounter = 1

    ## BEGIN FOR LOOP
    for k, ImageDataObject in DictOfImageDataObjects.items():

        ## DECLARE VARIABLES
        ## N/A

        ## IF WIDTH AND HEIGHT OF ORIGINAL IMAGE EXIST, THEN...
        if ImageDataObject["WidthOriginal"] and ImageDataObject["HeightOriginal"]:

            ## GET WIDTH AND HEIGHT PARAMETERS OF ORIGINAL IMAGE FRAME
            WidthParameter = ImageDataObject["WidthOriginal"]
            HeightParameter = ImageDataObject["HeightOriginal"]

            ## CALL FUNCTION #2A - CALCULATE ASPECT RATIO
            ## CALL FUNCTION 2A - RECEIVES INDIVIDUAL WIDTH x HEIGHT PARAMETERS FOR DYNAMIC CALCULATION OF ASPECT RATIO
            AspectRatio = mod_2A_CalculateAspectRatio.fn_CalculateAspectRatio(WidthParameter, HeightParameter)

            ## UPDATE IMAGE DATA OBJECT ## ADD ASPECT RATIO TO IMAGE DATA OBJECT
            ImageDataObject["AspectRatioOriginal"] = AspectRatio

        else:

            pass

        ## IF WIDTH AND HEIGHT OF RESIZED IMAGE (ANY RESIZE UP OR DOWN BY ASPECT RATIO) EXIST, THEN...
        if ImageDataObject["WidthNew"] and ImageDataObject["HeightNew"]:

            ## GET WIDTH AND HEIGHT PARAMETERS OF NEW RESIZED IMAGE (GENERAL - ANY RESIZE UP OR DOWN BY ASPECT RATIO)
            WidthParameter = ImageDataObject["WidthNew"]
            HeightParameter = ImageDataObject["HeightNew"]

            ## CALL FUNCTION #2A - CALCULATE ASPECT RATIO
            ## CALL FUNCTION 2A - RECEIVES INDIVIDUAL WIDTH x HEIGHT PARAMETERS FOR DYNAMIC CALCULATION OF ASPECT RATIO
            AspectRatio = mod_2A_CalculateAspectRatio.fn_CalculateAspectRatio(WidthParameter, HeightParameter)

            ## UPDATE IMAGE DATA OBJECT ## ADD ASPECT RATIO TO IMAGE DATA OBJECT
            ImageDataObject["AspectRatioNew"] = AspectRatio

        else:

            pass

        ## IF WIDTH AND HEIGHT OF RESIZED IMAGE DOWN BY INTERPOLIATION EXIST, THEN...
        if ImageDataObject["WidthNewDown"] and ImageDataObject["HeightNewDown"]:

            ## GET WIDTH AND HEIGHT PARAMETERS OF RESIZED IMAGE DOWN BY INTERPOLATION
            WidthParameter = ImageDataObject["WidthNewDown"]
            HeightParameter = ImageDataObject["HeightNewDown"]

            ## CALL FUNCTION #2A - CALCULATE ASPECT RATIO
            ## CALL FUNCTION 2A - RECEIVES INDIVIDUAL WIDTH x HEIGHT PARAMETERS FOR DYNAMIC CALCULATION OF ASPECT RATIO
            AspectRatio = mod_2A_CalculateAspectRatio.fn_CalculateAspectRatio(WidthParameter, HeightParameter)

            ## UPDATE IMAGE DATA OBJECT ## ADD ASPECT RATIO TO IMAGE DATA OBJECT
            ImageDataObject["AspectRatioNewDown"] = AspectRatio

        else:

            pass

        ## IF WIDTH AND HEIGHT OF RESIZED IMAGE UP BY INTERPOLIATION EXIST, THEN...
        if ImageDataObject["WidthNewUp"] and ImageDataObject["HeightNewUp"]:

            WidthParameter = ImageDataObject["WidthNewUp"]
            HeightParameter = ImageDataObject["HeightNewUp"]

            ## CALL FUNCTION #2A - CALCULATE ASPECT RATIO
            ## CALL FUNCTION 2A - RECEIVES INDIVIDUAL WIDTH x HEIGHT PARAMETERS FOR DYNAMIC CALCULATION OF ASPECT RATIO
            AspectRatio = mod_2A_CalculateAspectRatio.fn_CalculateAspectRatio(WidthParameter, HeightParameter)

            ## UPDATE IMAGE DATA OBJECT ## ADD ASPECT RATIO TO IMAGE DATA OBJECT
            ImageDataObject["AspectRatioNewUp"] = AspectRatio

        else:

            pass

        ## INCREMENT FILE COUNTER
        FileCounter += 1

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #2B - CALCULATE ASPECT RATIOS")

    ## RETURN VARIABLES
    return(DictOfImageDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""