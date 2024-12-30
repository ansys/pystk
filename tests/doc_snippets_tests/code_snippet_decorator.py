def code_snippet(name: str, description: str, category: str, eid: str):
    def decorator(func):
        func.name = name
        func.description = description
        func.category = category
        func.eid = eid
        return func

    return decorator
