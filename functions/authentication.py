

FIREBASE_API_KEY = "YOUR_API_KEY"
FIREBASE_AUTH_URL = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key="

def sign_in(email, password):
    try:
        response = requests.post(FIREBASE_AUTH_URL, json={
            "email": email,
            "password": password,
            "returnSecureToken": True
        })

        response_data = response.json()
        if 'idToken' in response_data:
            id_token = response_data['idToken']
            print("ID Token:", id_token)
            return id_token
        else:
            print("Error signing in:", response_data)
            return None

    except Exception as e:
        print("Exception during sign-in:", e)
        return None


