"""Story Item

Example:
{
    "by": "dhouston",
    "id": 8863,
    "kids": [8952, 9224, 8917],
    "score": 111,
    "time": 1175714200,
    "title": "My YC app: Dropbox - Throw away your USB drive",
    "type": "story",
    "url": "http://www.getdropbox.com/u/2/screencast.html"
}

Author: Rylan Santinon
"""

from ..schemas.storyschema import StorySchema
from .hnitem import HnItem

class StoryItem(HnItem):
    """Story Item"""

    def __init__(self, json):
        self.json = json

    def get_schema(self):
        return StorySchema()

    def is_deleted(self):
        return not not self.json.get('deleted')

    def get(self, name):
        return self.get_field_by_name(name)

    #pylint: disable=line-too-long
    def get_field_by_name(self, name):
        """Get field by name

        >>> StoryItem({'id':1234}).get_field_by_name('id')
        1234

        >>> StoryItem({'id':1234}).get_field_by_name('foobar') # doctest: +ELLIPSIS
        Traceback (most recent call last):
        RuntimeError: No field named 'foobar' in ...
        """
        schema = self.get_schema()
        if schema.has_field(name):
            return self.json[name]
        else:
            raise RuntimeError("No field named %r in %r" \
                    % (name, schema))

    def __repr__(self):
        return "StoryItem(json=%r, schema=%r)" \
                % (self.json, self.get_schema())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
