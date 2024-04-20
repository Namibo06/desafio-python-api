from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from workout.configs.database import get_session

# primeiro parametro tipagem,e o segundo retorno
DatabaseDependency=Annotated[AsyncSession,Depends(get_session)]