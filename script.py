import requests


def main():
    cities = ['london', 'svo', 'череповец']

    for city in cities:
        response = requests.get("https://wttr.in/{}".format(city),
                                params={"MnTq": "", "lang": "ru"})
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
