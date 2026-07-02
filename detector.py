import cv2
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)

detector = htm.HandDetector()


def generate_frames():
    while True:
        success, frame = cap.read()

        if not success:
            break

        # Detect hands
        frame = detector.findHands(frame)

        # Get landmark positions
        lmList = detector.findPosition(frame)

        # Count fingers
        fingerCount = detector.fingersUp(lmList)

        # Display finger count
        cv2.putText(
            frame,
            f"Fingers: {fingerCount}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # Convert frame for Flask
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame +
            b'\r\n'
        )