import pytest

from dundie.core import read
from dundie.database import add_person, commit, connect


@pytest.mark.unit
def test_read_with_query():
    db = connect()

    pk = "joe@mail.com"
    data = {"name": "Any Name", "dept": "Sales", "role": "Any role"}
    _, created = add_person(db, pk, data)
    assert created is True
    commit(db)

    pk = "jim@mail.com"
    data = {"name": "Jim Doe", "dept": "Management", "role": "Manager"}
    _, created = add_person(db, pk, data)
    assert created is True
    commit(db)

    response = read()
    assert len(response) == 2

    response = read(dept="Management")
    assert len(response) == 1
    response[0]["name"] == "Jim doe"
