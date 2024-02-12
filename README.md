

---

# Mondrian Style Random Art Generator

This Python script generates random art in the style of Piet Mondrian, a Dutch abstract artist known for his geometric compositions using primary colors.

## Overview

The script utilizes the Tkinter library to create a window with a canvas where the random art is drawn. The art is generated by recursively splitting rectangles into smaller rectangles, filling them with random colors chosen from a predefined palette.

## Usage

To run the script, make sure you have Python installed on your system. Then, simply execute the script using the following command:

```bash
python mondrian_art.py
```

The script will open a window displaying the generated art.

## Customization

You can customize the appearance of the generated art by adjusting the following parameters in the script:

- `WIDTH` and `HEIGHT`: Set the width and height of the canvas.
- `SPLIT_LOW`: Minimum size for rectangles to be split further.
- `SPLIT_PENALTY`: Determines how likely it is for a rectangle to be split horizontally or vertically.

Additionally, you can modify the `randomColor()` function to change the color palette used for filling the rectangles.

## Dependencies

- Python 3.x
- Tkinter (usually included with Python)

## Example

![Example Mondrian-style Art](example_art.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to add more details or sections as needed!
