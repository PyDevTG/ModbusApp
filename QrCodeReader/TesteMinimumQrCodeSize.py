import cv2
image = cv2.imread('QrcodeImage.png')

qrCodeDetector = cv2.QRCodeDetector()
decodedText, points, _ = qrCodeDetector.detectAndDecode(image)


if points is not None:
    points = points[0]
    
    
    for i in range(len(points)):
        pt1 = [int(val) for val in points[i]]
        pt2 = [int(val) for val in points[(i + 1) % 4]]
        cv2.line(image, pt1, pt2, color=(255, 0, 0), thickness=3)

    print(decodedText)    
 
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
     
 
else:
    print("QR code not detected")