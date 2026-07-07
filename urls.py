class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru"

    MAIN_PAGE = f"{BASE_URL}/"
    LOGIN_PAGE = f"{BASE_URL}/login"
    ORDERS_PAGE = f"{BASE_URL}/feed"

    CREATE_USER = f"{BASE_URL}/api/auth/register"
    LOGIN_USER = f"{BASE_URL}/api/auth/login"
    DELETE_USER = f"{BASE_URL}/api/auth/user"