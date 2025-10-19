from helper import get_response


ticket_1= """
 Hi there! My name is John Smith, and I am experiencing issues with your premium software, XYZ Pro. My license key is ABC12345. I purchased it last week, but it's not activating properly on my computer.
"""

entities_1= """
* Customer Details:
  - Name: John Smith
  - License Key: ABC12345
* Product/Service Mentions:
  - Product: XYZ Pro (premium software)
"""

ticket_2= """
 Dear support team, I am writing to inquire about the delivery status of my order. My name is Jane Doe, and I placed an order for a laptop on your website two days ago. The order number is ORD56789. Can you please provide an update on the delivery?
"""

entities_2="""
* Customer Details:
  - Name: Jane Doe
* Product/Service Mentions:
  - Product: laptop
"""

ticket_3= """
 Hello, I am having trouble accessing my account on your mobile app. My name is Alex Johnson, and I have a subscription for your Gold Plan. Can you help me resolve this issue?
"""

entities_3= """
* Customer Details:
  - Name: Alex Johnson
* Product/Service Mentions:
  - Product: mobile app
  - Service: Gold Plan
"""

ticket_4= """
Greetings, I am facing technical difficulties with your software, ABC Editor. My name is Sarah Lee, and I recently upgraded to the latest version. However, whenever I try to save my work, the software crashes. Can you please help me resolve this problem?
"""

# extract entities from ticket_4 with one-shot prompting
prompt = f""" 
            Ticket: {ticket_1} -> Entities: {entities_1}
            Ticket: {ticket_2} -> Entities: {entities_2}
            Ticket: {ticket_3} -> Entities: {entities_3}
            Ticket: {ticket_4} -> Entities: """
            
response = get_response(prompt)

      
print("Ticket: \n", ticket_4)
print("Entities: \n", response)      