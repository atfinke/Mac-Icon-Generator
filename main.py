import argparse
from pathlib import Path
from PIL import Image
import sys

# Constants
ICON_SIZES = {
    "16x16": [(16, 16), (32, 32)],
    "32x32": [(32, 32), (64, 64)],
    "128x128": [(128, 128), (256, 256)],
    "256x256": [(256, 256), (512, 512)],
    "512x512": [(512, 512), (1024, 1024)],
}
DEFAULT_SOURCE_IMAGE = "icon.png"
OUTPUT_DIR_NAME = "mac_icons"
EXPECTED_SIZE = (1024, 1024)


def generate_icons(source_path: Path, output_dir: Path, expected_size: tuple):
    """
    Generates resized icons from the source image and saves them to the output directory.

    :param source_path: Path to the source image.
    :param output_dir: Directory where resized icons will be saved.
    :param expected_size: Expected size of the source image (width, height).
    """
    # Check if the source image exists
    if not source_path.is_file():
        raise FileNotFoundError(f"Source image not found: {source_path}")

    # Create the output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output directory is set to: {output_dir.resolve()}")

    # Open the source image
    with Image.open(source_path) as img:
        # Verify the size of the source image
        if img.size != expected_size:
            raise ValueError(
                f"Source image size mismatch: expected {expected_size}, got {img.size}"
            )
        print(f"Opened source image: {source_path.name} with size {img.size}")

        # Generate and save each icon size
        for base_size, sizes in ICON_SIZES.items():
            for size in sizes:
                resized_img = img.resize(size, Image.Resampling.LANCZOS)
                icon_name = f"icon_{base_size}_{size[0]}x{size[1]}.png"
                icon_path = output_dir / icon_name
                resized_img.save(icon_path)
                print(f"Saved {icon_path.name}")

    print("All icons have been generated successfully.")


def parse_arguments():
    """
    Parses command-line arguments.

    :return: Namespace with the source image path.
    """
    parser = argparse.ArgumentParser(
        description="Generate macOS icon sizes from a source image."
    )
    parser.add_argument(
        "source_image",
        nargs="?",
        default=DEFAULT_SOURCE_IMAGE,
        type=Path,
        help=f"Path to the source image (default: {DEFAULT_SOURCE_IMAGE})",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    source_image_path = args.source_image
    output_dir = Path(OUTPUT_DIR_NAME)

    try:
        generate_icons(source_image_path, output_dir, EXPECTED_SIZE)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()