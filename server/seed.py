import csv
import random
from app import app
from models import db
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        Appearance.query.delete()
        Guest.query.delete()
        Episode.query.delete()

        print("Seeding data from CSV...")

        with open('seed.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            episode_counter = 1
            for row in reader:
                # Create episode
                episode = Episode(
                    date=row['YEAR'],
                    number=episode_counter
                )
                db.session.add(episode)
                db.session.flush()  # gets episode.id before commit

                # Create guest
                guest = Guest(
                    name=row['Raw_Guest_List'],
                    occupation=row['GoogleKnowlege_Occupation']
                )
                db.session.add(guest)
                db.session.flush()  # gets guest.id before commit

                # Create appearance
                appearance = Appearance(
                    rating=random.randint(1, 10),
                    episode_id=episode.id,
                    guest_id=guest.id
                )
                db.session.add(appearance)

                episode_counter += 1

        db.session.commit()
        print("Seeding complete!")
