import pyrebase

config = {
    "apiKey": "AIzaSyD3jVlyCDREECKJ2sTU4h2Dq-C5vt2L6AE",
    "authDomain": "parcial-final-98288.firebaseapp.com",
    "databaseURL": "https://parcial-final-98288-default-rtdb.firebaseio.com/",
    "storageBucket": "parcial-final-98288.firebasestorage.app",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
