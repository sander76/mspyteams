import logging
import pytest
from mspyteams.card import Card, KEY_TITLE, Section, KEY_SECTIONS

_LOGGER = logging.getLogger(__name__)


@pytest.fixture
def card():
    return Card()


def test_basic_card(card):
    _title = "a title"
    _text = "this is text"
    _summary = "this is a summary"
    expected = {
        "@type": "MessageCard",
        "@context": "https://schema.org/extensions",
        "title": _title,
        "summary": _summary,
        "text": _text,
    }
    card.title = _title
    card.text = _text
    card.summary = _summary

    data = card.card_data()

    assert data == expected


def test_add_section(card):
    _title = "a title"
    expected = {
        "@type": "MessageCard",
        "@context": "https://schema.org/extensions",
        "sections": [{"title": _title}],
    }

    section = Section()
    section.title = _title

    card.add_section(section)

    data = card.card_data()

    assert data == expected


def test_section():
    _fact = ("fact1", 1)
    _title = "a title"

    expected = {"title": _title, "facts": [{"name": _fact[0], "value": _fact[1]}]}

    section = Section()
    section.title = _title
    section.add_fact(*_fact)

    data = section.card_data()
    assert data == expected
