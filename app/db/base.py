from app.db.base_class import Base

# Todos os modelos devem ser importados aqui para que o
# SQLAlchemy possa criar as tabelas corretamente
from app.models.record import Record

print("Modelos importados com sucesso!")
print(Base)
print(Record)
