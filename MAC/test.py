#test.py

import pdfkit

# URL of the webpage you want to convert
url = 'https://debank.com/profile/0x36cc7b13029b5dee4034745fb4f24034f3f2ffc6'

# Output PDF file path
output_path = 'debank_profile.pdf'

# Configuration for wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')  # Adjust the path if necessary

# Options for pdfkit
options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None,
    'enable-local-file-access': None,
    'zoom': '1.0',  # Adjust zoom level if needed
    'javascript-delay': '3000',  # Wait for JavaScript to load, increase if necessary
    'load-error-handling': 'ignore',  # Ignore errors if needed
    'load-media-error-handling': 'ignore',  # Ignore media load errors if needed
}

# Convert webpage to PDF
pdfkit.from_url(url, output_path, options=options, configuration=config)
