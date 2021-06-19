from app import app


# Modelos
from app.menu import menuModel
## Relaciones
### Debe respetarse la jerarquia de los modelos
### Ejm: El modelo usuario, se relaciona con Rol (UserModel -> rol_id <- RolesModel)
from app.roles import rolesModel
from app.user import userModel
from app.categories import categoriesModel
from app.warehouse import warehouseModel
from app.clients import clientModel
from app.products import productModel
from app.stores import storeModel
from app.inventories import inventoryModel
from app.sales import saleModel


## Rutas
from app.menu import menuRouter
from app.auth import authRouter
from app.home import homeRouter
from app.categories import categoriesRouter
from app.warehouse import warehouseRouter
from app.clients import clientRouter
from app.products import productRouter
from app.stores import storeRouter
from app.inventories import  inventoryRouter
from app.sales import saleRouter