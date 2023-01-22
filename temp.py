from requests import get
from json import loads

# dodać odswieżanie i dodawanie do html

def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)

    for row in loads(response.text):
        print(row['stacja'])
    #     if row['stacja'] == request_city:
    #
    #         print('stacja', row['stacja'])
    #         print('data pomiaru', row['data_pomiaru'])
    #         print('godzina pomiaru', row['godzina_pomiaru'])
    #         print('temperatura', row['temperatura'])
    #         print('ciśnienie', row['cisnienie'])


if __name__ == '__main__':
    # request_city = input('Podaj dla jakiego miasta chcesz zobaczyć pogode?')
    main()