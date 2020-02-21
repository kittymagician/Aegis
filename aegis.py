import os
import yara
from app import app
from flask import Flask, request, redirect, render_template, url_for
from werkzeug import secure_filename

'''
concat rules into a single yara super file
'''


def yarcat():
    if os.path.exists("./rules/output.yara") == True:
        os.remove("./rules/output.yara")
    with open("./rules/output.yara", "wb") as outfile:
        for root, dirs, files in os.walk("./rules", topdown=False):
            for name in files:
                fname = str(os.path.join(root, name))
                with open(fname, "rb") as infile:
                    if fname != './rules/output.txt':
                        outfile.write(infile.read())


'''
Match rules and show hits
'''


def compileandscan(filematch):
    yarcat()
    print(filematch)
    rules = yara.compile('./rules/output.yara')
    matches = rules.match(filematch, timeout=60)
    ma = 0
    length = len(matches)
    if length > 0:
      c = matches
      dmatch = []
      for match in matches:
        dmatch.append(matches[ma].strings)
        ma = ma + 1
    else:
      matches = 'No YARA hits.'
      dmatch = None
    return [matches, dmatch]

'''
File Upload Page
'''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request)
        file = request.files['file']
        if file and file != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('scan', filename=filename))
        else:
          return 'file blank. Please specifiy file'
    return render_template('upload.html')

'''
About Page
'''

@app.route("/about")
def about():
  return render_template('about.html')

'''
Show results and delete file.
'''

@app.route("/scan/<filename>")
def scan(filename):
    a = compileandscan('./uploads/' + filename)
    remdir = './uploads/' + filename
    os.remove(remdir)
    ur = {'filename': filename, 'yararesults': a[0], 'yarastrings': a[1]}
    return render_template('results.html', ur=ur)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
