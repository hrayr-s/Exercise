"""
A dummy data generator for the project
"""
import random
from datetime import datetime, timedelta
from string import ascii_lowercase

import pandas as pd
from pandas import DataFrame

columns = [
    'SN',
    'Run_Time',
    'Site',
    'Operation',
    'Equipment',
    'Status.1',
    'Name',
    'Input',
    'Output',
    'High_Limit',
    'Low_Limit',
    'Status.2',
]
df = DataFrame(
    columns=columns,
).astype({
    'SN': str,
    'Run_Time': str,
    'Site': str,
    'Operation': str,
    'Equipment': str,
    'Status.1': str,
    'Name': str,
    'Input': float,
    'Output': float,
    'High_Limit': float,
    'Low_Limit': float,
    'Status.2': str,
})

aug = pd.read_csv('data/ProductDescSample.csv')
# aug = [
#     '123AB45',
#     '123AB55',
#     '681AB45',
#     '123ZF55',
# ]

part_serial_prefix = {
    'V8_Motor': 1,
    'Gear_Box': 2,
    'Panel': 3,
    'Hood_Cover': 4,
}

sites = ['S1', 'S2', 'S3', 'S4']
statuses = ['OK', 'NOK']
actions = [
    "measure voltage",
    "measure temperature",
]

start_time = datetime.now() - timedelta(days=5)
end_time = datetime.now()


def gen_serial(part_name: str) -> str:
    return (
        f"{part_serial_prefix[part_name]}"
        f"{str(random.randint(1, 100)).zfill(3)}"
        f"{''.join(random.sample(ascii_lowercase, k=2))}"
        f"{str(random.randint(1, 100)).zfill(3)}"
    )


if __name__ == '__main__':

    part_names = list(part_serial_prefix.keys())

    while end_time >= start_time:
        part = random.choice(part_names)
        sn = gen_serial(part)
        site = random.choice(sites)

        current_measurements = []
        OK = 'OK'

        for _ in range(5):

            action = random.choice(actions)

            if action == 'measure voltage':
                action_input = round(random.random() * 60 + 1, 2)
                action_output = round(random.random() * 2 - 1, 2)
                high_limit = 0
                low_limit = -1
            else:
                action_input = ''
                action_output = round(random.random() * 20 + 25, 2)
                high_limit = 30
                low_limit = 25

            if low_limit < action_output < high_limit:
                index_status = 'PASS'
            else:
                index_status = 'FAIL'
                OK = 'NOK'

            current_measurements.append([
                sn,
                start_time,
                site,
                '0105',
                'ST51',
                'OK',
                action,
                action_input,
                action_output,
                high_limit,
                low_limit,
                index_status,
            ])

        for row in current_measurements:
            row[5] = OK
            df.loc[len(df.index)] = row

        aug.loc[len(aug.index)] = [part, sn]

        start_time = start_time + timedelta(seconds=random.randint(20, 50))
        print(start_time, end='\r')

    df.to_csv('data/products6.csv', index=False)
    aug.to_csv('data/products6desc.csv', index=False)

