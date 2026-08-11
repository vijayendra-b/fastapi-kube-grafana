from fastapi import FastAPI
from app.routes.products import router as p
from app.routes.orders import router as o
from prometheus_client import generate_latest,CONTENT_TYPE_LATEST
from fastapi.responses import Response
app=FastAPI(title="Inventory API")
@app.get("/health")
def health(): return {"status":"healthy"}
@app.get("/metrics")
def metrics(): return Response(generate_latest(),media_type=CONTENT_TYPE_LATEST)
app.include_router(p,prefix="/products")
app.include_router(o,prefix="/orders")
