from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from ecommerce.user import router as user_router
from ecommerce.products import router as product_router
from ecommerce.cart import router as cart_router

app = FastAPI(docs_url="/")

app.include_router(router=user_router.router)
app.include_router(router=product_router.router)
app.include_router(router=cart_router.router)

app.add_middleware(CORSMiddleware,
                   allow_origins="*",
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   max_age="3600"
                   )


@app.options("/api/v1/server/options", tags=["Server"])
async def get_options():
    return {}


