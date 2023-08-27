from atproto import Client

def main(client: Client, handle: str):
    print(f"\n {handle}'s posts")
    count = 0

    get_profile = client.bsky.feed.get_author_feed({'actor': handle, 'limit': 100})
    for profile_view in get_profile.feed:
        count = count + 1
        print(count, '-', profile_view.post.record.text)
        agent.like(profile_view.post)

if __name__ == '__main__':
    agent = Client()
    agent.login('bluesky-handle', 'bluesky-password')
  
    while True:
        input_handle = input('\nEnter the username of the profile whose posts you want to like: ')
        main(agent, input_handle)
