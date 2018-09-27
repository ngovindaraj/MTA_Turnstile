import pandas as pd
import requests

MTA_df = pd.DataFrame()

urls = [
"http://web.mta.info/developers/data/nyct/turnstile/turnstile_180922.txt",
"http://web.mta.info/developers/data/nyct/turnstile/turnstile_180915.txt",
"http://web.mta.info/developers/data/nyct/turnstile/turnstile_180908.txt",
"http://web.mta.info/developers/data/nyct/turnstile/turnstile_180901.txt",
"http://web.mta.info/developers/data/nyct/turnstile/turnstile_180825.txt",
"http://web.mta.info/developers/data/nyct/turnstile/turnstile_180818.txt",
"http://web.mta.info/developers/data/nyct/turnstile/turnstile_180811.txt",
"http://web.mta.info/developers/data/nyct/turnstile/turnstile_180804.txt"
]

print(urls, '\n')

for url in urls:
    page = requests.get(url).text
    new_df = pd.read_csv(url, sep='\n')
    MTA_df = pd.concat([MTA_df, new_df])
print(MTA_df.describe())

MTA_df.to_csv(r'MTA_all_data.csv', index=None, sep=' ', mode='a')
