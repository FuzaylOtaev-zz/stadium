import flask_migrate
import pytest

from app import create_app, db, Stadium, StadiumGroup, User
from app.repositories.stadium_repo import get_stadium_full_data


@pytest.fixture()
def app():
    return create_app("testing")


@pytest.fixture(autouse=True)
def run_before_and_after(app):
    _run_before(app)
    yield
    _run_after(app)


def _run_before(app):
    with app.app_context():
        flask_migrate.upgrade()


def _run_after(app):
    with app.app_context():
        db.drop_all()
        db.engine.execute("drop table alembic_version")


# @pytest.fixture()
# def client(app):
#     with app.test_client() as client:
#         yield client


def test_get_stadium(app):
    def build():
        user = add_user()
        group = add_stadium_group(user.id)
        stadium = add_stadium(group.id)

        return stadium

    def add_user():
        user = User(**user_attributes())
        db.session.add(user)
        db.session.commit()

        return user

    def user_attributes():
        return dict(
            first_name="George", last_name="Washington", email="george@gmail.com"
        )

    def add_stadium_group(owner_id: int):
        group = StadiumGroup(name="Group1", owner_id=owner_id)
        db.session.add(group)
        db.session.commit()

        return group

    def add_stadium(group_id: int):
        stadium = Stadium(**stadium_attributes(group_id))
        db.session.add(stadium)
        db.session.commit()

        return stadium

    def stadium_attributes(group_id: int):
        return dict(
            name="Stadium1", status="active", stadium_group_id=group_id, is_deleted=False
        )

    def get_stadium_details(stadium_id: int):
        with app.test_client() as client:
            result = client.get(f"/stadium/{stadium_id}")
            return result

    def assert_stadium_details(details):
        pass

    def test():
        stadium = build()
        stadium_details = get_stadium_details(stadium.id)
        assert_stadium_details(stadium_details)

    with app.app_context():
        test()


