
import jpype, os, site

# MELKEAPI Class load
MELKEAPI = jpype.JClass('edu.yonsei.driver.MELKEAPI')()
path = site.getsitepackages()[1]+'\\melke\\'
MELKEAPI.loadProperties(path+"config\\melke.properties") # -- loadProperties 함수 실행


# entity 추출 함수
def ExtractEntity(text) :
    entity_result = MELKEAPI.extractEntity(text)
    return entity_result

# relation 추출 함수
def EntityRelation(text) :
    relation_result = MELKEAPI.extractEntityRelation(text)
    return relation_result

