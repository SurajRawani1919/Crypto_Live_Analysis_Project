from scripts.update_excel import update_excel
from scripts.analyze_crypto import analyze_crypto_data

if __name__ == "__main__":
    print("🚀 Fetching & Analyzing Live Crypto Data...")

    # Run analysis
    analyze_crypto_data()

    # Update Excel initially
    update_excel()

    print("\n✅ Process completed! Excel is live-updating every 5 minutes.")
