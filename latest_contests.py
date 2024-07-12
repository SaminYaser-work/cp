import requests
from datetime import datetime, timedelta
import pytz
import urllib.parse

TIMEZONE = 'Asia/Dhaka'

contests = {
    'codeforces': []
}


def shorten_url(long_url):
    tinyurl_api = "http://tinyurl.com/api-create.php"
    response = requests.get(tinyurl_api, params={'url': long_url})
    return response.text


def generate_gcal_link(details):
    gcal_base_url = "https://www.google.com/calendar/render"
    gcal_link = f"{gcal_base_url}?{urllib.parse.urlencode(details)}"
    return shorten_url(gcal_link)


def format_codeforces_data(contest):
    # Create timezone object
    timezone = pytz.timezone(TIMEZONE)

    # Convert startTimeSeconds to human-readable date and time in the specified timezone
    start_time = datetime.fromtimestamp(
        contest['startTimeSeconds'], tz=pytz.utc).astimezone(timezone)
    start_time_str = start_time.strftime('%d/%m/%Y %I:%M:%S %p')

    # Calculate end time
    end_time = start_time + timedelta(seconds=contest['durationSeconds'])
    end_time_str = end_time.strftime('%d/%m/%Y %I:%M:%S %p')

    # Convert durationSeconds to hours, minutes, and seconds
    duration = str(timedelta(seconds=contest['durationSeconds']))

    # Convert relativeTimeSeconds to human-readable format
    relative_time = str(timedelta(seconds=contest['relativeTimeSeconds']))

    # Create Google Calendar link
    start_time_gcal = start_time.strftime('%Y%m%dT%H%M%S')
    end_time_gcal = end_time.strftime('%Y%m%dT%H%M%S')
    details = {
        'action': 'TEMPLATE',
        'text': contest['name'],
        'dates': f"{start_time_gcal}/{end_time_gcal}",
        'details': f"Contest ID: {contest['id']}\nType: {contest['type']}\nDuration: {duration}",
        'trp': 'false',
        'sprop': '',
        'location': 'Online',
        'ctz': TIMEZONE
    }
    gcal_link = generate_gcal_link(details)

    # Construct the human-readable format
    readable_format = \
        f"""{contest['name']} - {start_time_str} ({relative_time})
    Add to Calendar: {gcal_link}
    """

    return readable_format


# Codeforces
response = requests.get('https://codeforces.com/api/contest.list?gym=false')

if (response.status_code == 200):
    response = response.json()
    for res in response['result']:
        if res['phase'] != 'BEFORE':
            break

        contests['codeforces'].append(format_codeforces_data(res))

    contests['codeforces'].reverse()

    print('CODEFORCES')
    print('----------------------')
    print('See all:', 'https://codeforces.com/contests\n')
    for i, con in enumerate(contests['codeforces']):
        print(str(i+1) + '.', con)
