from app.core.security import get_password_hash, verify_password, create_access_token
from jose import jwt
from app.core.config import settings

def test_password_hashing():
    password = "senhaSegura123"
    hashed_password = get_password_hash(password)
    assert password != hashed_password
    assert verify_password(password, hashed_password) == True
    assert verify_password("senhaIncorreta", hashed_password) == False

def test_create_access_token():
    email = "test@example.com"
    token = create_access_token(data={"sub": email})
    decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    assert decoded_payload["sub"] == email