# code_lookup_sample
Sample code that demonstrates the ICD-10 code lookup feature of the piClinic API

This sample contains two examples of accessing the piClinic API:
* Making piClinic API calls using [Postman](https://www.getpostman.com/)
* Making piClinic API calls from within a Python application

See [piClinic API documentation](https://piclinic.org/api) for more information about the piClinic API.

# Making piClinic API calls using Postman

Postman is an API development environment that enables calling a REST API through an interactive console.

The [postman](https://github.com/docsbydesign/code_lookup_sample/tree/master/postman) folder of this
repo contains a Postman collection of requests that demonstrate the
sequence of piClinic API calls that access the _**icd**_ resource.

The Postman collection demonstrates a typical sequence of piClinic API calls that an application might use.
This sequence consists of:
1. Opening a session on the piClinic server and receiving an access token.
1. Calling a piClinic API. The collection contains several examples of piClinic API calls.
1. Closing the session when access to the piClinic API is no longer needed.

## Download the repo

Download this repo to your system by clicking the `Clone or download` button above or executing
this `git` command from the folder in which you want to install the files.

```
$ git clone git://github.com/docsbydesign/code_lookup_sample.git
```

## Making piClinic API calls using Postman

Opening the collection, requires [Postman](https://www.getpostman.com/) to be installed on your system.

Running the examples in the Postman collection can give you a sense of interacting with the API,
which can help you when you use the API in a program.

If you're not familiar with Postman, review the documentation at [Getting started with Postman](https://learning.getpostman.com/getting-started/).

### Importing the Postman collection

A Postman collection is a set of API requests that can be made from Postman. This collection
demonstrates the piClinic API.

Open Postman and follow these steps to import the Postman collection:
1. Click the **Import** button.
2. Select the **Import from link** option.
3. Enter this URL, and then click **Import**
```
https://raw.githubusercontent.com/docsbydesign/code_lookup_sample/master/postman/piClinicApiClass.postman_collection.json
```

### Running the piClinic API requests in the collection

Open the collection in Postman to see these requests:
1. Open a piClinic session
2. Get a code description by ICD code lookup
3. Get a code description by ICD code lookup (en)
4. Get an ICD code by description search
5. Close the current piClinic session

Start with the first request, open it, and click **Send**.

Review the response **Body** to see the response format.

Repeat these two steps for each request. See the request description for additional information about the request.
