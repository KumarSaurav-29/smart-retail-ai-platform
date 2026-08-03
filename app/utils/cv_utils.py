import cv2


def read_image(image_path):
    """
    Read an image from disk.
    """
    return cv2.imread(image_path)


def resize_image(image, width=640, height=480):
    """
    Resize image.
    """
    return cv2.resize(image, (width, height))


def convert_to_grayscale(image):
    """
    Convert BGR image to grayscale.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_gaussian_blur(image, kernel_size=(5, 5)):
    """
    Apply Gaussian Blur.
    """
    return cv2.GaussianBlur(image, kernel_size, 0)


def detect_edges(image, threshold1=100, threshold2=200):
    """
    Detect edges using Canny.
    """
    return cv2.Canny(image, threshold1, threshold2)


def detect_faces(image):

    gray = convert_to_grayscale(image)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40)
    )

    return faces


def draw_face_boxes(image):

    faces = detect_faces(image)

    for (x, y, w, h) in faces:

        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    return image


def start_webcam():

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame = resize_image(frame)

        output = draw_face_boxes(frame)

        cv2.imshow("Smart Retail OpenCV Demo", output)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()