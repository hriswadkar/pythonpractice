# Match case is similar to switch case available in other languages


def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
        
# Usage

print(http_status(200))     # Output: OK
print(http_status(404))     # Output: Not Found
print(http_status(500))     # Output: Internal Server Error
print(http_status(403))     # Output: Unknown Status