## IMPORT MODULES
import cv2
import numpy as np
import matplotlib.pyplot as plt
import mod_0_CheckFileTypes
import mod_1A_OpenFilesVideosGIFs
import mod_00_CalculateDurationFromFPS
import mod_00_ConvertFrameBGR2RGB
import mod_00_ConvertFrameBGR2GRAY
import mod_00_ConvertFrameBGR2HSV
import mod_00_ConvertFrameRGB2BGR
import mod_00_ConvertFrameRGB2GRAY
import mod_00_ConvertFrameRGB2HSV
import mod_00_ConvertFrameGaussianBlur

import mod_00_ConvertFrameThreshold
import mod_00_ConvertFrameThresholdAdaptive_Mean
import mod_00_ConvertFrameThresholdAdaptive_Gaussian
import mod_00_ConvertFrameBGR2PILImage
import mod_00_ConvertFrameRGB2PILImage

import mod_1AA_ResizeVideosGIFsViaScale
import mod_1B_OpenFilesImagesNonGIFs
import mod_2A_CalculateAspectRatio
import mod_2B_CalculateAspectRatios
import mod_3_CalculateNewHxWs
import mod_4A_ResizeImageFramesViaAspectRatioWxH
import mod_4B_ResizeImageFramesViaInterpolation
import mod_99_WriteImageFiles
import mod_99_WriteVideoGIFFiles

## DECLARE VARIABLES
Threshold = 162

## PATH TO IMAGE DIRECTORY
PathToDirectoryOriginals = 'images_originals/' ## CONTAINS ALL IMAGES TYPES: .GIFS; .JPGS; .JPEGS; .PNG, ETC.

## FOR SINGLE FRAME IMAGES: .JPG, .PNG, ETC.
PathToDirectoryResized = 'images_resized_any_way/' ## CONTAINS IMAGES RESIZED VIA ASPECT RATIO OF W VS. H
PathToDirectoryResizedDown = 'images_resized_down/' ## CONTAINS SCALED DOWN IMAGES VIA INTERPOLATION
PathToDirectoryResizedUp = 'images_resized_up/' ## CONTAINS SCALED UP IMAGES VIA INTERPOLATION

## FOR ANIMATED GIFS
PathToDirectoryGIFsBGRCopies = 'images_gifs_bgr_copies/' ## CONTAINS COPIES OF THE ORIGINAL GIF IMAGES IN OPENCV BGR FORMAT
PathToDirectoryGIFsResized = 'images_gifs_resized_anyformat/' ## CONTAINS RESIZED COPIES OF THE ORIGINAL GIF IMAGES IN OPENCV BGR FORMAT
PathToDirectoryGIFsRGB = 'images_gifs_rgb/' ## CONTAINS COPIES OF THE ORIGINAL GIF IMAGES IN STANDARD RGB FORMAT
PathToDirectoryGIFsGRAY = 'images_gifs_gray/' ## CONTAINS COPIES OF THE ORIGINAL GIF IMAGES IN GRAYSCALE FORMAT
PathToDirectoryGIFsHSV = 'images_gifs_hsv/' ## CONTAINS COPIES OF THE ORIGINAL GIF IMAGES IN HSV FORMAT
PathToDirectoryGIFsGaussianBlur = 'images_gifs_gaussian_blur/' ## CONTAINS COPIES OF THE ORIGINAL GIF FILTERED THROUGH GAUSSIAN BLUR
PathToDirectoryGIFsThreshold = 'images_gifs_threshold/' ## CONTAINS COPIES OF THRESHOLD GIF IMAGES
PathToDirectoryGIFsThreshold_INV = 'images_gifs_threshold_INV/' ## CONTAINS COPIES OF THRESHOLD GIF IMAGES
PathToDirectoryGIFsThresholdAdaptive_Mean = 'images_gifs_threshold_adaptive_mean' ## CONTAINS COPIES OF THRESHOLD GIF IMAGES ## ERROR WITH THIS
PathToDirectoryGIFsThresholdAdaptive_Gaussian = 'images_gifs_threshold_adaptive_gaussian/' ## CONTAINS COPIES OF THRESHOLD GIF IMAGES


## BEGIN MAIN PROGRAM

## CALL FUNCTION 0
ListOfFileNamesInDirectory, ListOfGIFs, ListOfOthers, SetOfExtensions = mod_0_CheckFileTypes.fn_CheckFileTypes(PathToDirectoryOriginals)

## CALL FUNCTION 1A 
DictOfVideoCaptureDataObjects = mod_1A_OpenFilesVideosGIFs.fn_OpenFilesVideos(ListOfGIFs, PathToDirectoryOriginals)

## CALL FUNCTION 00
DictOfVideoCaptureDataObjects = mod_00_CalculateDurationFromFPS.fn_CalculateDurationFromFPS(DictOfVideoCaptureDataObjects)

## CALL FUNCTION 00
DictOfVideoCaptureDataObjects = mod_00_ConvertFrameBGR2RGB.fn_ConvertFrameBGR2RGB(DictOfVideoCaptureDataObjects)

## CALL FUNCTION 00
## DictOfVideoCaptureDataObjects = mod_00_ConvertFrameBGR2GRAY.fn_ConvertFrameBGR2GRAY(DictOfVideoCaptureDataObjects)

## CALL FUNCTION 00
## DictOfVideoCaptureDataObjects = mod_00_ConvertFrameBGR2HSV.fn_ConvertFrameBGR2HSV(DictOfVideoCaptureDataObjects)

## CALL FUNCTION 00
## DictOfVideoCaptureDataObjects = mod_00_ConvertFrameRGB2BGR.fn_ConvertFrameRGB2BGR(DictOfVideoCaptureDataObjects)
 
## CALL FUNCTION 00
DictOfVideoCaptureDataObjects = mod_00_ConvertFrameRGB2GRAY.fn_ConvertFrameRGB2GRAY(DictOfVideoCaptureDataObjects)

## CALL FUNCTION 00
## DictOfVideoCaptureDataObjects = mod_00_ConvertFrameRGB2HSV.fn_ConvertFrameRGB2HSV(DictOfVideoCaptureDataObjects)

## CALL FUNCTION 00
DictOfVideoCaptureDataObjects = mod_00_ConvertFrameGaussianBlur.fn_ConvertFrameGaussianBlur(DictOfVideoCaptureDataObjects)

## CALL FUNCTION 00
## DictOfVideoCaptureDataObjects = mod_00_ConvertFrameThreshold.fn_ConvertFrameThreshold(DictOfVideoCaptureDataObjects, Threshold)

## CALL FUNCTION 00
## DictOfVideoCaptureDataObjects = mod_00_ConvertFrameThresholdAdaptive_Mean.fn_ConvertFrameThresholdAdaptive_Mean(DictOfVideoCaptureDataObjects)

## CALL FUNCTION 00
## DictOfVideoCaptureDataObjects = mod_00_ConvertFrameThresholdAdaptive_Gaussian.fn_ConvertFrameThresholdAdaptive_Gaussian(DictOfVideoCaptureDataObjects)

## CALL FUNCTION 1AA - ## fn_ResizeVideosGIFsViaScale(DictOfVideoCaptureDataObjects, PathToDirectoryOriginals, PathToDirectorySaved)
## DictOfVideoCaptureDataObjects = mod_1AA_ResizeVideosGIFsViaScale.fn_ResizeVideosGIFsViaScale(DictOfVideoCaptureDataObjects, PathToDirectoryOriginals, PathToDirectoryGIFsResized)

## CALL FUNCTION 1B - EACH IMAGE DATA OBJECT RETURNED IN DYNAMIC (X-ELEMENT) LIST HAS SIX (6) KEY/VALUE PAIRS HERE WHEN IT IS CREATED
## DictOfImageDataObjects = mod_1B_OpenFilesImagesNonGIFs.fn_OpenFilesImagesNonGIFs(PathToDirectoryOriginals, ListOfOthers)

## CALL FUNCTION 2A - RECEIVES INDIVIDUAL IMAGE FRAME WIDTH x HEIGHT PARAMETERS FOR DYNAMIC CALCULATION OF ASPECT RATIO
## AspectRatio = mod_2A_CalculateAspectRatio.fn_CalculateAspectRatio(Width, Height)

## CALL FUNCTION 2B - RECEIVES THE DICTIONARY OF IMAGE DATA OBJECTS AND RETURNS THE SAME MODIFIED DICT OBJECT
## DictOfImageDataObjects = mod_2B_CalculateAspectRatios.fn_CalculateAspectRatios(DictOfImageDataObjects)

## CALL FUNCTION 3 - RECEIVES THE DICTIONARY OF IMAGE DATA OBJECTS AND RETURNS THE SAME MODIFIED DICT OBJECT
## DictOfImageDataObjects = mod_3_CalculateNewHxWs.fn_CalculateNewHxWs(DictOfImageDataObjects, HeightNew=None, WidthNew=162)

## CALL FUNCTION 4A - RECEIVES THE DICTIONARY OF IMAGE DATA OBJECTS AND RETURNS THE SAME MODIFIED DICT OBJECT
## DictOfImageDataObjects = mod_4A_ResizeImageFramesViaAspectRatioWxH.fn_ResizeImageFrames(DictOfImageDataObjects)

## CALL FUNCTION 4B - RECEIVES THE DICTIONARY OF IMAGE DATA OBJECTS AND RETURNS THE SAME MODIFIED DICT OBJECT
## DictOfImageDataObjects = mod_4B_ResizeImageFramesViaInterpolation.fn_ResizeImageFramesViaInterpolation(DictOfImageDataObjects)

## CALL FUNCTION 99 - RECEIVES THE DICTIONARY OF IMAGE DATA OBJECTS AND WRITES RESIZED IMAGE FILES TO NEW FOLDER FOR RESIZED IMAGES
## _ = mod_99_WriteImageFiles.fn_WriteImageFiles(PathToDirectoryResized, PathToDirectoryResizedDown, PathToDirectoryResizedUp, DictOfImageDataObjects)

## CALL FUNCTION 99 - RECEIVES THE DICTIONARY OF IMAGE DATA OBJECTS AND WRITES RESIZED IMAGE FILES TO NEW FOLDER FOR RESIZED IMAGES
## _ = mod_99_WriteVideoGIFFiles.fn_WriteVideoGIFFiles(DictOfVideoCaptureDataObjects, PathToDirectoryGIFsBGRCopies)

## CALL FUNCTION 99 - RECEIVES THE DICTIONARY OF IMAGE DATA OBJECTS AND WRITES RESIZED IMAGE FILES TO NEW FOLDER FOR RESIZED IMAGES
## _ = mod_99_WriteVideoGIFFiles.fn_WriteVideoGIFFiles(DictOfVideoCaptureDataObjects,PathToDirectoryGIFsRGB)

## CALL FUNCTION 99 - RECEIVES THE DICTIONARY OF IMAGE DATA OBJECTS AND WRITES RESIZED IMAGE FILES TO NEW FOLDER FOR RESIZED IMAGES
_ = mod_99_WriteVideoGIFFiles.fn_WriteVideoGIFFiles(DictOfVideoCaptureDataObjects, PathToDirectoryGIFsGRAY)

## CALL FUNCTION 99 - RECEIVES THE DICTIONARY OF IMAGE DATA OBJECTS AND WRITES RESIZED IMAGE FILES TO NEW FOLDER FOR RESIZED IMAGES
## _ = mod_99_WriteVideoGIFFiles.fn_WriteVideoGIFFiles(DictOfVideoCaptureDataObjects, PathToDirectoryGIFsHSV)

## CALL FUNCTION 99 - RECEIVES THE DICTIONARY OF IMAGE DATA OBJECTS AND WRITES RESIZED IMAGE FILES TO NEW FOLDER FOR RESIZED IMAGES
_ = mod_99_WriteVideoGIFFiles.fn_WriteVideoGIFFiles(DictOfVideoCaptureDataObjects, PathToDirectoryGIFsGaussianBlur)

## CALL FUNCTION 99 - RECEIVES THE DICTIONARY OF IMAGE DATA OBJECTS AND WRITES RESIZED IMAGE FILES TO NEW FOLDER FOR RESIZED IMAGES
## _ = mod_99_WriteVideoGIFFiles.fn_WriteVideoGIFFiles(DictOfVideoCaptureDataObjects, PathToDirectoryGIFsThreshold)

## CALL FUNCTION 99 - RECEIVES THE DICTIONARY OF IMAGE DATA OBJECTS AND WRITES RESIZED IMAGE FILES TO NEW FOLDER FOR RESIZED IMAGES
## _ = mod_99_WriteVideoGIFFiles.fn_WriteVideoGIFFiles(DictOfVideoCaptureDataObjects, PathToDirectoryGIFsThreshold_INV)

## ERROR WITH THE FUNCTION BELOW
## CALL FUNCTION 99 - RECEIVES THE DICTIONARY OF IMAGE DATA OBJECTS AND WRITES RESIZED IMAGE FILES TO NEW FOLDER FOR RESIZED IMAGES
## _ = mod_99_WriteVideoGIFFiles.fn_WriteVideoGIFFiles(DictOfVideoCaptureDataObjects, PathToDirectoryGIFsThresholdAdaptive_Mean)

## CALL FUNCTION 99 - RECEIVES THE DICTIONARY OF IMAGE DATA OBJECTS AND WRITES RESIZED IMAGE FILES TO NEW FOLDER FOR RESIZED IMAGES
## _ = mod_99_WriteVideoGIFFiles.fn_WriteVideoGIFFiles(DictOfVideoCaptureDataObjects, PathToDirectoryGIFsThresholdAdaptive_Gaussian)


## SHOW RESIZED IMAGE
## cv2.imshow("Resized Image", FrameResized)
## cv2.waitKey(0)
## cv2.destroyAllWindows()

## TEST PRINT OUTPUT
## print(img)
## print(img[0,0])
print("TEST")

"""
FourCC4AVI = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
FourCC4MP4 = cv2.VideoWriter_fourcc(*'XVID')

## DEFINE CODEC
VideoOutputAVI = cv2.VideoWriter(FileName, FourCC4AVI, 10, (FrameWidth, FrameHeight)) ## VideoWriter object = cv.VideoWriter(filename, fourcc, fps, frameSize )

VideoOutputMP4 = cv2.VideoWriter(FileName, FourCC4MP4, 10, (FrameWidth, FrameHeight))


"""