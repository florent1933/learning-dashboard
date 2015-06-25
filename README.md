# learning-dashboard for Placis

## Requirements

Tools to install:
- elasticsearch 1.5.2
- kibana 4.0.2
- java 1.8 for elasticsearch
- Python3 to generate fixtures


## How to start?

### 1. Start ES and kibana

./bin/elasticsearch
./bin/kibana


### 2. Load fixtures (only the first time)


```
python3 start.py cf
```


We use the Tin Can API format.



### 3. Visualize data


#### Configure Kibana (only the first time)

Deactivate Index contains time-based events

Add index name *placis*


#### Watch fixtures


Kibana: http://localhost:5601/

## Fixtures

Verbs come from : https://registry.tincanapi.com



#### Create fixtures

```
python start.py [arguments]
```

*arguments* :

- g : get indexes from ES
- d : delete indexes on ES
- c : create indexes on ES
- f : creates fixtures on ES

```
Example :
python start.py dcf
```


### 4. Load dashboard

Use of elasticdump

Install like that:

```
npm install elasticdump -g
```

Tuto from http://air.ghost.io/kibana-4-export-and-import-visualizations-and-dashboards/


#### Importing

```
elasticdump \  
    --input=http://localhost:9200/.kibana  \
    --output=$ \
    --type=data \
    --searchBody='{"filter": { "or": [ {"type": {"value": "dashboard"}}, {"type" : {"value":"visualization"}}] }}' \
    > kibana-exported.json
```

#### Exporting

Kibana-exported is in in the kibana-save folder


```
elasticdump \  
    --input=kibana-exported.json \
    --output=http://localhost:9200/.kibana \
    --type=data
```
