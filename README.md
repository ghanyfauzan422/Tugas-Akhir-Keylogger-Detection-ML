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

Edit `app.py` or set environment variables to customize:

**Environment Variables:**
- `SECRET_KEY`: Secret key for Flask sessions (required for production)
- `FLASK_DEBUG`: Set to 'true' to enable debug mode (default: 'false')
- `FLASK_HOST`: Host to bind to (default: '127.0.0.1')
- `FLASK_PORT`: Port to bind to (default: '5000')

**Application Settings:**
- `UPLOAD_FOLDER`: Directory where uploaded files are stored
- `MAX_CONTENT_LENGTH`: Maximum allowed file size
- `ALLOWED_EXTENSIONS`: Allowed file extensions

**Example for development:**
```bash
export FLASK_DEBUG=true
export FLASK_HOST=0.0.0.0
export FLASK_PORT=5000
export SECRET_KEY=your-secret-key-here
python app.py
```

### Security Considerations

⚠️ **Important Security Notes:**
1. **Executable Files**: This application accepts executable files (exe, dll) for malware analysis
   - Ensure the uploads directory has NO execute permissions
   - Never execute uploaded files directly on the server
   - Analyze files in a sandboxed/isolated environment only
   
2. **Production Deployment**:
   - Always set a strong `SECRET_KEY` environment variable
   - Run with `FLASK_DEBUG=false` in production
   - Use a production WSGI server (gunicorn, uWSGI) instead of Flask development server
   - Consider adding antivirus scanning integration
   
3. **File Storage**:
   - Files are saved with timestamps and UUIDs to prevent overwrites
   - Regular cleanup of old files is recommended
   - Monitor disk space usage 
