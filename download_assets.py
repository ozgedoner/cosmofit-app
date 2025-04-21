import os
import gdown

def download_all_assets():
    os.makedirs("csv", exist_ok=True)
    os.makedirs("Images", exist_ok=True)
    os.makedirs("user_images", exist_ok=True)

    # CSV indir
    gdown.download(
        "https://drive.google.com/uc?id=1yIN7WrDeVuM5KzNpVpAB7KVX6Tx0KImH", 
        "csv/extended_merged_obesity_coordinates.csv", 
        quiet=False
    )

    # Görseller indir
    gdown.download("https://drive.google.com/uc?id=1NwPmABhT4bHVZ5i9LoYBdvP9xhwW0UGR", "Images/banner.jpg", quiet=False)
    gdown.download("https://drive.google.com/uc?id=1kSuDqFuVrGvj5I0yIj8A7JH_wZglGVNc", "Images/tabak.png", quiet=False)
    gdown.download("https://drive.google.com/uc?id=1dCTzU7d4Bb0hcyLlvh3a0EFqt5z9rAF_", "Images/bmi_chart.png", quiet=False)

    # Kullanıcı görselleri indir
    gdown.download("https://drive.google.com/uc?id=1ZbhYJ3XXD7ZXjQdBDeALikA35toG8h7D", "user_images/selin.png", quiet=False)
    gdown.download("https://drive.google.com/uc?id=1Ur3nvEuQoGOYk0P2O9H5EpOeGVSE-9Ht", "user_images/murat.jpg", quiet=False)
    gdown.download("https://drive.google.com/uc?id=1GhjX7pqqQFOwnvZs54kN-NzWRoa8L57O", "user_images/ece.png", quiet=False)
    gdown.download("https://drive.google.com/uc?id=1HyKEx3s9mvMcUpZxUz_X2j7ASZ3YaKv6", "user_images/kaan.jpg", quiet=False)
    gdown.download("https://drive.google.com/uc?id=1Wa6LyM17UsFml0WDFyXgk2Ul8NwP70Ut", "user_images/zeynep.jpg", quiet=False)
    gdown.download("https://drive.google.com/uc?id=1q2BVa9UtG9-UMbLmcJxDkuN5blUIlFJ9", "user_images/emre.jpg", quiet=False)
