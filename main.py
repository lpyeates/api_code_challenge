import requests
import csv
from time import sleep


def get_data():
    url = 'https://atlas.pretio.in/atlas/coding_quiz'
    headers = {
        'Authorization': 'Bearer LpNe5bB4CZnvkWaTV9Hv7Cd37JqpcMNF',
        'Content - Type': 'application / json; charset = utf - 8'
    }
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 429:
        # retry
        sleep(60)
        get_data()
    elif response.status_code == 500:
        return response.message
    elif response.status_code == 401:
        return response.message
    else:
        data = response.json()
        write_to_csv(data)



def write_to_csv(data):
    data_file = open('data_file.csv', 'w')
    csv_writer = csv.writer(data_file)
    content = data['rows']
    count = 0
    for row in content:
        if count == 0:
            header = row.keys()
            csv_writer.writerow(header)
            count += 1

        csv_writer.writerow(row.values())

    data_file.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_data()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
