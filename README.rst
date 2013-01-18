pyWHMCS
==========================

Matt, WHMCS Founder/Lead Developer describes their product:
  WHMCS is an all-in-one client management, billing & support solution for online businesses. Handling everything from signup to termination, WHMCS is a powerful business automation tool that puts you firmly in control

This projects aims to provide an easy to use, consistent and simple client library and CLI program to interact with HTTP API of WHMCS software.

For now only interface is via command line.

Installation
---------------------------
Very simple process::

  $ git clone git://github.com/zekzekus/pywhmcs.git
  $ cd pywhmcs
  $ python setup.py install

And it is ready to use as a CLI script called **pywhmcs**!

Usage
---------------------------
CLI program includes usage information. The standart help output is::

    $ pywhmcs --help
    usage: pywhmcs [-h] [--verbose] --url URL --username USERNAME --password PASSWORD --action ACTION [--params ...]

    pyWHMCS Client Comman Line Interface

    optional arguments:
    -h, --help            show this help message and exit
    --verbose             Activate verbose output
    --url URL             WHMCS API endpoint URL
    --username USERNAME   Username with API permission
    --password PASSWORD   API user password
    --action ACTION       Action name to invoke
    --params ...          Parameters passed with action. (--params param1=value1 param2=value2 etc.)

If you want to take the list of clients you have to make a POST request to the WHMCS API endpoint with POST body includes action="getclients" and necessary credidentials. For example::

  $ pywhmcs --url http://yourdomain.com/includes/api.php --username apiuser --password pass --action getclients

The output will be like::

  {
      "startnumber": 0,
      "clients": {
          "client": [
              {
                  "status": "Active",
                  "firstname": "John",
                  "companyname": "Does Company",
                  "lastname": "Doe",
                  "datecreated": "2012-11-22",
                  "groupid": "0",
                  "id": "1",
                  "email": "john@doe.com"
              }
          ]
      },
      "totalresults": "1",
      "result": "success",
      "numreturned": 1
  }

For actions that requires extra arguments like clientid, userid etc. you must use optional --params parameter. After --params you must give your params in a format of paramN=valueN. These parameters and values will be appended to the POST body as key value pairs and send with the request. For example::

  $ pywhmcs --url http://yourdomain.com/includes/api.php --username apiuser --password pass --action addclientnote --params userid=1 notes="this is a note"
  {
    "result": "success",
    "noteid": 4
  }

With this approach you can call ALL of the acitons that provided by WHMCS system. You can find the developer API documentation here_.

.. _here: http://docs.whmcs.com/API

Also you can install this library on python path and import the invoke function from whmcs module. It can be used for internal interaction to WHMCS system. Actually i am planning to build a nice client on top of it and than implement a reusable django application for easy communication between any django app and WHMCS system.

TODO
---------------------------
- For now just JSON response type implemented. WHMCS API supports XML format and a simple key value format. These formats will be supported via parameters. (will be released with v0.0.3)
- Create action classes to manage API interface completely. Classes may now about action parameters, required data etc.
- Implement file upload infrastructure for actions may need uploading files.
-

Development
---------------------------
For now library needs only one external dependency: `requests HTTP client library`_. If you want to contribute you may follow these steps::

  $ git clone git://github.com/zekzekus/pywhmcs.git
  $ cd pywhmcs
  $ python setup.py develop

These commands will clone the repository and fetch all dependencies and install to your system.

.. _`requests HTTP client library`: http://docs.python-requests.org/en/latest/

Troubleshoot
---------------------------
- The user you give as --username parameter must have "API Permission". You or the administrator of the WHMCS system must grant this permission to your user.
- WHMCS system allows only specified set of IP addresses to make API requests for security reasons. So, your IP address must be added to permitted IP addresses list in WHMCS system.
- --params parameter must be the last parameter specified. Because it is a "rest of" type argument.

