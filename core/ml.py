import os
import cv2
import easyocr


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
import django
django.setup()

from adminpanel.models import TruckJourney, JourneyCheckpoint, Checkpoint


harcascade = "H:\\cl2\\core\\adminpanel\\model\\haarcascade_russian_plate_number.xml"
cap = cv2.VideoCapture(0)
cap.set(3, 640) 
cap.set(4, 480)  
min_area = 500
count = 0
reader = easyocr.Reader(['en'])

target_plates = set(TruckJourney.objects.values_list('driver__truck_no', flat=True))

target_plate_detected = False

img_roi = None  

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y:y + h, x:x + w]
            cv2.imshow("ROI", img_roi)

            results = reader.readtext(img_roi)

            for (bbox, text, prob) in results:
                text = ''.join(text.split())
                print(f"License Plate Number: {text}")

                if text in target_plates:
                    print(f"Target License Plate Number Detected: {text}")
                    target_plate_detected = True
                    break

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        if img_roi is not None:
            cv2.imwrite(f"plates/scaned_img_{count}.jpg", img_roi)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
            cv2.imshow("Results", img)
            cv2.waitKey(500)
            count += 1

    if target_plate_detected:
        break

cap.release()
cv2.destroyAllWindows()

if target_plate_detected:
    mumbai_location = Checkpoint.objects.get(location__name='Pune')
    journey_checkpoints = JourneyCheckpoint.objects.filter(checkpoint=mumbai_location)

    for journey_checkpoint in journey_checkpoints:
        journey_checkpoint.checkpoint_reached = True
        journey_checkpoint.save()
        print("Updated JourneyCheckpoint for Pune location.")
