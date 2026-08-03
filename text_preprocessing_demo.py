from app.utils.text_preprocessing import clean_text

text = """
I absolutely loved this product!!
It arrived in just 2 days and works perfectly.
Visit https://example.com for more details.
"""

print("Original:\n")
print(text)

print("\nProcessed:\n")
print(clean_text(text))