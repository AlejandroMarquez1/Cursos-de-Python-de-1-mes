#Exercise 5 — Dictionary search engine

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

country = input("Enter a country: ")
while country != "exit":
    print(capitals.get(country, "Country not found"))
    country = input("Enter a country: ")
