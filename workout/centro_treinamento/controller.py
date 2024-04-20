from http.client import HTTPException
from uuid import uuid4
from fastapi import APIRouter, Body,status
from pydantic import UUID4
from workout.centro_treinamento.models import CentroTreinamentoModel
from workout.centro_treinamento.schemas import CentroTreinamentoIn,CentroTreinamentoOut
from workout.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

router=APIRouter()

@router.post(
    '/',
    summary='Criar novo Centro de Treinamento',status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def post(
    db_session:DatabaseDependency,centro_treinamento_in:CentroTreinamentoIn = Body(...)
    ) -> CentroTreinamentoOut:

    centro_treinamento_out=CentroTreinamentoOut(id=uuid4(),**centro_treinamento_in.model_dump())
    centro_treinamento_model=CentroTreinamentoModel(**centro_treinamento_out.model_dump())

    db_session.add(centro_treinamento_model)
    await db_session.commit()

    return centro_treinamento_out

@router.get(
    '/',
    summary='Listar todos centros de treinamento',status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut]
)
async def query(db_session:DatabaseDependency) -> list[CentroTreinamentoOut]:
    centros:list[CentroTreinamentoOut] = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()

    return centros

@router.get(
    '/{id}',
    summary='Listar um centro de treinamento pelo id',
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut
)
async def query_one(id:UUID4,db_session:DatabaseDependency) -> CentroTreinamentoOut:
    centros:CentroTreinamentoOut = (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))).scalars().first()

    if not centros:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Centro de Treinamento não encontrado no id:{id}')

    return centros