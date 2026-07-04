import requests
BASE_URL = "https://random-d.uk/api/random"
def fetch_duck():

    ducks = []

    try:

        for _ in range(10):      

            response = requests.get(BASE_URL, timeout=10)

            if response.status_code != 200:
                continue

            data = response.json()

            ducks.append({
                "image": data.get("url", ""),
                "message": data.get("message", "Random Duck")
            })

        return {
            "success": True,
            "ducks": ducks
        }

    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": str(e)
        }


if __name__ == "__main__":
    result = fetch_duck()
    print(result)