import unittest
from unittest.mock import MagicMock
from datetime import date

from sqlalchemy.orm import Session

from src.database.models import Contact, User
from src.schemas import ContactBase, ContactUpdate

from src.repository.contacts import (
    get_birthdays_in_next_week,
    get_contacts,
    get_contact,
    create_contact,
    update_contact,
    remove_contact,
    search_contacts,
)


class TestContacts(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.user = User(id=1)

    # async def test_get_birthdays_in_next_week(self):
    #     contacts = [Contact(birthday=date.today())]
    #     self.session.query().filter().all.return_value = contacts
    #     result = await get_birthdays_in_next_week(db=self.session)
    #     self.assertEqual(result, contacts)

    async def test_get_contacts(self):
        contacts = [Contact(), Contact(), Contact()]
        self.session.query().filter_by().offset().limit().all.return_value = contacts
        result = await get_contacts(skip=0, limit=10, user=self.user, db=self.session)
        self.assertEqual(result, contacts)

    async def test_get_contact_found(self):
        contact = Contact()
        self.session.query().filter().first.return_value = contact
        result = await get_contact(id=1, user=self.user, db=self.session)
        self.assertEqual(result, contact)

    async def test_get_contact_not_found(self):
        self.session.query().filter().first.return_value = None
        result = await get_contact(id=1, user=self.user, db=self.session)
        self.assertIsNone(result)

    async def test_create_contact(self):
        body = ContactBase(
            first_name="Test",
            last_name="Contact",
            birthday=date(2000, 1, 1),
            comments="Test comments",
            email="test@example.com",
            phone_number="1234567890",
        )
        result = await create_contact(body=body, user=self.user, db=self.session)
        self.assertEqual(result.first_name, body.first_name)
        self.assertEqual(result.last_name, body.last_name)
        self.assertEqual(result.birthday, body.birthday)
        self.assertEqual(result.comments, body.comments)
        self.assertEqual(result.email, body.email)
        self.assertEqual(result.phone_number, body.phone_number)
        self.assertTrue(hasattr(result, "id"))

    async def test_update_contact_found(self):
        body = ContactUpdate(
            first_name="Test2",
            last_name="Contact2",
            birthday=date(2000, 1, 1),
            comments="Test comments",
            email="test@example.com",
            phone_number="1234567890",
            )
        contact = Contact(id=1, user_id=1)
        self.session.query().filter().first.return_value = contact
        result = await update_contact(id=1, body=body, user=self.user, db=self.session)
        self.assertEqual(result, contact)

    async def test_update_contact_not_found(self):
        body = ContactUpdate(
            first_name="Test2",
            last_name="Contact2",
            birthday=date(2000, 1, 1),
            comments="Test comments",
            email="test@example.com",
            phone_number="1234567890",
            )
        self.session.query().filter().first.return_value = None
        result = await update_contact(id=1, body=body, user=self.user, db=self.session)
        self.assertIsNone(result)

    async def test_remove_contact_found(self):
        contact = Contact()
        self.session.query().filter().first.return_value = contact
        result = await remove_contact(id=1, user=self.user, db=self.session)
        self.assertEqual(result, contact)

    async def test_remove_contact_not_found(self):
        self.session.query().filter().first.return_value = None
        result = await remove_contact(id=1, user=self.user, db=self.session)
        self.assertIsNone(result)

    async def test_search_contacts(self):
        contacts = [Contact(first_name="Test")]
        self.session.query().filter().all.return_value = contacts
        result = await search_contacts(query="Test", user=self.user, db=self.session)
        self.assertEqual(result, contacts)

    async def test_search_contacts_no_results(self):
        self.session.query().filter().all.return_value = []
        result = await search_contacts(query="NonExistent", user=self.user, db=self.session)
        self.assertEqual(result, [])