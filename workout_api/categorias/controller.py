from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.categorias.models import CategoriaModel

from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

router = APIRouter()

@router.post(
    '/', 
    summary='Criar uma nova Categoria',
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def post(
    db_session: DatabaseDependency, 
    categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:
    
    categoria_nome = categoria_in.nome

    # Verifica categoria
    categoria = (await db_session.execute(
        select(CategoriaModel).filter_by(nome=categoria_nome))
    ).scalars().first()
    
    if categoria:
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail=f'A categoria {categoria_nome} ja foi cadastrada.'
        )

    try:
        # código id gerado automaticamente por biblioteca uuid4 (strings de 36 caracteres alfanuméricos aleatórios)
        categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
        categoria_model = CategoriaModel(**categoria_out.model_dump())
        
        db_session.add(categoria_model)
        await db_session.commit()   

    except Exception as erro:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail= f'Já existe uma categoria cadastrada com o nome: {categoria_model.nome}. {erro.__class__}'
        )

    return categoria_out
    
    
@router.get(
    '/', 
    summary='Consultar todas as Categorias',
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut],
)
async def query(db_session: DatabaseDependency) -> list[CategoriaOut]:

    # Consulta de todas as categorias no banco de dados
    categorias_query = select(CategoriaModel)
    # Executa a consulta no banco de dados
    categorias: list[CategoriaOut] = (await db_session.execute(categorias_query)).scalars().all()
    
    return categorias


@router.get(
    '/{id}', 
    summary='Consulta uma Categoria pelo id UUID4',
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
)
async def get(id: UUID4, db_session: DatabaseDependency) -> CategoriaOut:
    

    categoria: CategoriaOut = (
        await db_session.execute(select(CategoriaModel).filter_by(id=id))
    ).scalars().first()
    print(id)

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Categoria não encontrada no id: {id}'
        )
    
    return categoria