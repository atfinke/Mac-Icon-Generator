# macOS Icon Generator

This script generates various macOS icon sizes from a source PNG image using Python's Pillow library.

---

### **Usage Instructions:**

1. **Install Dependencies:**
   
   Ensure you have the Pillow library installed. If not, install it using pip:

   ```bash
   pip install Pillow
   ```

2. **Prepare the Source Image:**
   
   Ensure your source image is named `icon.png` and is 1024x1024 pixels. Alternatively, you can specify a different image path when running the script.

3. **Run the Script:**
   
   Execute the script using Python:

   ```bash
   python generate_mac_icons.py [path_to_source_image]
   ```

   - Replace `[path_to_source_image]` with your desired source image path if it's not `icon.png`.

4. **Output:**
   
   The resized icons will be saved in the `mac_icons` directory with names following the format `icon_{base_size}_{width}x{height}.png`.