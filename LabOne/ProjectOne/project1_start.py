import cv2
import numpy as np


def pre_process_image(processed_image):
    # create a look up table, that maps an 8-bit color to 4-bit color
    ary = (np.round(np.linspace(0, 15, num=256)) / 15 * 255).astype(np.uint8)
    processed_image = np.stack([cv2.LUT(processed_image[:, :, i], ary)
                                for i in range(3)], axis=2)
    # use median blur (kernel size 3) to reduce noise from ISO
    processed_image = cv2.medianBlur(processed_image, 3)
    # change the color space from BGR to HSV
    return cv2.cvtColor(processed_image, cv2.COLOR_BGR2HSV)


def post_process_image(original_image, processed_image, segmentation):
    post_processed_img = cv2.bitwise_and(original_image.copy(),
                                         original_image.copy(),
                                         mask=segmentation)
    # extract the contours of all objects and draw them into the image
    contours, _ = cv2.findContours(segmentation, cv2.RETR_TREE,
                                   cv2.CHAIN_APPROX_SIMPLE)
    return cv2.drawContours(post_processed_img, contours, -1, (0, 0, 255), 2)


def select_range(image, col):
    threshold = np.array((cv2.getTrackbarPos("R", "ColorThresholding"),
                          cv2.getTrackbarPos("G", "ColorThresholding"),
                          cv2.getTrackbarPos("B", "ColorThresholding")))
    return cv2.inRange(image, np.maximum(col - threshold, np.array((0, 0, 0))),
                       np.minimum(col + threshold, np.array((255, 255, 255))))


def on_scale(new_val):
    pass


def on_mouse(event, x, y, flags, user_data, img_store, col):
    if event != cv2.EVENT_LBUTTONDOWN:
        return

    if img_store is None:
        return

    col[:] = img_store[y, x, :]


if __name__ == "__main__":
    image_store = None
    color = np.array((0, 0, 0))
    cv2.startWindowThread()
    cv2.namedWindow("ColorThresholding")
    cv2.setMouseCallback("ColorThresholding", (lambda event, x, y,
                                               flags, user_data:
                                               on_mouse(event, x, y, flags,
                                                        user_data, image_store,
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
        frame_pre_processed = pre_process_image(frame)
        # store image to select color via mouse-click
        image_store = frame_pre_processed
        # processing
        mask = select_range(frame_pre_processed, color)
        # post-processing
        post_processed_image = post_process_image(frame, frame_pre_processed,
                                                  mask)
        # display the final image
        cv2.imshow("ColorThresholding", post_processed_image)
        # close if the window is closed or escape is pressed
        k = cv2.waitKey(1)

        if k % 256 == 27:
            print("Escape hit, closing...")
            break
