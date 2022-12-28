from typing import List, Optional
from fastapi import APIRouter, Depends, Response, status

from ..tables import User
from ..models.operations import Operation, OperationKind, OperationCreate, OperationUpdate
from ..services.operations import OperationsService
from ..services.auth import get_current_user

router = APIRouter(
    prefix='/operations',
)

@router.get('/', response_model=List[Operation])
def get_operations(
    kind: Optional[OperationKind] = None,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends(),
):
    return service.get_list(kind=kind)

@router.post('/', response_model=Operation)
def create_operation(
    operation_data: OperationCreate,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends(),
):
    return service.create(operation_data)

@router.get('/{operation_id}', response_model=Operation)
def get_operation(
    operation_id: int,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends(),
):
    return service.get(operation_id)

@router.put('/{operation_id}', response_model=Operation)
def update_operation(
    operation_id: int,
    operation_data: OperationUpdate,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends(),
):
    return service.update(
        operation_id,
        operation_data,
    )

@router.delete('/{operation_id}')
def delete_operation(
    operation_id: int,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends(),
):
    service.delete(operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


