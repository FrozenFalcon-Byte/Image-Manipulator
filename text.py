import requests


def remove_bg(path):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(path, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'YOUR_API_KEY'},
    )
    
    if response.status_code == requests.codes.ok:
        output_path = 'no-bg.png'
        with open(output_path, 'wb') as out:
            out.write(response.content)
        return output_path 
    else:
        return f"Error: {response.status_code}, {response.text}"
