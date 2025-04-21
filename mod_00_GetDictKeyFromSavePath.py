## IMPORT MODULES
import cv2

## BEGIN CHECK FILE TYPE
def fn_GetDictKeyFromSavePath(PathToDirectorySaved):

    """
        DOC STRING HERE
    """

    ## TEST PRINT OUTPUT
    print(f"\nBEGIN FUNCTION #00 - GET DICT KEY FROM SAVE PATH")

    ## MATCH CASE OF PATH OF DIRECTORY WHERE THE IMAGES ARE SAVED IN ORDER TO GET CORRECT DICT KEY TO ACCESS THE VIDEO CAPTURE DATA OBJECT
    match PathToDirectorySaved:

        case 'images_originals/': ## CONTAINS ALL IMAGES TYPES: .GIFS; .JPGS; .JPEGS; .PNG, ETC.

            KEY_4_VideoCaptureDataObject = "ListForVideoGIFFramesBGR" ## NOT ACTUALLY ORIGINAL BUT THIS IS WHERE OPENCV BGR FORMAT COPIES OF ORIGINALS ARE SAVED

        case 'images_gifs_bgr_copies/': ## CONTAINS COPIES OF THE ORIGINAL GIF IMAGES IN OPENCV BGR FORMAT

            KEY_4_VideoCaptureDataObject = "ListForVideoGIFFramesBGR"

        case 'images_gifs_resized_anyformat/': ## CONTAINS COPIES OF THE ORIGINAL GIF IMAGES RESIZED IN WHATEVER GIVEN COLOR FORMAT

            KEY_4_VideoCaptureDataObject = "ListForVideoGIFFramesResized"

        case 'images_gifs_gray/':  ## CONTAINS COPIES OF THE ORIGINAL GIF IMAGES IN GRAYSCALE FORMAT

            KEY_4_VideoCaptureDataObject = "ListForVideoGIFFramesGRAY"
            
        case 'images_gifs_rgb/': ## CONTAINS COPIES OF THE ORIGINAL GIF IMAGES IN STANDARD RGB FORMAT

            KEY_4_VideoCaptureDataObject = "ListForVideoGIFFramesRGB"

        case 'images_gifs_hsv/': ## CONTAINS COPIES OF THE ORIGINAL GIF IMAGES IN HSV FORMAT

            KEY_4_VideoCaptureDataObject = "ListForVideoGIFFramesHSV"

        case 'images_gifs_gaussian_blur/': ## CONTAINS COPIES OF THE ORIGINAL GIF IMAGES FILTERED THROUGH GAUSSIAN FILTER

            KEY_4_VideoCaptureDataObject = "ListForVideoGIFFramesGaussianBlur"

        case 'images_gifs_threshold/': ## CONTAINS COPIES OF THE ORIGINAL GIF IMAGES AS THRESHOLDS

            KEY_4_VideoCaptureDataObject = "ListForVideoGIFFramesThreshold"

        case 'images_gifs_threshold_INV/': ## CONTAINS COPIES OF THE ORIGINAL GIF IMAGES AS THRESHOLDS

            KEY_4_VideoCaptureDataObject = "ListForVideoGIFFramesThreshold_INV"

        case 'images_gifs_threshold_adaptive_mean/': ## CONTAINS COPIES OF THE ORIGINAL GIF IMAGES AS THRESHOLDS

            KEY_4_VideoCaptureDataObject = "ListForVideoGIFFramesThresholdAdaptive_Mean"

        case 'images_gifs_threshold_adaptive_gaussian/': ## CONTAINS COPIES OF THE ORIGINAL GIF IMAGES AS THRESHOLDS

            KEY_4_VideoCaptureDataObject = "ListForVideoGIFFramesThresholdAdaptive_Gaussian"

                            

    ## TEST PRINT OUTPUT
    print(f"\nEND FUNCTION #00 - GET DICT KEY FROM SAVE PATH")

    ## RETURN VARIABLES
    return(KEY_4_VideoCaptureDataObject)

## END DEFINE FUNCTION

## RETURNS. E.G.:

"""

"""