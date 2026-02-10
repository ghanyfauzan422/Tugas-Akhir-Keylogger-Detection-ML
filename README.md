# Tugas-Akhir-Keylogger-Detection-ML
ML Keylogger Detection

## File Upload Feature

This application provides a web interface for uploading files to be analyzed for keylogger detection.

### Features
- Web-based file upload interface
- Support for multiple file formats (TXT, LOG, CSV, JSON, EXE, DLL)
- File size validation (max 16MB)
- Secure file handling with filename sanitization
- Drag and drop support
- Flash messages for user feedback

### Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. Run the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Upload files using the web interface:
   - Click the upload area or drag and drop a file
   - Supported formats: TXT, LOG, CSV, JSON, EXE, DLL
   - Maximum file size: 16MB
   - Click "Upload File for Analysis" to submit

4. Uploaded files are stored in the `uploads/` directory

### Configuration

Edit `app.py` to customize:
- `SECRET_KEY`: Change the secret key for production use
- `UPLOAD_FOLDER`: Directory where uploaded files are stored
- `MAX_CONTENT_LENGTH`: Maximum allowed file size
- `ALLOWED_EXTENSIONS`: Allowed file extensions 
