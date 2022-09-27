import requests


def main():
    params = [{"nTq": "", "lang": "en"}, {"nTq": "", "lang": "en"},
              {"MnTq": "", "lang": "ru"}]

    cities = ['london', 'svo', 'череповец']

    for i in range(len(cities)):
        response = requests.get("https://wttr.in/{}".format(cities[i]),
                                params=params[i])
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
