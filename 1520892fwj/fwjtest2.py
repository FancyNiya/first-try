import unittest
from hello import db,User

class UserTest(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test1(self):
        user = User("fwj1")
        db.session.add(user)
        db.session.commit()
        result = db.session.query(User).all()[0]
        self.assertEqual(user.username, result.username)

    def test2(self):
        user = User("fwj2")
        db.session.add(user)
        db.session.commit()
        result = db.session.query(User).all()[0]
        self.assertEqual(user.age, result.age)

    def test3(self):
        user = User("fwj3", age=45)
        db.session.add(user)
        db.session.commit()
        result = db.session.query(User).all()[0]
        self.assertEqual(user.age, result.age)
        
if __name__ == '__main__':
    unittest.main()
