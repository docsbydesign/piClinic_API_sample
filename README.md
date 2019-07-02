# piClinic_API_sample
This repo contains code examples that demonstrate the ICD-10 code lookup feature of the piClinic API.

There are two examples that demonstrate the piClinic API:
* Making piClinic API calls from [Postman](https://www.getpostman.com/)
* Making piClinic API calls from within a Python application

If you're not familiar with the piClinic API, check out the [piClinic API documentation](https://piclinic.org/api).

After you review these examples and try them out, you will be familiar with the piClinic API and be able to access it from within your own Python programs.

# Making piClinic API calls from Postman

Postman is an API development environment that lets you call a REST API through an interactive console.

The [Postman_examples](https://github.com/docsbydesign/piClinic_API_sample/tree/master/Postman_examples) folder of this
repo contains a Postman collection of requests that demonstrate the
piClinic API calls that an application could use to access the piClinic API's _**icd**_ resource.

The requests in the collection do the following:
1. Open a session on the piClinic server and receive an access token.
1. Call a piClinic API in several different ways.
1. Close the session after access to the piClinic API is no longer needed.

## Using Postman

Running the examples in the Postman collection can give you a sense of interacting with the API,
which can help you when you use the API in a program.

The collection requires [Postman](https://www.getpostman.com/). If you're new to Postman,
review [Getting started with Postman](https://learning.getpostman.com/getting-started/) to learn more about it.

## Importing the Postman collection

A Postman collection is a set of API requests that can be made from within Postman.

To import the Postman collection, Open Postman and:
1. Click the **Import** button.
2. Select the **Import from link** option.
3. Enter this URL, and then click **Import**.
```
https://raw.githubusercontent.com/docsbydesign/piClinic_API_sample/master/Postman_examples/piClinicApiClass.postman_collection.json
```
4. Select the **Collections** tab to see the collection you just imported.

## Running the piClinic API requests in the collection

Open the `piClinicApiClass` collection in Postman to see these requests:
1. Open a piClinic session
2. Get a code description by ICD code lookup
3. Get a code description by ICD code lookup (en)
4. Get an ICD code by description search
5. Close the current piClinic session

### Adding your credentials

Access to the piClinic API is password protected, so you must first add your credentials to the sample.

**BE CAREFUL!** You do not want to save your credentials in a public folder or repo! (Don't ask me how I know this.)

1. Open the `Open a piClinic session` request, and then open the request's **Body** tab.
1. Edit the username and password values and replace:
  * `REPLACE WITH YOUR USERNAME` with the username you were provided.
  * `REPLACE WITH YOUR PASSWORD` with the password you were provided.
1. Click **Send**.
1. Review the response **Body** to see the data returned in the response. You should see a `data` object like the one in [the documentation](https://piclinic.org/api/#post-response-example) and a `status` object that indicates success.

### Exploring the examples

After you have provided your credentials and run the first request,
run the remaining samples in order. Each of the subsequent requests uses the access token
that the first request created and saved. You can see the token header in the request's **Headers** tab.

For each of the other requests in the collection:

1. Open the request and click **Send**.
2. Review the parameters and the response to get to know the API.

**Remember** that the piClinic API requires a valid session token to access
most of its resources so the `Open a piClinic session` request must be sent
 first to obtain a valid session token for the other requests.

# Making piClinic API calls from within a Python application

The [Python_examples](https://github.com/docsbydesign/piClinic_API_sample/tree/master/Python_examples) folder
contains these Python scripts to demonstrate how you can access the piClinic API from within an application.

Use your favorite Python development environment to review and run them in the following sequence.
If you don't have a favorite Python environment, you can always view them in a text editor and run them from a terminal or command window.

1. piclinic_session.py
1. piclinic_lookup_code.py
1. piclinic_lookup_code_en.py
1. piclinic_search_code_en.py

## Preparing Python

The code examples require Python 3.x and import the `requests` module.
If you don't have the `requests` module installed on your system, you can
install it by running the following command line on your Mac:

```
python3 -m pip install requests
```
or on your PC:
```
python -m pip install requests
```

### Downloading the code examples

You can download this repo to access the files directly from your system by clicking the `Clone or download` button above or executing
this `git` command from the folder under which you want to install the files.

```
git clone git://github.com/docsbydesign/piClinic_API_sample.git
```

## Running the Python examples

Each of the scripts requires the username and password you were provided.
In a terminal or command window, you enter them on the command line after the script name as:

```
<script_name.py> username password
```

For example, to run the `piclinic_lookup_code.py` script from the command line, you would enter the following command line, replacing `username` and `password` with the username and password you were provided.

```
piclinic_lookup_code.py username password
```

### piclinic_session.py

Opens and closes a piClinic session.

The methods in this script show how to access the **session** resource to
obtain an access token and close the session when finished. These methods
will be imported by the other scripts to perform those functions.

This script makes API calls like the `Open a piClinic session` and `Close the current piClinic session` requests in the Postman collection.

### piclinic_lookup_code.py

Opens a piClinic session to look up an ICD-10 code and then closes the session.

This script imports the session methods from `piclinic_session.py` and then
calls the _**icd**_ resource to look up an ICD-10 code and get its description.

This script makes an API call like the `Get a code description by ICD code lookup` request in the Postman collection.

Try changing the code value to look up the description of another ICD-10 codes.
For example, try looking up the description for ICD-10 code: `J00` or have it accept a code as another
command line parameter.

### piclinic_lookup_code_en.py

Opens a piClinic session to look up an ICD-10 code in English and then closes the session.

This script imports the session methods from `piclinic_session.py` and then
calls the _**icd**_ resource to look up an ICD-10 code and get its description in English.

This script makes an API call like the `Get a code description by ICD code lookup (en)` request in the Postman collection.

Try changing the code value to look up the description of another ICD-10 codes as you did in the previous example.

### piclinic_search_code_en.py

Opens a piClinic session to search for the ICD-10 codes that contain a specific text in English and then closes the session.

This script imports the session methods from `piclinic_session.py` and then
calls the _**icd**_ resource to search for the ICD-10 codes based on their description in English.

This script makes an API call like the `Get an ICD code by description search` request in the Postman collection.

Try changing the search text to look up some other ICD-10 codes.

# Where to next?

Now that you know how to access the piClinic API, you can access its features from your application to help make it easier
for your customers correctly code their medical diagnoses.
