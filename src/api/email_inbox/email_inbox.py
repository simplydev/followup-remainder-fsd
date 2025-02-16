import uuid
from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select
from app.models.email_inbox import Email, MsgInference, CustomColumnsDataMeta, CustomColumnsData
from api_objects.email_objects import EmailItems


from app.api.deps import CurrentUser, SessionDep


router = APIRouter(prefix="/email/inbox", tags=["email_inbox"])

@router.get("/", response_model=EmailItems)
def read_items(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve items.
    """

    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(Email)
        count = session.exec(count_statement).one()
        statement = select(Email).offset(skip).limit(limit)
        items = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(Email)
            .where(Email.user_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(Email)
            .where(Email.user_id == current_user.id)
            .offset(skip)
            .limit(limit)
        )
        items = session.exec(statement).all()

    return EmailItems(data=items, count=count)

@router.get("/{id}", response_model=EmailItems)  # response_model=ItemPublic
def read_item(session: SessionDep, current_user: CurrentUser, id: uuid.UUID) -> Any:
    """
    Get item by ID.
    """
    item1 = session.get(Email, id)
    item = EmailItems(data=[Email()], count=1)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not current_user.is_superuser and (item.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return item 