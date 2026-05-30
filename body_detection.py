import streamlit as st
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

import cv2
import numpy as np
from PIL import Image


st.title("Full Body Landmark Detector")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])


def draw_landmarks(image, detection_result):
    annotated_image = image.copy()

    # MediaPipe body landmark connections
    POSE_CONNECTIONS = [
        (0, 1), (1, 2), (2, 3), (3, 7),
        (0, 4), (4, 5), (5, 6), (6, 8),
        (9, 10),
        (11, 12),
        (11, 13), (13, 15),
        (12, 14), (14, 16),
        (11, 23), (12, 24),
        (23, 24),
        (23, 25), (25, 27),
        (24, 26), (26, 28),
        (27, 29), (29, 31),
        (28, 30), (30, 32),
        (27, 31), (28, 32)
    ]

    height, width, _ = annotated_image.shape

    for pose_landmarks in detection_result.pose_landmarks:
        points = []

        for landmark in pose_landmarks:
            x = int(landmark.x * width)
            y = int(landmark.y * height)
            points.append((x, y))

            cv2.circle(annotated_image, (x, y), 5, (0, 255, 0), -1)

        for start, end in POSE_CONNECTIONS:
            if start < len(points) and end < len(points):
                cv2.line(
                    annotated_image,
                    points[start],
                    points[end],
                    (255, 0, 0),
                    2
                )

    return annotated_image


if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    base_options = python.BaseOptions(
        model_asset_path="pose_landmarker_heavy.task"
    )

    options = vision.PoseLandmarkerOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.IMAGE,
        num_poses=3,
        min_pose_detection_confidence=0.5,
        min_pose_presence_confidence=0.5,
        min_tracking_confidence=0.5
    )

    detector = vision.PoseLandmarker.create_from_options(options)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=image_np
    )

    detection_result = detector.detect(mp_image)

    if detection_result.pose_landmarks:
        annotated_image = draw_landmarks(image_np, detection_result)

        st.image(
            annotated_image,
            caption="Detected Full Body Landmarks",
            use_container_width=True
        )

        st.success("Body landmarks detected!")

        st.write("Number of poses detected:", len(detection_result.pose_landmarks))

        for i, pose in enumerate(detection_result.pose_landmarks):
            st.write(f"Pose {i + 1}: {len(pose)} landmarks")
    else:
        st.image(image_np, caption="Original Image", use_container_width=True)
        st.warning("No full body pose detected.")