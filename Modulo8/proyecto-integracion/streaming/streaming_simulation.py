import json
import random
import time
from datetime import datetime, timedelta
from collections import defaultdict

def generate_event():
    users = ['user1', 'user2', 'user3']
    actions = ['click', 'view', 'purchase']
    products = ['productA', 'productB', 'productC']
    return {
        'timestamp': datetime.now().isoformat(),
        'user': random.choice(users),
        'action': random.choice(actions),
        'product': random.choice(products)
    }

def enrich_event(event):
    user_profiles = {
        'user1': {'age': 25, 'location': 'NY'},
        'user2': {'age': 30, 'location': 'CA'},
        'user3': {'age': 22, 'location': 'TX'}
    }
    profile = user_profiles.get(event['user'], {})
    event.update(profile)
    return event

def process_window(events):
    summary = defaultdict(lambda: {'click': 0, 'view': 0, 'purchase': 0})
    for event in events:
        user = event['user']
        action = event['action']
        summary[user][action] += 1
    return summary

def simulate_streaming(window_seconds=10, total_duration_seconds=30):
    start_time = datetime.now()
    window_start = start_time
    event_buffer = []

    while (datetime.now() - start_time).seconds < total_duration_seconds:
        event = generate_event()
        enriched_event = enrich_event(event)
        event_buffer.append(enriched_event)
        print("Received event:", json.dumps(enriched_event))

        if (datetime.now() - window_start).seconds >= window_seconds:
            print("\n--- Window Summary ---")
            summary = process_window(event_buffer)
            for user, actions in summary.items():
                print(f"{user}: {actions}")
            print("----------------------\n")
            event_buffer = []
            window_start = datetime.now()

        time.sleep(1)

simulate_streaming()