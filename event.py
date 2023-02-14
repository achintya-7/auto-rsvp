class Event:
    def __init__(self, json: dict):
        self.unique_id = json['id']
        self.name = json['name']

        self.guest_allowed = json['rsvp_rules']['guest_limit']

        if not self.guest_allowed:
            print("Guest listing not available for the Event !Removing +1")
            print("Guest listing not available")

        try:
            if (json['self']['rsvp']['response'] == 'yes'):
                # Already RSVP'd to the event
                print("Already RSVP'd/Waitlisted to!")
            self.rsvp_done = 1
            if (json['self']['rsvp']['response'] == 'no'):
                # Means the user has previously said NO to the event,manually
                print("Seems like you've said no to this event earlier")
            self.rsvp_done = 1
        except:
            # print ("Not Reacted to before")
            self.rsvp_done = 0