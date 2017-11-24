import boto3
import StringIO
import zipfile
import mimetypes

def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:eu-west-2:940878095277:DeployPortfolioTopic')

    try:
        s3 = boto3.resource('s3')
        
        portfolio_bucket = s3.Bucket('portfolio.t3a9.com')
        build_bucket = s3.Bucket('portfoliobuild.t3a9.com')

        portfolio_zip = StringIO.StringIO()
        build_bucket.download_fileobj('portfoliobuild.zip',portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
               obj = myzip.open(nm)
               portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
        print 'Job done.'
        topic.publish(Subject='Portfolio Deployed', Message='Portfolio deployed successfully.')
    except:
        topic.publish(Subject='Portfolio Deployed Failed', Message='The Portfolio was not deployed successfully.')
        raise
    return 'Deployed a new build.'
