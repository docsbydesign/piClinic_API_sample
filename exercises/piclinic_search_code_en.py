# coding=utf-8
#
#	script to look up an ICD-10 code and return its description in English
#
#		Command line format:
#	        piclinic_search_code_en.py
#
#
import sys
import requests
import piclinic_session


#
#   declare API variables
#
piclinic_host = 'https://dev.piclinic.org'
piclinic_session_url = piclinic_host + '/api/session.php'
piclinic_icd_url = piclinic_host + '/api/icd.php'


def search_code(token, text, lang):
    # look up an ICD 10 code by it's description and print the matching codes in the specified language
    #
    code_data = []
    search_data = {}

    # create the token header for access to the API
    search_code_headers = {
        'X-piClinic-token': token
    }

    # create the data params for this query
    search_code_params = {
        'q': text,          # q is the code search query parameter
        'language': lang    # the language to return
    }

    try:
        search = requests.get(piclinic_icd_url, params=search_code_params, headers=search_code_headers)
        print("URL: " + search.url)
        # if the request returned data, it should be a JSON string, so try to parse it
        if search.text:
            # parse the response into a DICT object
            search_data = search.json()

    except Exception as e:
        # if an exception was raised, get the message
        print("Search error: " + str(e))

    if search_data:
        # a valid response was returned and parsed so take a look at what was returned

        # convert returned data to an array to simplify subsequent processing
        if search_data['count'] == 1:
            # add the data element to an array
            code_data.append(search_data['data'])
        else:
            # just copy the returned array
            code_data = search_data['data']

    if code_data:
        for elem in code_data:
            print(elem['icd10code'] + " (" + elem['language'] + "): " + elem['shortDescription'])

    else:
        print("Sorry, No codes containing '" + text + "' were found in the piClinic.")

    return


def main(argv):
    #    open a piClinic session using hard-coded credentials
    #       NOTE: this is for demonstration only! You would not
    #       normally do this outside of an experimental context
    session_token = piclinic_session.open_session('twilio', 'Twilio!')
    if session_token:
        print("Token returned: " + session_token)
    else:
        print("Session not opened.")
        return

    # search the ICD descriptions for "headache" in English and print those that match
    search_code(session_token, 'headache', 'en')

    if session_token:
        print("Closing piClinic session.")
        piclinic_session.close_session(session_token)

    return

if __name__ == '__main__':
    main(sys.argv)