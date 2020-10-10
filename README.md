# MELKE
python package that extracts entities and relations from bio-text
<br> <br> <br>
## about MELKE
### 1. Installation
You can install MELKE package with PIP INSTALL 
<br>https://pypi.org/project/MELKE/1/
> pip install MELKE

<br> <br>

### 2. Functions
There is a module contains 2 functions. <br>
- Module: EntityRelation
- Functions: ExtractEntity, EntityRelation
##### 1. ExtractEntity
- Extract all of entities from input which is BIO-text. <br>
- It will return the result with python dictionary object. <br>
- Key is entity_id and value is dictionary of information about entity. <br>
##### 2. EntityRelation
- Extract all of entities and relations from input which is BIO-text. <br>
- It will return the result with python dictionary object. <br>
- Key is entity_1_entity_2 (connect first entity and second entity with under bar) and value is dictionary of information about relation. <br> <br> <br>

### 3. Examples
##### 0. First import
<img src="./image/example0.png" width="70%">
![example0](./image/example0.png)
<br>
If you import module very first time, Resources will be downloaded by init file.
And you will see this message from your console.

##### 1. How to use
<img src="./image/example1.png" width="70%">
![example1](./image/example1.png)

##### 2. Returned object of ExtractEntity
<img src="./image/example2.png" width="70%">
![example2](./image/example2.png)

##### 3. Returned object of EntityRelation
<img src="./image/example3.png" width="70%">
![example3](./image/example3.png)
