# Flash Mock 2
FlashMock is a program I developed to automate subscription payment processing through Square, allowing a company I previously worked with to charge customers before their merchant account had built-in automatic billing capabilities.
### What it does:
1. Open Firefox and log into Square.com, signing into the merchant account.
2. Navigate to the payment interface.
3. Authenticate the user, retrieve and decrypt a single database row, then send the JSON-formatted data to the Python program.
4. Auto-fill the Square payment interface with the JSON data and related payment details.
5. If the charge is successful, generate an invoice with customer information for business records. The customer is also sent an email.
### Main Features:
* A framework to handle selenium commands
* Generate HTML documents based on program activities
* Error management and logging
* Securly handles business processes; saving time, money, and liability

Run ```python main.py``` in the powershell directory to start program.