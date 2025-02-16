from sqlmodel import Field, SQLModel
  
class User(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    username: str
    email: str
    password: str
    is_active: bool = True
    org_id: int
    idp_access_token: str
    idp_refresh_token: str
