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

Kibana: http://localhost:5601/


#### Configure Kibana (only the first time)

Deactivate Index contains time-based events

Add index name *placis*

## Fixtures

Verbs come from : https://registry.tincanapi.com


## Advanced

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

