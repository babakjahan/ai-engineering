from helper import get_response


product_description = """
The Smartphone XYZ-5000 is a device packed with innovative features to enhance the user experience. Its sleek design and vibrant display make it visually appealing, while the powerful octa-core processor ensures smooth performance and multitasking capabilities.
The XYZ-5000 boasts a high-resolution triple-camera system, combining a 48MP primary lens, a 12MP ultra-wide lens, and a 5MP depth sensor, enabling users to capture stunning photos and videos in various shooting scenarios. The device also supports 4K video recording and comes with advanced image stabilization features.
With a generous 128GB of internal storage, expandable up to 512GB via microSD, users can store a vast collection of media files and apps without worrying about running out of space. The smartphone runs on the latest Android OS and offers seamless integration with various Google services.
In terms of security, the XYZ-5000 features a reliable fingerprint sensor and facial recognition technology for quick and secure unlocking. Additionally, it supports NFC for contactless payments and has a dedicated AI-powered virtual assistant to simplify daily tasks.
The device's long-lasting 4000mAh battery ensures all-day usage, and it supports fast charging, providing hours of power with just a few minutes of charging. The XYZ-5000 is also water and dust resistant, giving users peace of mind in various environments.
Overall, the Smartphone XYZ-5000 offers a fantastic combination of style, performance, and advanced features, making it an excellent choice for tech enthusiasts and everyday users alike.

"""


# Craft a prompt to summarize the product description
prompt = f"""
summarizes the product_description in no more than five bullet points.
``` {product_description} ```
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Summarized description: \n", response)