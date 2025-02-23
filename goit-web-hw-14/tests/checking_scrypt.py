# check_import.py
try:
    from src.database.models import User
    print("Module 'src.database.models' is accessible.")
except ModuleNotFoundError:
    print("Module 'src.database.models' is NOT accessible.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")