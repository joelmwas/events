import datetime
from flask import url_for
from events import db


class Event(db.Document):
    title = db.StringField(max_length=255, required=True)
    description = db.StringField(required=True)
    slug = db.StringField(max_length=255, required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)

    def get_absolute_url(self):
        return url_for('event', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }


class Comment(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(verbose_name="Comment", required=True)
    author = db.StringField(verbose_name="Name", max_length=255, required=True)