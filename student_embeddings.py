import cv2
import os
import re  # For regular expressions
import csv
from datetime import datetime

# Path to the folder where student images are stored
student_images_folder = "/Users/charandusary/Desktop/Training_set"

# Path to the CSV file to track attendance
csv_file_path = '/Users/charandusary/Desktop/albums_data.csv'

# Load OpenCV's Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces in an image
def detect_faces(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image: {image_path}")
        return []
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

# Function to normalize the student ID from the image name
def normalize_student_id(image_name):
    match = re.match(r'(\d{2}bcs\d{3})', image_name.lower())
    if match:
        return match.group(1)
    else:
        print(f"Could not normalize Student ID for image: {image_name}")
        return None

# Function to update the CSV file with attendance data
def update_attendance_csv(student_id, present, current_date):
    file_exists = os.path.exists(csv_file_path)
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            header = ['Student_ID', current_date]
            writer.writerow(header)
        attendance_status = 'Present' if present else 'Absent'
        writer.writerow([student_id, attendance_status])

# Function to process group photos and mark attendance
def process_group_photos():
    detected_students = set()  # To track detected students
    all_students = {f"23bcs{str(i).zfill(3)}" for i in range(1, 71)}  # All student IDs from 23bcs001 to 23bcs070
    current_date = datetime.today().strftime('%Y-%m-%d')

    # Iterate through each image in the folder
    for image_name in sorted(os.listdir(student_images_folder)):
        image_path = os.path.join(student_images_folder, image_name)
        if not image_name.lower().endswith(('png', 'jpg', 'jpeg')):
            continue  # Skip non-image files
        
        print(f"Processing image: {image_name}")
        
        # Normalize the student ID
        student_id = normalize_student_id(image_name)
        
        if student_id and student_id not in detected_students:
            # Detect faces in the image
            faces = detect_faces(image_path)

            if len(faces) > 0:
                print(f"Detected {len(faces)} faces in {image_name}")
                student_present = True  # If faces are detected, mark the student as present
            else:
                print(f"No faces detected in {image_name}")
                student_present = False  # If no faces are detected, mark the student as absent
            
            # Add detected student ID to the set
            detected_students.add(student_id)

            # Update attendance in the CSV file for each detected student
            update_attendance_csv(student_id, student_present, current_date)

    # Ensure all students are marked as present or absent, and in order
    for student_id in sorted(all_students):
        if student_id not in detected_students:
            # If a student was not detected, mark them as absent
            update_attendance_csv(student_id, False, current_date)

    # Returning a success message
    return f"Processing complete. Detected students: {', '.join(sorted(detected_students))}", 200

if __name__ == "__main__":
    message, status_code = process_group_photos()
    print(message)
 
