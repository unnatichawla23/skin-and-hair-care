def get_skin_recommendations(skin_type):
    recommendations = {
        "oily": [
            ("Facewash - Ethiglo Skin Whitening Deep Cleansing Facial Foam", "https://l1nq.com/JVGn0"),
            ("Moisturizer - Neutrogena Oil-Free Moisturizer", "https://encr.pw/skWcf"),
            ("Serum - The Ordinary Niacinamide 10% + Zinc 1%", "https://encr.pw/MjwnD"),
            ("Sunscreen - Deconstruct Lightweight Gel Sunscreen", "https://encr.pw/3s2Vx")
        ],
        "dry": [
            ("Facewash - Cetaphil Gentle Skin Cleanser", "https://l1nq.com/9gf13"),
            ("Moisturizer - CeraVe Moisturizing Cream", "https://l1nq.com/x9sOn"),
            ("Serum - Minimalist 2% Hyaluronic Acid + PGA", "https://encr.pw/nnwOU"),
            ("Sunscreen - Foxtale Glow Sunscreen SPF 50", "https://encr.pw/gLTxo")
        ],
        "combination": [
            ("Facewash - The Derma Co 1% Kojic Acid", "https://l1nq.com/fddnQ"),
            ("Moisturizer - Plum 2% Niacinamide Moisturiser", "https://encr.pw/P1roW"),
            ("Serum - Minimalist 10% Niacinamide + Zinc", "https://l1nq.com/EdIhx"),
            ("Sunscreen - Dr. Sheth's Ceramide + Vitamin C", "https://encr.pw/Vz2g2")
        ],
        "sensitive": [
            ("Facewash - Neutrogena Deep Clean Gentle Foaming Cleanser", "https://l1nq.com/yDTyt"),
            ("Moisturizer - Simple Hydrating Light Moisturiser", "https://encr.pw/et60J"),
            ("Serum - Neutrogena Hydro Boost Hyaluronic Serum", "https://encr.pw/7Pl6c"),
            ("Sunscreen - Minimalist SPF 60 PA++++", "https://encr.pw/A8LK9")
        ]
    }
    return recommendations.get(skin_type.lower(), [("No recommendations available.", "")])


def get_hair_recommendations(hair_type):
    recommendations = {
        "curly": [
            ("Shampoo - SheaMoisture Curl Enhancing Shampoo", "https://encr.pw/hmsnI"),
            ("Conditioner - Curl Up Hydrating Conditioner", "https://l1nq.com/903vO"),
            ("Serum - Arata Curl Detangler", "https://encr.pw/Ag7ZS")
        ],
        "straight": [
            ("Shampoo - Pantene Smooth & Sleek", "https://encr.pw/9xaF2"),
            ("Conditioner - L'Oréal Dream Lengths Conditioner", "https://l1nq.com/la4fy"),
            ("Serum - Tresemme Keratin Smooth", "https://encr.pw/86rsH")
        ],
        "wavy": [
            ("Shampoo - OGX Moroccan Argan Oil Shampoo", "https://encr.pw/GNJ0m"),
            ("Conditioner - BBlunt Intense Moisture", "https://encr.pw/RNADj"),
            ("Serum - Matrix Biolage SmoothProof", "https://encr.pw/YHVLt")
        ],
        "coily": [
            ("Shampoo - Curl Up Moisturising Shampoo", "https://encr.pw/ZLXvG"),
            ("Conditioner - Curlvana Curl Shine Conditioner", "https://l1nq.com/7QBkA"),
            ("Serum - GK Hair Serum", "https://l1nq.com/QEFgf")
        ]
    }
    return recommendations.get(hair_type.lower(), [("No recommendations available.", "")])


def main():
    print("✨ Welcome to the Skin & Hair Care Product Recommendation System ✨")

    skin_type = input("\nEnter your skin type (Oily/Dry/Combination/Sensitive): ").strip().lower()
    hair_type = input("Enter your hair type (Curly/Straight/Wavy/Coily): ").strip().lower()
    age = input("Enter your age: ").strip()
    gender = input("Enter your gender (Optional): ").strip()

    print("\n🧴 Recommended Skin Care Products for", skin_type.capitalize(), "Skin:")
    for product, link in get_skin_recommendations(skin_type):
        print(f" - {product}")
        if link:
            print(f"  Purchase Link: {link}")

    print("\n💇 Recommended Hair Care Products for", hair_type.capitalize(), "Hair:")
    for product, link in get_hair_recommendations(hair_type):
        print(f" - {product}")
        if link:
            print(f"   Purchase Link: {link}")

    print("\nThank you for using the Product Recommendation System! Stay glowing! ✨")


if __name__ == "__main__":
    main()
