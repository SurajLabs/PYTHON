# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)") 

# Output: List is too long (5 elements, expected <= 3)
# := iska matlab hai "assignment expression" yaani ki aap ek variable ko assign karte hue uska value check kar sakte ho. Is case mein, n ko assign kiya gaya hai len([1, 2, 3, 4, 5]) ka value aur phir usko check kiya gaya hai agar wo 3 se bada hai ya nahi.