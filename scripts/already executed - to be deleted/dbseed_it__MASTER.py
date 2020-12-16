import os


# truncate entire database before seeding



os.system('python -m scripts.dbseed_it_person')
os.system('python -m scripts.dbseed_it_tense')
os.system('python -m scripts.dbseed_it_verb')
# os.system('python -m scripts.dbseed_it_vconj')