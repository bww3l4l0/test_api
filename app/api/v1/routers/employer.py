from fastapi.routing import APIRouter



router = APIRouter(prefix='/v1/employers', tags=['Работа с сотрудниками', 'v1'])



@router.post(
    '/test',
    # response_model=SomeModelQwerty,
)
def test_def():
    return 'Working!'