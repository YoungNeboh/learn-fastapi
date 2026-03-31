# app/db/base.py

# 1. Import the specific Base classes/Metadatas
from sqlmodel import SQLModel
from app.models.tenant.base import MultiTenantBase

# 2. Group Public Models (Schema: public)
from app.models.public.organization import Organization
# any other shared/global models

# 3. Group Tenant Models (Schema: tenant_specific)
from app.models.tenant.user import User
from app.models.tenant.shopping import CartItems
from app.models.tenant.shopping import Products
