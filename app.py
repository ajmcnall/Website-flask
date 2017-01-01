from flask import Flask
import controllers
import config

app = Flask(__name__, template_folder='templates')


# Register the controllers
app.register_blueprint(controllers.main)

app.secret_key = config.env['secret_key']

# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the
# server
if __name__ == '__main__':
    # listen on external IPs
    app.run(host=config.env['host'], port=config.env['port'], debug=True)
