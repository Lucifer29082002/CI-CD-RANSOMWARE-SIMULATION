from flask import Flask, render_template, request, jsonify
import os
from cryptography.fernet import Fernet
import base64
import time

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = './static/uploads'
KEY_FILE = './static/key/ransom.key'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(os.path.dirname(KEY_FILE), exist_ok=True)

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    if os.path.exists(KEY_FILE):
        return open(KEY_FILE, 'rb').read()
    return generate_key()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)
    return encrypted_data

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)
        return decrypted_data
    except Exception as e:
        print(f"Error decrypting: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    # Save the file
    filename = file.filename
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)
    
    # Save original content for display
    with open(file_path, 'rb') as f:
        original_content = f.read()
        if isinstance(original_content, bytes):
            try:
                original_content = original_content.decode('utf-8')
            except UnicodeDecodeError:
                original_content = base64.b64encode(original_content).decode('utf-8')
    
    return jsonify({
        'status': 'success',
        'filename': filename,
        'content': original_content,
        'path': file_path
    })

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    file_path = data.get('file_path')
    
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'})
    
    key = load_key()
    
    # Simulate ransomware operation with a delay for demonstration
    time.sleep(1)
    
    try:
        encrypted_data = encrypt_file(file_path, key)
        encrypted_preview = base64.b64encode(encrypted_data).decode('utf-8')
        return jsonify({
            'status': 'success',
            'encrypted': True,
            'content': encrypted_preview,
            'key': key.decode('utf-8')
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    file_path = data.get('file_path')
    
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'})
    
    key = load_key()
    
    # Simulate ransomware operation with a delay for demonstration
    time.sleep(1)
    
    try:
        decrypted_data = decrypt_file(file_path, key)
        if decrypted_data:
            try:
                decrypted_content = decrypted_data.decode('utf-8')
            except UnicodeDecodeError:
                decrypted_content = base64.b64encode(decrypted_data).decode('utf-8')
            
            return jsonify({
                'status': 'success',
                'decrypted': True,
                'content': decrypted_content
            })
        else:
            return jsonify({'error': 'Failed to decrypt'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)