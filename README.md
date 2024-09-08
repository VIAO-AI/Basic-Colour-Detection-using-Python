# Basic Colour Detection Using Python By VIAO.AI
This project, developed by VIAO.AI, is a friendly and practical introduction to computer vision, designed for beginners and technology enthusiasts. Through a simple example of basic colour detection (red, green and blue), we will show you how to teach a computer to ‘see’ the world around us.

# Colour Detection with VIAO.AI: Teaching the Computer to See Like You Do!

Hello, computer vision explorer! Have you ever wondered how computers can ‘see’ the world around us? This project will show you a little magic trick! 

We are going to teach a computer to detect colours, as if it were a small child learning to recognise the colours of its favourite toys. 

**How does the magic work?**

Imagine that the computer is a curious child who wants to understand the world around him. 

1. **We define the colours (Configuration):** In `color_detection/config.py`, we define the colours we want the computer to learn to recognise. It is like giving the child a set of crayons with the colours we want it to learn: red, green and blue.

2. **We convert the image to a language the computer understands:** The computer doesn't see colours like we do, so first we convert the image to a language it understands, called HSV. It's as if we tell the child that colours have different shades and brightness!

3.  **We create a magic mask:** For each colour, we create a kind of filter that only lets light of that colour through. The computer uses this filter to look for areas of the image that match the colour. It's as if we gave the child a pair of special glasses that only let them see red, then glasses to see only green, and finally glasses for blue.

4. **The computer looks for the edges** Of the areas that match the colours, it is as if the child is drawing around the red, green and blue parts of the picture with a magic pencil.

5. **We draw the outlines!** Finally, the computer draws the edges it has found in the original image - it's as if the child has finished his magic drawing, showing the parts of the image that correspond to each colour!

   **How to use this project?**

    1. **Prepare your tools:** Make sure you have the tools installed so that the computer can ‘see’:
  
  In your bash/powershell or other terminal, you will install:
  pip install opencv-python numpy 

 2. **Choose what you want to do:**

**Process an image:** Enter the path to the image when prompted.

**Use webcam:** Select the ‘c’ option to view real-time colour detection.

3. **Run the script!**
   python main.py


**Explore and experiment!**

You can modify the colour ranges in colour_detection/config.py to experiment with other colours, or even add new colours to the list - you can also change the image or use the camera to see the colour detection in real time!

**What have we learned?**

**We've seen a bit of computer vision magic, such as:
HSV colour space:** A special way of seeing colours that the computer understands.

**Masks:** Magic filters that help find specific colours.
Contour detection: A way to find the edges of objects in an image.

**Thank you for learning with VIAO.AI! We hope this project has inspired you to explore more of the world of computer vision.**
