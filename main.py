import cv2
import HandTrackingModule as htm

print("1. Program started")

cap = cv2.VideoCapture(0)

print("2. Camera object created")

if not cap.isOpened():
    print("3. Camera failed to open")
    exit()

print("3. Camera opened successfully")

detector = htm.HandDetector()

print("4. HandDetector created")

while True:
    print("Loop started")

    success, img = cap.read()
    print("cap.read() =", success)

    if not success:
        print("Failed to read frame")
        break

    print("Before findHands")

    img = detector.findHands(img)

    print("After findHands")

    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()