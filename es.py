import requests

def create_es():
    '''
    Create index placis in ES
    '''

    print('Create index placis in ES')
    config = '''
    {
        "mappings": {
            "user" : {
                "properties": {
                    "object": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "verb":{
                        "type": "string",
                        "index": "not_analyzed"
                    }
                }
            }
        }
    }
    '''

    r = requests.put("http://localhost:9200/placis?pretty", data=config)
    print('Response')
    print(r.text)


def delete_es():
    '''
    Delete index placis in ES
    '''

    print('Delete index placis')
    r = requests.delete("http://localhost:9200/placis?pretty")
    print(r.text)

def get_es():
    '''
    List all indexes in ES
    '''

    r = requests.get('http://localhost:9200/_cat/indices?v')
    print(r.text)