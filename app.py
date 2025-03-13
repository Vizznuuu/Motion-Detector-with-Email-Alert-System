import cv2
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
import time

# Email configuration
sender_email = 'vishnuprasad280204@gmail.com'
receiver_email = 'vishnuprasad280204@gmail.com'
password = 'mjtt eiyi ymyz iqgd'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Initialize the camera
cap = cv2.VideoCapture(0)

# Function to send email with the captured image
def send_email(image_path):
    try:
        print("Preparing to send email...")
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = 'Motion Detected!'
        
        # Read the image and attach to email
        with open(image_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(image_path)}')
            msg.attach(part)

        # Sending email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            print("Email sent successfully!")
    
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main loop
print("Starting the smart security camera...")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    # Process the frame here for motion detection
    # For example: check for motion...

    # Simulating motion detection for testing
    motion_detected = True  # Change this condition based on actual detection logic
    if motion_detected:
        image_path = 'captured_image.jpg'
        cv2.imwrite(image_path, frame)  # Save the captured image
        print("Motion detected! Capturing image...")
        
        # Send the email with the captured image
        send_email(image_path)

    # Display the frame (optional)
    cv2.imshow('Smart Security Camera', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()