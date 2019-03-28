import pyrealsense2 as rs
import numpy as np
import cv2


def create_camera_configuration():
    image_size = (640, 480)
    new_config = rs.config()
    new_config.enable_stream(rs.stream.color, image_size[0], image_size[1],
                             rs.format.bgr8, 30)
    new_config.enable_stream(rs.stream.depth, image_size[0], image_size[1],
                             rs.format.z16, 30)
    return new_config


def create_segmentation_mask(x_pos, y_pos, wdth, hght, img, depth_img):
    mask = np.ones((img.shape[0], img.shape[1]))
    # compute the mean distance to the face
    mean_dist = np.mean(depth_img[y_pos:y_pos + hght, x_pos:x_pos + wdth])
    # compute the threshold values for distances to be shown
    low, hgh = max(mean_dist - clpng_dst, 0), min(mean_dist + clpng_dst, 255)
    # apply the threshold by selecting only those pixels that lie within
    mask[np.logical_and(depth_img > low, depth_img < hgh)] = 1.0
    return mask


if __name__ == "__main__":
    cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
    background = np.zeros((480, 640, 3))
    # pre-trained haar-cascade classifier data
    face_cascade = cv2.CascadeClassifier('frontal_face_features.xml')
    # configure the real-sense camera
    pipeline = rs.pipeline()
    config = create_camera_configuration()
    frame_aligner = rs.align(rs.stream.color)
    clipping_distance_meters = 0.2
    # Start streaming
    profile = pipeline.start(config)
    depth_sensor = profile.get_device().first_depth_sensor()
    depth_scale = depth_sensor.get_depth_scale()
    clpng_dst = clipping_distance_meters / depth_scale

    try:
        while cv2.getWindowProperty('RealSense', 0) != -1:
            # get a raw image into the pipeline
            frames = pipeline.wait_for_frames()
            aligned_frames = frame_aligner.process(frames)
            depth_frame = aligned_frames.get_depth_frame()
            color_frame = aligned_frames.get_color_frame()
            # Pre-processing
            # image to display (normalized float bgr)
            image = np.asanyarray(color_frame.get_data()).astype(np.float32)
            image -= np.min(image[:])
            image /= np.max(image[:])
            # convert to gray-scale (uint8)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray_image -= np.min(gray_image[:])
            gray_image /= np.max(gray_image[:])
            gray_image_uint = gray_image * 255
            gray_image_uint = gray_image_uint.astype(np.uint8)
            # Processing
            faces = face_cascade.detectMultiScale(gray_image_uint, 1.3, 5)

            if len(faces) > 0:
                mask = np.zeros((image.shape[0], image.shape[1]))
                depth_image = np.asanyarray(depth_frame.get_data())

                for (x, y, w, h) in faces:
                    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    person_mask = create_segmentation_mask(x, y, w, h, image,
                                                           depth_image)
                    mask = np.logical_or(mask, person_mask)
            else:
                mask = np.ones((image.shape[0], image.shape[1]))
            # Postprocessing
            image = (mask[..., None] * image + (1 - mask[..., None]) *
                     background)
            image = (image * 255).astype(np.uint8)
            # Display the final image
            cv2.imshow('RealSense', image)
            k = cv2.waitKey(1)

            if k % 256 == 27:
                print("Escape hit, closing...")
                break
    finally:
        # Stop streaming
        pipeline.stop()
