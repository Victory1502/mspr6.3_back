from routes import *


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5001, host="0.0.0.0")