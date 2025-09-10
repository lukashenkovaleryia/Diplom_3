from faker import Faker

fake = Faker(locale="ru_RU")  #  генератор по России

def generated_email():
    return fake.email()

def generated_password(length=10):
    return fake.password(length=length, special_chars=False)

def generated_login():
    return fake.name()

def generate_user_data():
    return {
        'email': generated_email(),
        'password': generated_password(),
        'name': generated_login()
    }
