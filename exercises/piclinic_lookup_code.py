# coding=utf-8
#
#	script to look up an ICD-10 code and return its description(s)
#
#		Command line format:
#	        piclinic_lookup_code.py
#
#
import sys
import requests
import piclinic_session


#
#   declare variables to access the piClinic API
#
piclinic_host = 'https://dev.piclinic.org'
piclinic_session_url = piclinic_host + '/api/session.php'
piclinic_icd_url = piclinic_host + '/api/icd.php'


def lookup_code(token, code):
    # look up an ICD 10 code and print it's description(s)
    #
    code_data = []
    lookup_data = {}

    # create the token header for access to the API
    lookup_code_headers = {
        'X-piClinic-token': token
    }

    # create the token header to access the API
    lookup_code_params = {
        'c': code           # c is the code lookup query parameter
    }

    try:
        lookup = requests.get(piclinic_icd_url, params=lookup_code_params, headers=lookup_code_headers)
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
        print(str(lookup_data['count']) + " ICD-10 code object(s) returned.")
        for elem in code_data:
            print(elem['icd10code'] + " (" + elem['language'] + "): " + elem['shortDescription'])

    else:
        print("Sorry, " + code + " was not found in the piClinic.")

    return


def main(argv):
    #    open a piClinic session using hard-coded credentials
    #       NOTE: this is for demonstration only! You would not
    #       normally include credentials in a program outside of
    #       an experimental context.

    #  open a new session and get the token
    session_token = piclinic_session.open_session('twilio', 'Twilio!')
    if session_token:
        print("Token returned: " + session_token)
    else:
        print("Session not opened.")
        return

    # lookup the ICD code "R51" and print it's description(s)
    lookup_code(session_token, 'R51')

    if session_token:
        print("Closing piClinic session.")
        piclinic_session.close_session(session_token)

    return

if __name__ == '__main__':
    main(sys.argv)
