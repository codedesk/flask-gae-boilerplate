Python Flask BoilerPlate for Google App Engine
==============================================

Boilerplate project template for running a Flask-based application on
Google App Engine (Python)


About Flask
-----------
[Flask][flask] is a BSD-licensed microframework for Python based on
[Werkzeug][wz], [Jinja2][jinja2] and good intentions.

See <http://flask.pocoo.org> for more info.

## Run Locally
1. Install the [App Engine Python SDK](https://developers.google.com/appengine/downloads).
See the README file for directions. You'll need python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html) installed too.

2. Clone this repo with

   ```
   git clone https://github.com/codedesk/flask-gae-boilerplate.git
   ```
3. Install dependencies in the project's lib directory.
   Note: App Engine can only import libraries from inside your project directory.

   ```
   cd flask-gae-boilerplate
   cd src
   mkdir lib
   pip install -r requirements.txt -t src/lib
   ```
4. Add the secret keys for CSRF protection by running the `generate_keys.py`
   script at `src/application/generate_keys.py`, which will generate the
   secret keys module at src/application/secret_keys.py

5. Run this project locally from the command line:

   ```
   dev_appserver.py src/
   ```

Visit the application [http://localhost:8080](http://localhost:8080)

See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver)
for options when running dev_appserver.

### Feedback
Star this repo if you found it useful. Use the github issue tracker to give
feedback on this repo.

## Author
Vasanth Saminathan
