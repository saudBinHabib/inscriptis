#!/usr/bin/env python3

from inscriptis.html_properties import Table

def test_table():
    t = Table()

    t.add_row()
    t.add_column()
    t.add_text("first")
    t.add_column()
    t.add_text("second")
    t.add_column()
    t.add_text("third")

    t.add_row()
    t.add_column()
    t.add_text("a")
    t.add_column()
    t.add_text("b")
    t.add_column()
    t.add_text("c")

    text = str(t)
    print(text)
    assert text == 'first\tsecond\tthird\na\tb\tc'