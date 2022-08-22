import pytest

from dundie.database import EMPTY_DB, add_person, commit, connect


@pytest.mark.unit
def test_database_schema():
    db = connect()
    assert db.keys() == EMPTY_DB.keys()


@pytest.mark.unit
def test_commit_to_database():
    db = connect()
    data = {"name": "Joe Doe", "role": "Salesman", "dept": "Sales"}
    db["people"]["joe@doe.com"] = data
    commit(db)
    db = connect()
    assert db["people"]["joe@doe.com"] == data


@pytest.mark.unit
@pytest.mark.high
def test_add_person_for_the_first_time():
    db = connect()
    pk = "joe@mail.com"
    data = {"name": "Any Name", "dept": "Any Dep", "role": "Any role"}

    _, created = add_person(db, pk, data)

    assert created is True

    commit(db)

    assert db["people"][pk] == data
    assert len(db["movement"][pk]) > 0


@pytest.mark.unit
def test_negative_add_person_invalid_email():
    with pytest.raises(ValueError):
        add_person({}, ".@bla", {})
