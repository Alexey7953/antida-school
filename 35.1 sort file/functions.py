def file_has_permissions(filename):
    try:
        with open(filename, 'rb') as f:
            f.readline()
        return True

    except PermissionError:
        print(f'Нет доступа к файлу {filename}')
        return False


def generate_new_name(title, artist, album):
    if title:
        return f'{title} - {artist} - {album}.mp3'
    else:
        return None
