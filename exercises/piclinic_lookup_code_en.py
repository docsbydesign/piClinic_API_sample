# coding=utf-8
#
#	script to look up an ICD-10 code and return its description in English
#
#		Command line format:
#	        piclinic_lookup_code_en.py
#
#
import sys
import requests


#
#   declare API variables
#
piclinic_host = 'https://dev.piclinic.org'
piclinic_session = piclinic_host + '/api/session.php'
piclinic_icd = piclinic_host + '/api/icd.php'


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
    #   data to pass to session
    #
    new_session_data = {
        'username': username,
        'password': password
    }
    try:
        #
        #   POST to session to create a new piClinic session
        #
        session = requests.post(piclinic_session, data=new_session_data)
        # if the request returned data, it should be a JSON string, so try to parse it
        if session.text:
            # parse the response into a DICT object
            session_data = session.json()
            # save the status information if it's present
            if session_data['status']['httpResponse']:
                post_status = session_data['status']['httpResponse']
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
        # 201 means a new session was opened. If it is anything but 201,
        #  no new session was created, so display a message.
        print("Sorry, I was unable to log in to the piClinic host.")
        print("Status : " + str(post_status))
        print("Reason: " + post_response)

    return session_token


def lookup_code(token, code, lang):
    # look up an ICD 10 code and print it's description in the specified language
    #
    code_data = []
    lookup_data = {}

    # create the token header for access to the API
    lookup_code_headers = {
        'X-piClinic-token': token
    }

    # create the data params for this query
    lookup_code_params = {
        'c': code,          # c is the code lookup query parameter
        'language': lang    # the language to return
    }

    try:
        lookup = requests.get(piclinic_icd, params=lookup_code_params, headers=lookup_code_headers)
        print("URL: " + lookup.url)
        # if the request returned data, it should be a JSON string, so try to parse it
        if lookup.text:
            # parse the response into a DICT object
            lookup_data = lookup.json()

    except Exception as e:
        # if an exception was raised, get the message
        print("Lookup error: " + str(e))

    if lookup_data:
        # a valid response was returned and parsed so take a look at what was returned

        # convert returned data to an array to simplify subsequent processing
        if lookup_data['count'] == 1:
            # add the data element to an array
            code_data.append(lookup_data['data'])
        else:
            # just copy the returned array
            code_data = lookup_data['data']

    if code_data:
        for elem in code_data:
            print(elem['icd10code'] + " (" + elem['language'] + "): " + elem['shortDescription'])

    else:
        print("Sorry, " + code + " was not found in the piClinic.")

    return


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
        # call the DELETE action with the token header to close the session
        session = requests.delete(piclinic_session, headers=close_session_header)
        if session.text:
            # if the request returned data, it should be a JSON string, so try to parse it
            session_data = session.json()
            if session_data['status']['httpResponse'] :
                delete_status = session_data['status']['httpResponse']
                delete_response = session_data['status']['httpReason']

    except Exception as e:
        delete_status = 500
        delete_status = str(e)

    if delete_status != 200:
        # 200 = success, so anything else is an error so show a message.
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
    #       normally do this outside of an experimental context
    session_token = open_session('twilio', 'Twilio!')
    if session_token:
        print("Token returned: " + session_token)
    else:
        print("Session not opened.")
        return

    # lookup the ICD code "R51" in English and print it's description
    lookup_code(session_token, 'R51', 'en')

    if session_token:
        print("Closing piClinic session.")
        close_session(session_token)

    return

if __name__ == '__main__':
    main(sys.argv)