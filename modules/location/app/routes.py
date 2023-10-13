def register_routes(api, app, root="api"):
    from app.location_service import register_routes 

    # Add routes
    register_routes(api, app)
