# MELKE
python package that extracts entities and relations from bio-text
<br> <br> <br>
## about MELKE
### 1. Installation
You can install MELKE package with PIP INSTALL 
<br>https://pypi.org/project/MELKE/1/
> pip install MELKE

<br> <br>

## 2. Functions
There is a module contains 2 functions. <br>
- Module: EntityRelation
- Functions: ExtractEntity, EntityRelation
### 1. ExtractEntity
- Extract all of entities from input text about BIO. <br>
- It will return result as python dictionary object. <br>
- Key is entity_id and value is dictionary of information about entity. <br>
### 2. EntityRelation
- Extract all of entities and relations from input which is BIO-text. <br>
- It will return the result with python dictionary object. <br>
- Key is entity_1_entity_2 (connect first entity and second entity with under bar) and value is dictionary of information about relation. <br> <br> <br>

## 3. Examples
### 0. When you import MELKE very first
> <img src="./image/example0.png" width="50%">

when you import module very first time, Resources will be downloaded by init file. <br>
And you will see this message from your console.
<br> <br>

### 1. How to use
<img src="./image/example1.png" width="70%">
<br>

### 2. Returned object of ExtractEntity
<img src="./image/example2.png" width="70%">
<br>

### 3. Returned object of EntityRelation
<img src="./image/example3.png" width="70%">
<br>

### 4. Structure of dictionary (ExtractEntity)
<img src="./image/example4.png" width="70%">

#### key
- entity_id
#### value (dictionary)
- sent_id: sentent id
- entity: entity
- type: entity type
- sentence: raw text
- start: starting index of entity(word) from sentence
- end: ending index of entity from sentence
<br>

### 5. Structure of dictionary (EntityRelation)
<img src="./image/example5.png" width="70%">

#### key
- entity_1_entity_2 (connect first entity and second entity with under bar)
#### value (dictionary)
- sent_id: sentent id
- entity_1: first entity
- entity_type_1: type of first entity
- entity_2: second entity
- entity_type_2: type of second entity
- negation: positive or negative
- type: type of relation
- sentence: raw text
<br>

