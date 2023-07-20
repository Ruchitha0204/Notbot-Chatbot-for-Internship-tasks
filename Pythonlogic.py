//the logic for chat-bot while using python
//code starts  from below 
.........................
msg = input()
reply_to_user = ""
check = True
if check:
    user_enter_name_check = (msg.lower() == "hi")
    check_yes_no_options = (msg.lower() == "yes" or msg.lower() == "no")
    check_email_address = False
    if user_enter_name_check:
        reply_to_user = "Hi! Are you here to apply for the Internship? \n Enter - Yes or No"
        user_enter_name_check = False
    elif check_yes_no_options:
        reply_to_user = "Please enter your Name"
        check_yes_no_options = False
    elif msg.isalpha() and not msg.endswith(".com"):
        if msg.isalpha():
            reply_to_user = "Please Enter Your Email"
        else:
            reply_to_user = "Please enter your Name"
    elif msg.isdigit():
        reply_to_user = "Thanks for connecting. We will get back to you shortly"
    else:
        reply_to_user = "Please select how many years of experience you \n Show List: \n 1. 1 Year\n 2. 2 Year\n 3. 3 Year\n 4. 4 Year\n 5. 5 Year"

    
print(reply_to_user)
