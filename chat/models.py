import uuid
from datetime import datetime

from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class CassandraMessage(DjangoCassandraModel):
    id = columns.UUID(default=uuid.uuid4)
    room = columns.Text(required=True, primary_key=True)
    date_added = columns.DateTime(required=True, primary_key=True, default=datetime.now)
    username = columns.Text(required=True)
    content = columns.Text(required=True)

    class Meta:
        get_pk_field = 'date_added'
