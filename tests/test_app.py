import pytest
from app.v1.items import Id, Book, Dvd
from app.v1.catalog import Catalog
from app.v1.member import Member
def setup_sample():
cat = Catalog()
cat.add(Book(Id("B1"), "Rust for Humans"))
cat.add(Book(Id("B2"), "Pythonic Patterns"))
cat.add(Dvd(Id("D1"), "Taking Flight"))
return cat
def test_add_and_get():
cat = setup_sample()
assert cat.get("B1").title == "Rust for Humans"
assert cat.get("D1").days_allowed() == 7
