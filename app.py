# from flask import Flask, render_template, request, redirect, url_for, flash
# from werkzeug.utils import secure_filename
# import os

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'
# app.config['UPLOAD_FOLDER'] = 'static/uploads'
# app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# # Check if file type is allowed
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# @app.route('/')
# def index():
#     # List images in the upload folder
#     images = os.listdir(app.config['UPLOAD_FOLDER'])
#     return render_template('index.html', images=images)

# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             flash('No file part', 'danger')
#             return redirect(request.url)

#         file = request.files['file']
#         if file.filename == '':
#             flash('No selected file', 'danger')
#             return redirect(request.url)

#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             flash('File uploaded successfully!', 'success')
#             return redirect(url_for('index'))
    
#     return render_template('upload.html')

# if __name__ == '__main__':
#     os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
#     app.run(debug=True)




from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route for sign-in
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Replace this with real authentication
        if username == 'admin' and password == 'password':
            return redirect('/')
        else:
            flash('Invalid credentials, try again.')
    return render_template('signin.html')

# Route for gallery
@app.route('/')
def gallery():
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', images=images)

# Route for uploading images
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            flash('Image uploaded successfully!')
            return redirect('/')
    return render_template('upload.html')

# Route for deleting images
@app.route('/delete/<filename>', methods=['POST'])
def delete(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        flash('Image deleted successfully!')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
