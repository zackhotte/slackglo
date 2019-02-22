import os
import sys

import pytest

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../')

from slackgo import create_app


@pytest.fixture
def client():
    app = create_app({
        'TESTING': True
    })

    yield app.test_client()
