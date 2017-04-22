# coding=utf-8
"""
1) Using the user_db_tools module, import the people.txt file.

2) Normalize the cities in a repeatable fashion, then import more_people.csv
    Normalizing means doing something to make sure that Wash DC can always be displayed as Washington, DC

3) Print out to screen all the users with normalized locations

"""

from user_db_tools import FriendFetcherDb
import csv


def main():
    file_names = ['people.csv', 'more_people.csv']
    with FriendFetcherDb() as db:
        db.setup_db()

        for name in file_names:
            locations = set()

            # Import data from csv files
            with open(name) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if db.fetch_info("SELECT count(*) FROM users WHERE screen_name = '{}'".format(row['name']))[0][0] != 0:
                        continue
                    db.ad_hoc(
                        "INSERT INTO users (screen_name, location) VALUES ('{0}', '{1}');".format(row['name'], row['location']))

            # Normalize the data
            results = db.fetch_info("SELECT location FROM users")
            for result in results:
                locations.add(result[0])

            for key in locations:
                parts = key.split()
                match = True
                if db.fetch_info("SELECT count(*) FROM locations WHERE location = '{}'".format(key))[0][0] != 0:
                    continue
                for loc in locations:
                    for part in parts:
                        if part in loc and len(key) < len(loc):
                            continue
                        else:
                            match = False
                            break
                    if match:
                        db.ad_hoc(
                            "INSERT INTO locations (normal_location, location) VALUES ('{0}', '{1}')".format(loc, key))
                        db.ad_hoc(
                            "INSERT INTO locations (normal_location, location) VALUES ('{0}', '{1}')".format(loc, loc))

        results = db.fetch_info("SELECT users.screen_name, locations.normal_location \
                        FROM users\
                        INNER JOIN locations ON users.location=locations.location"
                                )
        for res in results:
            print("{0}\t{1}".format(res[0], res[1]))

    return


if __name__ == '__main__':
    main()
