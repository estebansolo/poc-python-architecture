from source.shared.adapters.api.server import app, server
from source.pago_co.adapters.api.routes import router as pago_co_router


app.title = 'Credit Evaluation Services'
app.description = 'Service for credit risk and profitability evaluation, and home of the loan proposal engine'

# Routers
app.include_router(pago_co_router)


def main():
    server()
