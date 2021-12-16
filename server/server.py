from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter

from gql.schema.query import Query
from sql_db.models.ingredient import Ingredient

schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(schema=schema, graphiql=True)

app = FastAPI()

@app.get("/")
async def root():
    return Ingredient.find(1)

app.include_router(graphql_app, prefix="/graphql")
