def review_file(file_meta):
    print(f"\nUncertain file detected: {file_meta['path']}")
    print(f"Size: {file_meta['size']} bytes")

    while True:
        decision = input("Keep (k), Delete (d), Skip (s)? ").lower()
        if decision in ["k", "d", "s"]:
            return decision
