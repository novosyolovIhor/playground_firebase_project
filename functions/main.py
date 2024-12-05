
from firebase_functions import firestore_fn, https_fn
from firebase_admin import initialize_app, firestore
import google.cloud.firestore
import authentication

app = initialize_app()

@https_fn.on_request()
def add_message_to_database(req: https_fn.Request) -> https_fn.Response:
    message = req.args.get("text")
    if message is None:
        return https_fn.Response("No text was provided",status=400)
    firestore_client: google.cloud.firestore.Client = firestore.client()
    _, document_reference = firestore_client.collection("messages").add({"message": message})
    return https_fn.Response(f"Message with ID{document_reference.id} added")

@https_fn.on_request()
def count_the_number_of_letters(req: https_fn.Request) -> https_fn.Response:
    message = req.args.get("text")
    if message is None:
        return https_fn.Response("There was no text provided", status = 400)
    num = 0
    for n in message:
        if n >= 'a' and n <= 'z':
            num+=1
    return https_fn.Response(f"{num}")
#make push doc function

@firestore_fn.on_document_created(document="messages/{pushId}")
def make_upper_case_and_add_yoloo(event: firestore_fn.Event[firestore_fn.DocumentSnapshot | None]) -> None:
    # Get the value of "original" if it exists.
    if event.data is None:
        return
    try:
        original = event.data.get("message")
    except KeyError:
        print("There is no such document", status = 400)
        return

    # Set the "uppercase" field.
    print(f"Uppercasing {event.params['pushId']}: {original}")
    upper_w_y = original.upper() + " Yoloooo!!!!"
    event.data.reference.update({"uppercase_with_yoloo": upper_w_y})

@firestore_fn.on_document_created(document="messages/{pushId}")
def make_some_big(event: firestore_fn.Event[firestore_fn.DocumentSnapshot | None]) -> None:
    if event.data is None:
        return
    try:
        orig = event.data.get("message")
    except KeyError:
        print("There is no message there", status = 400)
        return
    print(f"document with text {orig.upper()} was added + it is big now")
