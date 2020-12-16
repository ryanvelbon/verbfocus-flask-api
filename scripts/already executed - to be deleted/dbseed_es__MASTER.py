import os


# truncate entire database before seeding



os.system('python -m scripts.dbseed_es_person')
os.system('python -m scripts.dbseed_es_tense')
# os.system('python -m scripts.dbseed_es_verb')
# os.system('python -m scripts.dbseed_es_vconj')