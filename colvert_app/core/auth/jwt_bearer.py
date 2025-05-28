"""JWT Bearer authentication class for FastAPI."""

from fastapi import Request, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from colvert_app.core.config import settings

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def _decode_jwt(self, jwtoken: str) -> dict:
        try:
            decoded_token = jwt.decode(jwtoken, settings.supabase_secret, audience="authenticated", algorithms=[settings.supabase_jwt_algorithm], options={"verify_exp": True})
            print(decoded_token)
            
            # Verify required fields
            if 'user_role' not in decoded_token:
                raise HTTPException(status_code=403, detail="Missing user_role in token")
            if 'sub' not in decoded_token:
                raise HTTPException(status_code=403, detail="Missing sub in token")
                
            return decoded_token
        except HTTPException as he:
            # Re-raise HTTP exceptions
            raise he
        except Exception as e:
            print(e)
            return {}

    def verify_jwt(self, jwtoken: str) -> bool:
        is_token_valid: bool = False

        try:
            payload = self._decode_jwt(jwtoken)
        except:
            payload = None
        if payload:
            is_token_valid = True
        return is_token_valid 