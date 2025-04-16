# Product parts testing reports

A report generator over the raw test results from CSV sources. It takes two files:

- Dataset: CSV formatted file with columns below
    - `SN` - The Part Serial number (Identifier)
    
    - `Run` time - test/measurement run time
    
    - `Site` - Not used
    
    - `Operation` - Not used
    
    - `Equipment` - Not used
    
    - `Status.1` - Overall the part measurement status: 
      - OK if all tests passed,
      - NOK any test failed
    
    - `Name` - test/measurement name
    
    - `Input` - input value for the test
    
    - `Output` - output value for the current measurement
    
    - `High_Limit` - Allowed highest value for the output
    
    - `Low_Limit` - Allowed lowest value for the output
    
    - `Status.2` - current test/measurement status

- Descriptive file for parts in CSV format with two columns:

  - `SN` - part serial number (unique)

  - `Part_Desc` - Human readable part description

After report is generated it sends the generated charts and tables to
the provided email addresses.

The project is developed on JupyterNotebook for learning purposes.

# Installation & Configurations

The project needs Python 3.11 to be installed. Use the command below to install required python packages for python:
```shell
  python -m pip install -r requirements.txt
```

Note! **it is required to have Jupyter Notebook installed on your computer to use the main processor**

If the requirements installation didn't install Jupyter Notebook follow the link for more information: https://jupyter.org/install

## Emailing

To be able to send out email reports the `.env` file filled with the variables below is required:
```dotenv
EMAIL_HOST=<SMTP_HOST>
EMAIL_PORT=<SMTP_SERVER_PORT>
EMAIL_HOST_USER=<SMTP_USER>
EMAIL_HOST_PASSWORD=<SMTP_PASSWORD>
```

The STMP authentication details can be generated using for example gmail account. 
For more information follow the link: https://support.google.com/a/answer/176600?hl=en

# Dummy data generation

It is possible to create dummy data using the python script `duplicator.py`. It is required
to have `pandas` installed for dummy data generation.
