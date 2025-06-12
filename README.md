# Pi Full Screen Slideshow

A Python script for displaying a full-screen slideshow of images on both macOS and Raspberry Pi systems.

## Prerequisites

### macOS
- Python 3.x
- PyQt5 (`pip install PyQt5`)

### Raspberry Pi
- Python 3.x
- Raspbian/Raspberry Pi OS
- PyQt5 (`sudo apt-get install python3-pyqt5`)

## Installation

1. Clone this repository or download the script
2. Install the required dependencies for your system (see Prerequisites)

## Usage

1. Place your images in a directory
2. Run the script:

```bash
python3 pi_slideshow.py [path_to_image_directory] [interval_seconds]
```

Parameters:
- `path_to_image_directory`: Directory containing your images (default: current directory)
- `interval_seconds`: Time between slides in seconds (default: 10)

## Features

- Full-screen display
- Automatic image scaling to fit screen
- Supports common image formats (JPG, PNG, GIF)
- Cross-platform compatibility (macOS and Raspberry Pi)
- Configurable slide intervals

## Controls

- ESC: Exit slideshow
- Space: Pause/Resume
- Right Arrow: Next image
- Left Arrow: Previous image

## Auto-start on Raspberry Pi

To make the slideshow start automatically on your Raspberry Pi:

1. Create an autostart entry:
```bash
mkdir -p ~/.config/autostart
cat > ~/.config/autostart/slideshow.desktop << EOL
[Desktop Entry]
Type=Application
Name=Slideshow
Exec=python3 /path/to/pi_slideshow.py /path/to/images 10
X-GNOME-Autostart-enabled=true
EOL
```

2. Make sure the script is executable:
```bash
chmod +x /path/to/pi_slideshow.py
```

## Notes

- For best performance on Raspberry Pi, optimize your images to match your display resolution
- The script automatically handles different screen orientations
- Supports both windowed and full-screen modes (default: full-screen)

