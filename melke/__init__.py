from melke import *
import os, sys, jpype
import site
from urllib.request import urlretrieve
import zipfile


names = ['biological_process_index', 'biological_process_index', 'body_index', 'celllucene_index', 'compound_index', 
         'config', 'dict', 'gene_index', 'lib', 'model', 'molacular_function_index', 
         'molecular_function_lucene_index', 'name_finder', 'organlucene_index', 'phenotype_index', 'resources', 
         'species_index', 'text_classification', 'tissuelucene_index']

path = site.getsitepackages()[1]+'\\melke\\'

if os.path.exists(path+names[0]) :
    pass
else :
    print('Downloading files... (It will take about 30 minutes.)')
    for name in names :
        if not os.path.exists(path+name) :
            os.mkdir(path+name)
            urlretrieve("https://github.com/zzoliman/Project_Brazil/releases/download/test/"+name+".zip",
                        path+name+'.zip')
            with open(path+name+'.zip', 'rb') as fileobj:
                z = zipfile.ZipFile(fileobj)
                z.extractall(path+name)
                z.close()
            os.remove(path+name+'.zip')
    
    if not os.path.isfile(path+'ent_disambig_doc2vec.model') :
        urlretrieve("https://github.com/zzoliman/Project_Brazil/releases/download/test/ent_disambig_doc2vec.zip",
                    path+'ent_disambig_doc2vec.zip')
        with open(path+'ent_disambig_doc2vec.zip', 'rb') as fileobj:
            z = zipfile.ZipFile(fileobj)
            z.extractall(path)
            z.close()
        os.remove(path+'ent_disambig_doc2vec.zip')

classpath = os.pathsep.join([site.getsitepackages()[1]+'\\melke\\lib\\'+j
                             for j in [i for i in os.listdir(site.getsitepackages()[1]+'\\melke\\lib') if '.jar' in i]])
os.chdir(site.getsitepackages()[1]+'\\melke')

jvmpath = jpype.getDefaultJVMPath()

try :
    jpype.startJVM(
        jvmpath,
        '-Djava.class.path=%s' % classpath,
        '-Dfile.encoding=UTF8',
        '-ea', '-Xmx{}m'.format(4096),
        convertStrings=True
        )
except Exception as e :
    print(e)
