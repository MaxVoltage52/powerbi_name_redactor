from PIL import Image, ImageDraw
import os

def clean_dashboard():
    input_file = 'dashboard.png'
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found!")
        print("Please save your screenshot as 'dashboard.png' in this folder first.")
        input("\nPress Enter to close...")
        return
    
    # Open the image
    img = Image.open(input_file)
    draw = ImageDraw.Draw(img)
    
    # TODO: UPDATE THESE COORDINATES after your first test
    # Format: [left, top, right, bottom]
    # These are placeholder values - you'll adjust them based on your dashboard
    name_column_coords = [100, 200, 300, 800]
    
    # Draw white rectangle over name column
    draw.rectangle(name_column_coords, fill='white')
    
    # Save cleaned version
    output_file = 'dashboard_clean.png'
    img.save(output_file)
    
    print(f"✓ Cleaned image saved as: {output_file}")
    print(f"  Original size: {img.size[0]}x{img.size[1]} pixels")
    print(f"  Redacted area: {name_column_coords}")
    print("\nIf the redaction doesn't cover the names correctly,")
    print("open dashboard.png in Paint to find the correct coordinates.")
    
    input("\nPress Enter to close...")

if __name__ == "__main__":
    clean_dashboard()
