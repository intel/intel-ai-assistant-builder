import datetime
import win32com.client
import json
import random
from tzlocal import get_localzone

import superbuilder_middleware_pb2 as sb

def get_outlook_meetings():
    meetings =[]
    # Connect to Outlook
    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    calendar_folder = namespace.GetDefaultFolder(9)  # 9 refers to the Calendar folder

    # Get today's date
    today = datetime.datetime.now().date()
    start = datetime.datetime.combine(today, datetime.time.min)
    end = datetime.datetime.combine(today, datetime.time.max)

    # Restrict the calendar items to today's meetings
    restriction = "[Start] >= '{}' AND [End] <= '{}'".format(start.strftime("%m/%d/%Y %H:%M %p"), end.strftime("%m/%d/%Y %H:%M %p"))
    items = calendar_folder.Items
    items.IncludeRecurrences = False
    items.Sort("[Start]")
    restricted_items = items.Restrict(restriction)

    # Extract meeting details
    
    for item in restricted_items:
        if item.Class == 26:  # 26 refers to AppointmentItem
            if item.Subject and item.Subject.find("KOR")==-1:
                meeting = {
                    "Subject": item.Subject,
                    "Start": item.Start.Format("%Y-%m-%d %H:%M:%S"),
                    "End": item.End.Format("%Y-%m-%d %H:%M:%S"),
                    "Location": item.Location,                    
                }
            meetings.append(meeting)
    return meetings


def build_meetings_prompt(json_string):

    # Parse the JSON string
    calendar_items = json.loads(json_string)
    
    # Convert the start and end times to datetime objects and sort the items by start time
    for item in calendar_items:
        item['Start'] = datetime.datetime.strptime(item['Start'], '%Y-%m-%d %H:%M:%S')
        item['End'] = datetime.datetime.strptime(item['End'], '%Y-%m-%d %H:%M:%S')
    sorted_calendar_items = sorted(calendar_items, key=lambda x: x['Start'])
    
    # Build the prompt string
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    prompt_lines = [f"The following appointments are found from my calendar. Call out number of appointments and tell me if there are conflicts. Please suggest for preparation or follow-ups. Keep the reply brief and easy to understand. Important: Only use your own knowledge. Do not use any existing context. Do not add reference at the end. Here are the appointments:"]
    
    for appointment in sorted_calendar_items:
        prompt_lines.append(
            f"* {appointment['Subject']}, Location: {appointment['Location']}, Start time: {appointment['Start']}, End time: {appointment['End']}"
        )    
    prompt = "\n".join(prompt_lines)
    return prompt

def gen_appointment(stub):    
    session_id = init_chat_session(stub)
    success = False
    print(f"init_default_params")
    parametersReq = init_default_params()  
    reply = stub.SetParameters(parametersReq)
    prompt = "suggest one family friendly fun activity to attend in Las Vegas area for today. Only list headline. do not elaborate. do not add note. do not summary. "
    request = sb.ChatRequest(name='SuperBuilder Python Clients!', prompt=prompt,sessionId=session_id, attachedFiles="[]")
    print("\nEvent: ")
    response = get_chat_response(stub.Chat(request))
    return session_id,response


# Note:: only works with enterprise outlook not new outlook
def save_appointment(response, session_id, stub):
    start,end = generate_random_time_block()
    local_time_offset = datetime.datetime.now(get_localzone()).utcoffset()
    print(f"\ntime: {start - local_time_offset}-{end - local_time_offset}")
    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    calendar_folder = namespace.GetDefaultFolder(9)
    appointment = calendar_folder.Items.Add(1)
    appointment.Subject = response
    appointment.Start = start
    appointment.End = end
    '''
    #appointment.Location = event_details.get('Location', '')
    #appointment.Body = responses['body']
    #appointment.RequiredAttendees = "me@me.com; you@you.com"
    userInput = input("\nSave to calendar? (Y/N): ").strip().upper()
    if userInput == "Y":
        appointment.Save()
        print("saved appointment")
    '''
    appointment.Save()
    clean_session(session_id,stub)
    success=True
    return success

def generate_random_time_block():
    now = datetime.datetime.now(get_localzone())
    end_time_limit = now + datetime.timedelta(hours=4)
    # Calculate the total number of minutes from now to 4 hours from now
    total_minutes = int((end_time_limit - now).total_seconds() // 60)
    
    # Generate a random start time within this range
    random_start_minutes = random.randint(0, total_minutes - 30)
    random_start = now + datetime.timedelta(minutes=random_start_minutes)
    random_end = random_start + datetime.timedelta(minutes=30)

    local_time_offset = datetime.datetime.now(get_localzone()).utcoffset()
    start = random_start + local_time_offset
    end = random_end + local_time_offset
    
    return start, end