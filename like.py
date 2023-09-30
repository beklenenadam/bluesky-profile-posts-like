from atproto import Client, models
import time

def main(client: Client, handle: str):
    print(f"\n {handle}'s posts")
    
    count = 0

    profile_feed = client.app.bsky.feed.get_author_feed({'actor': handle})
    for feed_view in profile_feed.feed:
        count = count + 1
        print(count, '-', feed_view.post.record.text)
        try:
            client.like(models.create_strong_ref(feed_view.post))
        except Exception as e:
            print(f"Hata: {e}")
            time.sleep(60)
            client = recreate_session()

def create_session():
    at_client = Client()
    at_client.login('handle', 'password')
    return at_client

def recreate_session():
    print("Yeniden oturum oluşturuluyor...")
    time.sleep(60)
    return create_session()

if __name__ == '__main__':
    at_client = create_session()

    while True:
        input_handle = input('\nEnter the username of the profile whose posts you want to like: ')
        main(at_client, input_handle)
