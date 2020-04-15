from collections import abc


class TeamsWebhookException(Exception):
    """custom exception for failed webhook call"""

    pass


KEY_TITLE = "title"
KEY_TEXT = "text"
KEY_SUMMARY = "summary"
KEY_SECTIONS = "sections"
KEY_FACTS = "facts"


class TeamData:
    """Base class for TeamData"""

    def __init__(self):
        self.data = {}

    def card_data(self):
        new_data = {}
        for key, value in self.data.items():
            if isinstance(value, TeamData):
                new_data[key] = value.card_data()
            elif isinstance(value, abc.Sequence) and not isinstance(value, str):
                new_data[key] = []
                for itm in value:
                    if isinstance(itm, TeamData):
                        new_data[key].append(itm.card_data())
                    else:
                        new_data[key].append(itm)
            else:
                new_data[key] = value

        return new_data


class _CardProperty:
    """Property descriptor for the card properties."""

    def __init__(self, name):
        self._name = name

    def __get__(self, obj, objtype):
        return obj.data.get(self._name, None)

    def __set__(self, obj, val):
        obj.data[self._name] = val


class Section(TeamData):
    """A card section"""

    title = _CardProperty(KEY_TITLE)
    text = _CardProperty(KEY_TEXT)

    def add_fact(self, name, value):
        """Add a fact to this section."""
        try:
            facts = self.data[KEY_FACTS]
        except:
            facts = []
            self.data[KEY_FACTS] = facts
        facts.append({"name": name, "value": value})


class Card(TeamData):
    """A Card."""
    title = _CardProperty(KEY_TITLE)
    text = _CardProperty(KEY_TEXT)
    summary = _CardProperty(KEY_SUMMARY)

    def __init__(self):
        super().__init__()
        self.data["@type"] = "MessageCard"
        self.data["@context"] = "https://schema.org/extensions"

    def add_section(self, section: Section):
        try:
            sections = self.data[KEY_SECTIONS]
        except KeyError:
            sections = []
            self.data[KEY_SECTIONS] = sections
        sections.append(section)
