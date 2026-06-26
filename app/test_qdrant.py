from app.services.qdrant_service import (
    create_collection,
    insert_document,
    search_documents
)

create_collection()

insert_document()

results = search_documents()

print(results)