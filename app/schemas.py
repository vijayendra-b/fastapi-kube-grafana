from pydantic import BaseModel
class ProductCreate(BaseModel):
 name:str; price:float; quantity:int
class OrderCreate(BaseModel):
 product_id:int; quantity:int
