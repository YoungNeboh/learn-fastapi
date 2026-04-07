from datetime import UTC, datetime, timedelta
from typing import Any, Union, Optional
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings



# Initialize Passlib to use bcrypt for hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check if the provided password matches the stored hash."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Create a Bcrypt hash from a plain-text password."""
    return pwd_context.hash(password)

def create_access_token(subject: Union[str, Any], schema_name: str, expires_delta: Optional[timedelta] = None) -> str:
    """Create a signed JWT token containing the user ID and their tenant schema."""
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # We embed the schema_name in the token so we can verify 
    # the user's "home" schema on every request.
    to_encode = {"exp": expire, "sub": str(subject), "tenant": schema_name}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt