from fastapi import Depends, HTTPException, status
from .permissions import Role

def get_current_role() -> Role:
    # Placeholder — depois entra JWT / OAuth2 / API Keys
    return Role.public

def require_role(required: Role):
    def checker(role: Role = Depends(get_current_role)):
        if role != required and role != Role.admin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permissão insuficiente"
            )
    return checker
