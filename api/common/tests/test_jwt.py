from common.auth.jwt import jwt_authenticate, build_jwt_token

def test_jwt_is_built_correctly():
    expected = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJleHAiOiIxMjMifQ.T9KfYZlOvVEZi-atonxZCwavc8fm0CjFC64pG_WP1EE'
    output = build_jwt_token("test", "123")
    assert expected == output
