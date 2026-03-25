def div(x:int, y:int):
    try:
        return x / y
    except Exception as e:
        return f"Somthing wrong in division.py: {e}"