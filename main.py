from datetime import date
import requests

from utils import *


def login():
    user = get_json('credentials.json')
    headers = get_headers('initial')
    r = requests.get('https://secure.meetup.com/login/', headers=headers)

    headers = get_headers('login')
    data = {
        'email': user['email'],
        'password': user['password'],
        'rememberme': 'on',
        'token': find_token(r.text),
        'submitButton': 'Log in',
        'returnUri': 'https://www.meetup.com/',
        'op': 'login',
        'apiAppClientId': ''
    }
    loginResponse = requests.post('https://secure.meetup.com/login/', data=data)

    if loginResponse.text.find("Your email or password was entered incorrectly") != -1:
        print("Login Failed!")

    if (loginResponse.status_code != 200):
        print("Login Failed!")
        return

    print("Authorized Succesfully!")


    print(loginResponse.headers['Set-Cookie'])
    # token = "memberId"
    
    # index = text.find(token)

    # while index != -1:
    #     print(text[index-100:index+100])
    #     print("\n")
    #     index = text.find(token, index+len(token))

    # groups = get_json('groups.json')

    #     print("Getting events for " + group['name'])
    #     get_events(group['name'], group['end_date'])
    #     print("\n\n")




def get_events(group: str, endDate: str):
        """
        Gets all events from a group till configured date , 
        rsvps to them , if dryrun parameter is not True
        if not configured , queried till a month later
        """
        
        startDate = str(date.today())
        requests.headers = get_headers('standard')
        requests.headers['referer'] = getUrl(group) + 'events/calendar/'
        requests.headers['x-meetup-activity'] = 'standardized_url=%2Furlname%2Fevents%2Fcalendar%2Fdate&standardized_referer=%2Furlname%2Fevents'

        queryStr = '(endpoint:members/self,meta:(method:get),params:(fields:\'memberships, privacy\'),ref:self,type:member),(endpoint:noop,flags:!(facebook_login_active,feature_microtargets_MUP-16377,nwp_event_template_MUP-16782,wework-announce,feature_google_tag_manager_MUP-19169),meta:(metaRequestHeaders:!(unread-notifications,unread-messages,admin-privileges,tos-query,facebook-auth-url,google-auth-url),method:get),params:(),ref:headers,type:headers),' + \
                   '(endpoint:' + group + ',meta:(flags:!(feature_app_banner_MUP-16415,feature_new_group_event_home_MUP-16376,feature_new_group_home_sharing_MUP-16516,feature_twitter_group_sharing_MW-2381),method:get),params:(country:in,fields:\'category,city_link,fee_options,join_info,leads,localized_location,membership_dues,member_sample,other_services,past_event_count,draft_event_count,proposed_event_count,pending_members,photo_count,photo_sample,photo_gradient,plain_text_description,plain_text_no_images_description,profile,self,topics,nominated_member,nomination_acceptable,member_limit,leader_limit,last_event,welcome_message,pro_rsvp_survey\',state:\'\'),ref:group,type:group),' + \
                   '(endpoint:' + group + '/events,list:' \
                   + '(dynamicRef:\'list_events_for_period_' + group + "_" + startDate + 'T00:00:00.000_' + endDate + 'T00:00:00.000\'),meta:(method:get),params:(fields:\'comment_count,event_hosts,featured_photo,plain_text_no_images_description,series,self,rsvp_rules,rsvp_sample,venue,venue_visibility\',' \
                   + 'no_earlier_than:\'' + startDate + 'T00:00:00.000\',' \
                   + 'no_later_than:\'' + endDate + 'T00:00:00.000\',status:\'past,cancelled,upcoming\'),ref:\'' \
                   + 'events_for_period_' + group + "_" + startDate + 'T00:00:00.000_' + endDate + 'T00:00:00.000\')'

        params = (
            ('queries', queryStr),
        )

        response = requests.get('https://www.meetup.com/mu_api/urlname/events/calendar/date', params=params)
        response = json.loads(response.text)
        name = response['responses'][2]['value']['name']
        events = response['responses'][3]['value']
        events.sort(key=lambda event: event['created'], reverse=True)  # Reverse sorting via date of creation

        for event in events:
            event = Event(event)
            
 
class Event:
    def __init__(self, json: dict):
        self.uniqueId = json['id']
        self.name = json['name']
        
        try:
            self.rsvp_limit = json['rsvp_limit']
        except:
            self.rsvp_limit = 0
        
        self.yes_rsvp_count = json['yes_rsvp_count']

        print(self.name)
        print(self.rsvp_limit)
        print(self.yes_rsvp_count)
        print("\n")
        

def getUrl(group: str):
     return 'https://www.meetup.com/' + group + '/'

if __name__ == '__main__':
    login()