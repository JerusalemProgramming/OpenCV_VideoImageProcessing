## IMPORT MODULES
import cv2

## BEGIN CHECK FILE TYPE
def fn_OpenFilesImagesNonGIFs(PathToDirectory, ListOfOthers):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #1B - OPEN FILES IMAGES NON GIFS")

    ## DECLARE VARIABLES
    DictOfImageDataObjects = {} ## {1: {  }, 2: {  }, 3: {  } }
    ImageDataObject = {} ## 
    FileCounter = 1

    ## BEGIN FOR LOOP
    for FileName in ListOfOthers:

        ## DECLARE VARIABLES
        ListTemp = []

        ## LOAD IMAGE 
        PathToImage = f"{PathToDirectory}{FileName}"

        ## TEST PRINT OUTPUT
        ## print(f"PathToImage: {PathToImage}")

        ## LOAD IMAGE
        ## DEFAULT: BGR COLOR
        ImageFrameOriginal = cv2.imread(PathToImage, cv2.IMREAD_COLOR)

        ## AS-IS (INCLUDES ALPHA IF AVAILABLE)
        ## ImageFrameOriginal = cv2.imread(PathToImage, cv2.IMREAD_UNCHANGED) 

        ## GET ORIGINAL DIMENSIONS
        HeightOriginal, WidthOriginal = ImageFrameOriginal.shape[:2]
        ImageFrameOriginalShape = ImageFrameOriginal.shape

        ## TEST PRINT OUTPUT
        print(f"\nFileCounter: {FileCounter}")
        print(f"FileName: {FileName}")
        print(f"ImageFrameOriginal.shape: {ImageFrameOriginal.shape}")
        print("Data type = {}".format(ImageFrameOriginal.dtype))
        print("Object type = {}".format(type(ImageFrameOriginal)))
        print("Image Dimensions/Shape = {}".format(ImageFrameOriginal.shape))
        print("Image Size (in px) = {}".format(ImageFrameOriginal.size))

        ## ADD VALUES TO IMAGE DATA (DICTIONARY) OBJECT
        ImageDataObject["FileCounter"] = FileCounter
        ImageDataObject["FileName"] = FileName
        ImageDataObject["WidthOriginal"] = WidthOriginal
        ImageDataObject["HeightOriginal"] = HeightOriginal
        ImageDataObject["AspectRatioOriginal"] = None
        ImageDataObject["ImageFrameOriginalShape"] = ImageFrameOriginalShape ## <class 'tuple'>, e.g. (239, 162, 3)
        ImageDataObject["ImageFrameOriginal"] = ImageFrameOriginal ## <class 'numpy.ndarray'>
        
        ImageDataObject["WidthNew"] = None
        ImageDataObject["HeightNew"] = None
        ImageDataObject["AspectRatioNew"] = None
        ImageDataObject["RatioNewToOriginal"] = None

        ImageDataObject["WidthNewDown"] = None
        ImageDataObject["HeightNewDown"] = None
        ImageDataObject["AspectRatioNewDown"] = None
        ImageDataObject["RatioNewToOriginalDown"] = None

        ImageDataObject["WidthNewUp"] = None
        ImageDataObject["HeightNewUp"] = None
        ImageDataObject["AspectRatioNewUp"] = None
        ImageDataObject["RatioNewToOriginalUp"] = None

        ImageDataObject["ImageFrameResized"] = None
        ImageDataObject["ImageFrameResizedDown"] = None
        ImageDataObject["ImageFrameResizedUp"] = None

        ImageDataObject["ImageFrameResizedShape"] = None
        ImageDataObject["ImageFrameResizedDownShape"] = None
        ImageDataObject["ImageFrameResizedUpShape"] = None
        ## ImageDataObject[""] = None

        ## ADD IMAGE DATA (DICTIONARY) OBJECT TO DICT OF IMAGE DATA OBJECTS
        DictOfImageDataObjects[FileCounter] = ImageDataObject

        ## INCREMENT FILE COUNTER
        FileCounter += 1

        ImageDataObject = {} ## RESET TO EMPTY DICTIONARY OBJECT
    
        ## TEST PRINT OUTPUT
        ## print(DictOfImageDataObjects)

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #1B - OPEN FILES IMAGES NON GIFS")

    ## RETURN VARIABLES
    return(DictOfImageDataObjects)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""