# import the AWS SDK for python (boto3) - http://boto3.readthedocs.io/en/latest/
import boto3
# import json module to serialize JSON - https://docs.python.org/3.6/library/json.html
import json

# instantiate a new comprehend client
# 2020.02.16. KY 
comprehend = boto3.client(service_name='comprehend', region_name='ap-northeast-2')

# provide english and spanish text to analyze
# 2020.02.16. KY
# english_string_list = ['Machine Learning is fascinating.', 'Studying Artificial Intelligence is my passion.'] 
# spanish_string_list = ['El aprendizaje automático es fascinante.', 'Estudiar Inteligencia Artificial es mi pasión.']
mixed_string_list = ['Machine Learning is fascinating.', 'El aprendizaje automático es fascinante.', '머신러닝은 환상적인 서비스를 제공합니다 :-)'] 

print('Calling BatchDetectDominantLanguage')

# 2020.02.16. KY
# print('english_string_list results:')
# json.dumps() writes JSON data to a Python string
# print(json.dumps(comprehend.batch_detect_dominant_language(TextList = english_string_list), sort_keys=True, indent=4))

# print('\nspanish_string_list results:')
# print(json.dumps(comprehend.batch_detect_dominant_language(TextList = spanish_string_list), sort_keys=True, indent=4))
print('\nmixed_string_list results:')
print('\nraw results')
print(comprehend.batch_detect_dominant_language(TextList = mixed_string_list))
print('\nresults using json.dumps')
print(json.dumps(comprehend.batch_detect_dominant_language(TextList = mixed_string_list), sort_keys=True, indent=4))
print('End of BatchDetectDominantLanguage\n') 
