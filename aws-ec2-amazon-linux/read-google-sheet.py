import boto3
from botocore.exceptions import ClientError
import gspread
import json
import pandas as pd

secret_name = "my-google-github-sa"
region_name = "us-east-1"

session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=region_name
)

try:
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
except ClientError as e:
    print(e)
    exit()

secret = get_secret_value_response['SecretString']
key_data = json.loads(secret)
gc = gspread.service_account_from_dict(key_data)
sht1 = gc.open_by_key('1dsYt-kroqo9neVpV_VeJewNIt-mOzTdrPUq6nx5-Z-w')
worksheet = sht1.worksheet("Stock-list")
list_of_dicts = worksheet.get_all_records()
df=pd.DataFrame(list_of_dicts)
print(df)