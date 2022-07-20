from faker import Faker

fake = Faker()


def generate_data():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "phone_number": fake.phone_number(),
        "job": fake.job()
    }
