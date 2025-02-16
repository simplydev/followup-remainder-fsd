from typing import Optional # 👈 new imports

import jwt # 👈 new imports
from fastapi import Depends, HTTPException, status # 👈 new imports
from fastapi.security import SecurityScopes, HTTPAuthorizationCredentials, HTTPBearer # 👈 new imports

#from application.config import get_settings # 👈 new imports
from src.config import settings

API_AUDIENCES = [
    "https://speedy-followup.com/api/speedy-followup",  # React SPA Audience
    "https://dev-rjil63cgo5sk5f0b.us.auth0.com/api/v2/"  # Machine-to-Machine Audience
]
ALGORITHMS = ["RS256"]

class UnauthorizedException(HTTPException):
     def __init__(self, detail: str, **kwargs):
          """Returns HTTP 403"""
          super().__init__(status.HTTP_403_FORBIDDEN, detail=detail)

class UnauthenticatedException(HTTPException):
     def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Requires authentication"
        )

# 👇 new code
class VerifyToken:
    """ Does all the token verification using PyJWT """
    def __init__(self):
        self.config = settings

        # This gets the JWKS from a given URL and does processing so you can
        # use any of the keys available
        jwks_url = f'https://{self.config.auth0_domain}/.well-known/jwks.json'
        self.jwks_client = jwt.PyJWKClient(jwks_url)
    
    async def verify(self,
                     security_scopes: SecurityScopes,
                     token: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer())
                     ):
        if token is None:
            raise UnauthenticatedException

        # This gets the 'kid' from the passed token
        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(
                token.credentials
            ).key
        except jwt.exceptions.PyJWKClientError as error:
            raise UnauthorizedException(str(error))
        except jwt.exceptions.DecodeError as error:
            raise UnauthorizedException(str(error))

        try:
            payload = jwt.decode(
                token.credentials,
                signing_key,
                algorithms=self.config.auth0_algorithms,
                audience=self.config.auth0_api_audience,
                #algorithms=ALGORITHMS,
                #audience=API_AUDIENCES,
                issuer=self.config.auth0_issuer,
            )
        except Exception as error:
            raise UnauthorizedException(str(error))
    
        return payload
