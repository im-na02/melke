# MELKE
python package that extracts entities and relations from bio-text
<br> <br>
### about MELKE
#### [1] Installation
You can install MELKE package with PIP INSTALL 
<br>https://pypi.org/project/MELKE/1/
> pip install MELKE
<br>

#### [2] Functions
There is 1 module contains 2 functions.
EntityRelation(module): ExtractEntity, EntityRelation(functions)
<br>
##### 1. ExtractEntity
Extract all of entities from input which is BIO-text. <br>
It will return the result with python dictionary object. <br>
Key is entity_id and Values are information of entity_id. <br> <br>
##### 2. EntityRelation
Extract all of entities and relations from input which is BIO-text. <br>
It will return the result with python dictionary object. <br>
Key is entity_1_entity_2 (connect first entity and second entity with under bar) and Values are information of that relation. <br> <br>

#### [3] Examples
