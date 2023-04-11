import vonage
import openpyxl
import time

client = vonage.Client(key="25b48157", secret="adaDOvLV5Ac3KLR9")
sms = vonage.Sms(client)

workbook = openpyxl.load_workbook('numbers.xlsx')
worksheet = workbook['Sheet1']
for row in worksheet.iter_rows(min_row=1, max_row=50, values_only=True):
    recipient_number = row[0]
    responseData = sms.send_message({
        'from': '12506638706',
        'to': int(recipient_number),
        'text': 'Alert: Please update your informations and pay for the redelivery here: https://postglobals.com',
    })
    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
    time.sleep(8)
