import boto3
import StringIO
import zipfile
import mimetypes

session = boto3.Session(profile_name='t3a9-admin')
s3 = session.resource('s3')

portfolio_bucket = s3.Bucket('portfolio.t3a9.com')
build_bucket = s3.Bucket('portfoliobuild.t3a9.com')

portfolio_zip = StringIO.StringIO()
build_bucket.download_fileobj('portfoliobuild.zip',portfolio_zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
       obj = myzip.open(nm)
       portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
