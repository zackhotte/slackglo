import json


def test_slack_challenge(client):
    payload = {'token': 'Jhj5dZrVaK7ZwHHjRyZWjbDl', 'challenge': '3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P',
               'type': 'url_verification'}
    rv = client.post('/api/v1/slack/challenge', data=json.dumps(payload), content_type='application/json')
    data = json.loads(rv.data.decode('utf-8'))

    assert 200 == rv.status_code
    assert '3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P' == data['challenge']
    assert 'application/json' == rv.headers.get('Content-Type')
