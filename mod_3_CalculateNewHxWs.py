## IMPORT MODULES
import cv2

## BEGIN CHECK FILE TYPE
def fn_CalculateNewHxWs(DictOfImageDataObjects, HeightNew=None, WidthNew=None):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #3 - CALCULATE NEW H x Ws")
    
    ## DECLARE VARIABLES
    FileCounter = 1

    ## BEGIN FOR LOOP
    for k, ImageDataObject in DictOfImageDataObjects.items():

        ## BEGIN IF / ELSE
        if HeightNew: ## IF EXISTS 
            
            ImageDataObject["HeightNew"] = HeightNew 
            GivenDimension = "HeightNew"

        elif WidthNew: ## IF EXISTS
        
            ImageDataObject["WidthNew"] = WidthNew
            GivenDimension = "WidthNew"

        elif (HeightNew == None and WidthNew == None):

            GivenDimension = None

        ## END IF / ELSE

        ## DEFINE NEW WIDTH AND HEIGHT WHILE MAINTAINING ASPECT RATIO
        
        ## GET ASPECT RATIO + W x H DATA
        WidthOriginal = ImageDataObject["WidthOriginal"]
        HeightOriginal = ImageDataObject["HeightOriginal"]
        AspectRatioOriginal = ImageDataObject["AspectRatioOriginal"]

        ## BEGIN MATCH CASE
        match GivenDimension:

            ## A = W / H

            ## W = A * H

            ## H = W / A
        
            case "WidthNew": 

                ## COMPUTE HEIGHT BASED ON ASPECT RATIO
                HeightNew = int(WidthNew / AspectRatioOriginal) ## H = W / A

                ## GET ASPECT RATIO
                AspectRatioNew = WidthNew / HeightNew # A = W / H

                ## GET NEW RATIO OF NEW TO ORIGINAL 
                RatioNewToOriginal = HeightNew / HeightOriginal 
                
                ## ADD NEW HEIGHT TO IMAGE DATA OBJECT
                ImageDataObject["HeightNew"] = HeightNew

            case "HeightNew":
                
                ## COMPUTE WIDTH BASED ON ASPECT RATIO
                WidthNew = int(AspectRatioOriginal * HeightNew) ## W = A * H

                ## GET ASPECT RATIO
                AspectRatioNew = WidthNew / HeightNew # A = W / H

                ## GET NEW RATIO OF NEW TO ORIGINAL 
                RatioNewToOriginal = WidthNew / WidthOriginal

                ## ADD NEW WIDTH TO IMAGE DATA OBJECT
                ImageDataObject["WidthNew"] = WidthNew

            case None:

                print(f"ERROR: It is not possible to call this function without at least one given variable for Height (H) or Width (W).")
                break

        ## END MATCH CASE

        ## CREATE NEW KEY/VALUE PAIR IN IMAGE DATA OBJECT
        ImageDataObject["AspectRatioNew"] = AspectRatioNew

        ## CREATE NEW KEY/VALUE PAIR IN IMAGE DATA OBJECT
        ImageDataObject["RatioNewToOriginal"] = RatioNewToOriginal

        ## ADD IMAGE DATA OBJECT TO DICTIONARY OF IMAGE DATA OBJECTS
        DictOfImageDataObjects[k] = ImageDataObject
         
        ## TEST PRINT OUTPUT
        print(f"ImageDataObject: {ImageDataObject}")
                
        ## TEST PRINT OUTPUT
        ## print(f"KEY: {FileCounter} OR {k}; OLD DIMENSIONS: H = {ImageDataObject["HeightOriginal"]}, W = {ImageDataObject["WidthOriginal"]}, AspectRatioOriginal = {ImageDataObject["AspectRatioOriginal"]}")
        ## print(f"KEY: {FileCounter} OR {k}: NEW DIMENSIONS: H = {ImageDataObject["HeightNew"]}, W = {ImageDataObject["WidthNew"]}, AspectRatioNew = {ImageDataObject["AspectRatioNew"]}")
              
        ## INCREMENT FILE COUNTER
        FileCounter += 1
    
        ## TEST PRINT OUTPUT
        ## print(DictOfImageDataObjects)

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #3 - CALCULATE NEW H x Ws")

    ## RETURN VARIABLES
    return(DictOfImageDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""