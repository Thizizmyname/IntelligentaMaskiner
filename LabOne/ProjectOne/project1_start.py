import cv2
import numpy as np


def preprocess_image(image):
    # change color space for more robust thresholding
    processed_image = image

    # create a look up table, that maps an 8-bit color to 4-bit color
    # TODO: Exercise 3

    # use median blur (kernel size 3) to redice noise from ISO
    # TODO: Exercise 3

    # change the color space from BGR to HSV
    # TODO: Exercise 2

    return processed_image


def postprocess_image(original_image, processed_image, segmentation):
    postprocessed_image = cv2.bitwise_and(original_image,
                                          original_image,
                                          mask=segmentation)

    # exctract the contours of all objects and draw them into the image
    # TODO: Exercise 3

    return postprocessed_image


def selectRange(image, color):
    low = (0, 0, 0)
    high = (255, 255, 255)
    threshold = np.array((cv2.getTrackbarPos("R", "ColorThresholding"),
                          cv2.getTrackbarPos("G", "ColorThresholding"),
                          cv2.getTrackbarPos("B", "ColorThresholding")))

    # compute the low and high boundaries for each channel
    # TODO: Exercise 1

    mask = cv2.inRange(image, low, high)
    return mask


def on_scale(new_value):
    pass


def on_mouse(event, x, y, flags, userdata, image_store, color):
    if event != cv2.EVENT_LBUTTONDOWN:
        return

    if image_store is None:
        return

    color[:] = image_store[y, x, :]
    return

if __name__ == "__main__":
    image_store = None
    color = np.array((0, 0, 0))

    cv2.startWindowThread()
    cv2.namedWindow("ColorThresholding")
    cv2.setMouseCallback("ColorThresholding", (lambda event, x, y,
                                               flags, userdata:
                                               on_mouse(event, x, y, flags,
                                                        userdata, image_store,
                                                        color)))
    cv2.createTrackbar("R", "ColorThresholding", 255, 255, on_scale)
    cv2.createTrackbar("G", "ColorThresholding", 255, 255, on_scale)
    cv2.createTrackbar("B", "ColorThresholding", 255, 255, on_scale)

    cam = cv2.VideoCapture(0)

    while cv2.getWindowProperty('ColorThresholding', 0) != -1:
        # raw image capture and preparation
        ret, frame = cam.read()
        if not ret:
            print("Could not get a frame from the camera, exiting.")
            break

        # pre-processing
        frame_preprocessed = preprocess_image(frame)

        # store image to select color via mouseclick
        image_store = frame_preprocessed

        # processing
        mask = selectRange(frame_preprocessed, color)

        # post-processing
        postprocessed_image = postprocess_image(frame, frame_preprocessed, mask)

        # display the final image
        cv2.imshow("ColorThresholding", postprocessed_image)

        # close if the window is closed or escape is pressed
        k = cv2.waitKey(1)
        if k % 256 == 27:
            print("Escape hit, closing...")
            break
