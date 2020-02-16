# import the AWS SDK for python (boto3) - http://boto3.readthedocs.io/en/latest/
import boto3
# import json module to serialize JSON - https://docs.python.org/3.6/library/json.html
import json

# instantiate a new comprehend client
comprehend = boto3.client(service_name='comprehend', region_name='ap-northeast-2')

# provide english and spanish text to analyze
english_string = 'Machine Learning is fascinating.'
spanish_string = 'El aprendizaje automático es fascinante.'
# 2020.02.16. KY adds Korean string
korean_string = '머신러닝은 환상적인 서비스를 제공합니다 :-)'

print('Calling DetectDominantLanguage')

print('english_string result:')
# json.dumps() writes JSON data to a Python string
print(json.dumps(comprehend.detect_dominant_language(Text = english_string), sort_keys=True, indent=4))

print('\n spanish_string result:')
print(json.dumps(comprehend.detect_dominant_language(Text = spanish_string), sort_keys=True, indent=4))
# print('End of DetectDominantLanguage\n')

# 2020.02.16. KY adds Korean string
print('\n korean_string result:')
print(json.dumps(comprehend.detect_dominant_language(Text = korean_string), sort_keys=True, indent=4))
print('End of DetectDominantLanguage\n')
