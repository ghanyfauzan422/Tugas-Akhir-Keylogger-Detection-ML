"""
Flask application for file upload in Keylogger Detection ML system.

SECURITY NOTE: This application accepts executable files (exe, dll) for malware analysis.
Ensure the following security measures are in place:
1. The uploads directory should have no execute permissions
2. Files should be analyzed in a sandboxed environment
3. Never execute uploaded files directly on the server
4. Consider integrating antivirus scanning before processing
5. Use environment-based configuration for production deployment
"""

import os
import uuid
import logging
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
# Note: The fallback generates a new key on each restart. For production, ALWAYS set SECRET_KEY env var.
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24).hex())
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'log', 'csv', 'json', 'exe', 'dll'}

# Create upload directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    """Check if the file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    """Render the main page with upload form"""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload"""
    # Check if file part exists in request
    if 'file' not in request.files:
        flash('No file part in the request', 'error')
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    # Check if user selected a file
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('index'))
    
    # Validate and save file
    if file and allowed_file(file.filename):
        original_filename = secure_filename(file.filename)
        # Add timestamp and UUID to prevent file overwrites
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_id = str(uuid.uuid4())[:8]
        name, ext = os.path.splitext(original_filename)
        filename = f"{name}_{timestamp}_{unique_id}{ext}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Log warning for executable files
        if ext.lower() in ['.exe', '.dll']:
            logger.warning(f"SECURITY: Executable file uploaded: {filename}. Ensure analysis is done in sandboxed environment.")
        
        file.save(filepath)
        logger.info(f"File uploaded successfully: {filename}")
        flash(f'File "{original_filename}" uploaded successfully as "{filename}"!', 'success')
        return redirect(url_for('index'))
    else:
        flash('Invalid file type. Allowed types: txt, log, csv, json, exe, dll', 'error')
        return redirect(url_for('index'))


if __name__ == '__main__':
    # Get configuration from environment variables
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = int(os.environ.get('FLASK_PORT', '5000'))
    app.run(debug=debug_mode, host=host, port=port)
