import firebase_admin
from firebase_admin import credentials, auth
from flask import Flask, request, jsonify

# Initialize the Firebase Admin SDK
cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)


@app.route('/add_message_to_database', methods=['POST'])
def add_message_to_database():
    # Get the ID token from the Authorization header
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return jsonify({'error': 'Unauthorized: No token provided'}), 403

    id_token = auth_header.split('Bearer ')[-1]

    try:
        # Verify the ID token
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        print(f"User ID: {uid}")

        # Process the request (add your message handling logic here)
        message = request.json.get('text')

        # For example, you can save the message to Firestore here

        # Respond back to the client
        return jsonify({'success': True, 'message': 'Message added successfully'})

    except Exception as e:
        print(f"Error verifying ID token: {e}")
        return jsonify({'error': 'Unauthorized: Invalid token'}), 403


# For deploying the function with Flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
