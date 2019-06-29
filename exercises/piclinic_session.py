# coding=utf-8
#
#	script to open and close a piclinic session
#
#		Command line format:
#	        piclinic_session.py
#
#
import sys
import requests


#
#   declare variables to access the piClinic API
#
piclinic_host = 'https://dev.piclinic.org'
piclinic_session_url = piclinic_host + '/api/session.php'


def open_session (username, password):
    #
    #    open a piClinic session
    #       success: return a session token
    #       error: return NONE and display an error message to the console
    #
    session_token = None
    post_status = None
    post_response = "Unable to create a new session."
    #
    #   credential data to pass to session resource
    #
    new_session_data = {
        'username': username,
        'password': password
    }
    try:
        #
        #   POST to session to create a new piClinic session
        #
        session = requests.post(piclinic_session_url, data=new_session_data)
        # if the request returned data, it should be a JSON string, so try to parse it
        if session.text:
            # parse the response into a DICT object
            session_data = session.json()
            # save the status information if it's present
            if session_data['status']['httpResponse']:
                post_status = session_data['status']['httpResponse']
                # if there's an httpResponse, there's also an httpReason
                post_response = session_data['status']['httpReason']

    except Exception as e:
        # if an exception was raised, get the message
        post_status = 500
        post_response = str(e)

    if post_status == 201:
        # 201 means a new session was created so get the token
        if session_data['count'] == 1:
            # count should always be 1 in this context
            # however, if count is ever greater than 1, an array is returned
            # which requires different syntax
            session_token = session_data['data']['token']
        # else return None, because something strange happened

    else:
        # if the status is anything but 201,
        #  no new session was created, so display a message.
        print("Sorry, I was unable to log in to the piClinic host.")
        print("Status: " + str(post_status))
        print("Reason: " + post_response)

    return session_token


def close_session(token):
    #
    #   Close the piclinic session referenced by token
    #
    #       NOTE that the DELETE action requires only the token header
    #
    close_session_header = {
        'X-piClinic-token': token
    }

    try:
        session = requests.delete(piclinic_session_url, headers=close_session_header)
        if session.text:
            # if the request returned data, it should be a JSON string, so try to parse it
            session_data = session.json()
            if session_data['status']['httpResponse'] :
                delete_status = session_data['status']['httpResponse']
                # if there's an httpResponse, there's also an httpReason
                delete_response = session_data['status']['httpReason']

    except Exception as e:
        delete_status = 500
        delete_status = str(e)

    if delete_status != 200:
        # 200 = success, for anything else, show the reason.
        #  However, in most cases, either way the session is closed.
        #  either by this call or a previous one.
        #
        print("An error occurred closing the session.")
        print("Status : " + str(delete_status))
        print("Reason: " + delete_response)

    return # nothing


def main(argv):
    #    open a piClinic session using hard-coded credentials
    #       NOTE: this is for demonstration only! You would not
    #       normally include credentials in a program outside of
    #       an experimental context.

    #  open a new session and get the token
    session_token = open_session('twilio', 'Twilio!')
    if session_token:
        print("Token returned: " + session_token)
    else:
        print("Session not opened.")
        return

    # that's all there is to do in this example so close the session and leave.
    print("Closing piClinic session.")
    close_session(session_token)

    return

if __name__ == '__main__':
    main(sys.argv)
