from app.db.base_class import Base
from app.models.record import Record

print("Modelos importados com sucesso!")
print(Base)
print(Record)

base = Base()
print("Base instanciada:", base)
