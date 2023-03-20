
all_users = {}
all_albums = {}


def add_user(username: str, age: int, city: str, albums: list, all_users: dict, all_albums: dict):
    all_users[username] = {
        'age': age,
        'city': city,
        'albums': albums
    }


def add_album(name: str, artist_name: str, genre: str, tracks: int, all_users: dict, all_albums: dict):
    all_albums[name] = {
        'artist_name': artist_name,
        'genre': genre,
        'tracks': tracks
    }


def query_user_artist(username: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    result = 0
    music_lst = all_users[username]['albums']
    for i in music_lst:
        if i in all_albums:
            if all_albums[i]['artist_name'] == artist_name:
                result += all_albums[i]['tracks']
    return result


def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    result = 0
    music_lst = all_users[username]['albums']
    for i in music_lst:
        if i in all_albums:
            if all_albums[i]['genre'] == genre:
                result += all_albums[i]['tracks']

    return result


def query_age_artist(age: int, artist_name: str, all_users: dict, all_albums: dict) -> int:
    result = 0
    for name in all_users:
        if all_users[name]['age'] == age:
            for al in all_users[name]['albums']:
                if al in all_albums:
                    if all_albums[al]['artist_name'] == artist_name:
                        result += all_albums[al]['tracks']
    return result


def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    result = 0
    for name in all_users:
        if all_users[name]['age'] == age:
            for al in all_users[name]['albums']:
                if al in all_albums:
                    if all_albums[al]['genre'] == genre:
                        result += all_albums[al]['tracks']
    return result


def query_city_artist(city: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    result = 0
    for name in all_users:
        if all_users[name]['city'] == city:
            for al in all_users[name]['albums']:
                if al in all_albums:
                    if all_albums[al]['artist_name'] == artist_name:
                        result += all_albums[al]['tracks']

    return result


def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    result = 0
    for name in all_users:
        if all_users[name]['city'] == city:
            for al in all_users[name]['albums']:
                if al in all_albums:
                    if all_albums[al]['genre'] == genre:
                        result += all_albums[al]['tracks']
    return result
