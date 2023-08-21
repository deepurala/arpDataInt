import subprocess
import boto3
from botocore.exceptions import NoCredentialsError

program_list = ['circuit.py', 'constructors.py', 'drivers.py', 'finishStatus.py', 'races.py','seasons.py','resultsMapped.py']

for program in program_list:
    subprocess.call(['python', program])
    print("Finished:" + program)

csv_files = ['circuits.csv', 'constructors.csv', 'drivers.csv', 'races.csv', 'results.csv', 'seasons.csv', 'status.csv']
ACCESS_KEY = ''
SECRET_KEY = ''


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful:"+local_file)
        return True
    except FileNotFoundError:  
        print("The file was not found:" +local_file)
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

for file in csv_files:
    uploaded = upload_to_aws(file, 'dataintegrationproj', file)