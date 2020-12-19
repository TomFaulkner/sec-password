from sec_password import hash_password, verify_password


def test_all():
    hashed = hash_password(
       password='secure password',
       key='string from keyfile',
       iterations=500
    )
    result = verify_password(
       stored_password=hashed,
       provided_password='secure password',
       key='string from keyfile',
       iterations=500
    )
    assert result

