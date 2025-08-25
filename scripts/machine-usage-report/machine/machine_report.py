# Function to extract the date from an event
def get_event_date(event):
    return event.date

# Function to track which users are currently logged into which machines
def current_users(events):
    # Sort events in chronological order (important so logins/logouts are processed correctly)
    events.sort(key=get_event_date)
    
    # Dictionary to map machine -> set of current users
    machines = {}
    
    # Process each event
    for event in events:
        # If the machine hasn't been seen before, add it to the dictionary
        if event.machine not in machines:
            machines[event.machine] = set()
        
        # Handle login event: add user to that machine
        if event.type == "login":
            machines[event.machine].add(event.user)
        
        # Handle logout event: remove user from that machine
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    
    return machines  # Return dictionary of machines with current users

# Function to generate and print the final report
def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            # Join multiple users with a comma
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))
        else:
            # Optional: show machines with no users
            print("{}: (no users)".format(machine))

# Class to represent an event (login/logout activity on a machine)
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date      # Date/time of the event
        self.type = event_type      # "login" or "logout"
        self.machine = machine_name # Machine name (e.g., server, workstation)
        self.user = user            # Username involved in the event

# Sample event data (normally would come from system logs)
events = [
    Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

# Process events to find current users
users = current_users(events)

# Debug print: show the raw dictionary
print(users)

# Generate the final formatted report
generate_report(users)
