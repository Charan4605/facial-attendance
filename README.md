Facial Recognition Attendance System
A facial recognition-based attendance system that automatically marks attendance from group photos. This system uses face detection models to recognize students and mark their attendance in a Google Sheet.

Features
Detects multiple faces in a group photo.

Marks attendance automatically in Google Sheets.

Uses Google Vision API for image processing.

Easy to set up and integrate.

Installation
Prerequisites
Before you begin, ensure you have the following installed:

Python 3.6+ (You can download it from here)

pip (Python package installer) (Usually comes with Python)

Steps
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Charan4605/facial-attendance.git
cd facial-attendance
Install the required dependencies: Create a virtual environment (optional but recommended):

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows
Then, install the necessary Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
The requirements.txt file will list the dependencies (e.g., opencv-python, google-cloud-vision, etc.).

Usage
Prepare your student images: Ensure each student has a high-quality image for training. Save them in a folder named student_images.

Train the model: Use the provided Python script to train the model on the dataset. Run the following command:

bash
Copy
Edit
python train_model.py
Upload the class images: Faculty will upload class photos (group photos) to a specified Google Drive folder.

Attendance Marking: The system will process the uploaded images, detect faces, and mark attendance. The attendance will be logged automatically in a Google Sheet.

Check Attendance: View the attendance log in the linked Google Sheet.

Contributing
If you'd like to contribute to this project, feel free to fork the repo, make changes, and create a pull request.

License
This project is open-source and available under the MIT License.
