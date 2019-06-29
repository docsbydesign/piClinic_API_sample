# coding=utf-8
#
#	script to look up an ICD-10 code and return its description in English
#
#		Command line format:
#	        piclinic_lookup_code_en.py username password
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


def lookup_code(token, code, lang):
    # look up an ICD 10 code and print it's description in the specified language
    #
    code_data = []
    lookup_data = {}

    # create the token header to access the API
    lookup_code_headers = {
        'X-piClinic-token': token
    }

    # create the data params for this query
    lookup_code_params = {
        'c': code,          # c is the code lookup query parameter
        'language': lang    # the language to return
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
    #    open a piClinic session using the credentials passed in the command line

    username = None
    password = None

    # read the command line arguments
    if len(argv) > 2:
        # there are enough command line arguments to create the credentials
        username = argv[1]
        password = argv[2]
        # any others are ignored

    else:
        print("I couldn't open a session because you forgot to give me your username and password.")
        return

    #  open a new session and get the token
    print("Opening a piClinic API session for: " + username)
    session_token = piclinic_session.open_session(username, password)

    if session_token:
        print("Token returned: " + session_token)
    else:
        print("Session not opened.")
        return

    # lookup the ICD code "R51" in English and print it's description
    lookup_code(session_token, 'R51', 'en')

    if session_token:
        print("Closing piClinic session.")
        piclinic_session.close_session(session_token)

    return

if __name__ == '__main__':
    main(sys.argv)
