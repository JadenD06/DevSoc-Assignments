# Rotating Soda Can Project

An interactive animation that creates the illusion of a soda can rotating when hovered over. This project demonstrates advanced CSS techniques including CSS variables, blend modes, masking, and smooth transitions.

## Preview

The project shows a soda can that appears to rotate when you hover over it:
- Initially, one version of the soda can is visible
- On hover, the first can fades out while a second version fades in
- The background image shifts horizontally, creating a rotating effect
- The entire product container moves upward slightly on hover

## File Structure
```
project-folder/
│
├── index.html
├── styles.css
├── 1.png (First soda can texture)
├── 2.png (Second soda can texture)
├── soda.png (Soda can mask/shape)
├── bg.jpg (Background image)
└── README.md
```
## Step-by-Step Implementation Guide

### 1. HTML Structure

Create an `index.html` file and add the following code:

```html
<!DOCTYPE html> 
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Rotating Soda Can</title>
</head>
<body>
    <div class="banner">
        <div class="product">
            <div class="soda" style="--url: url(1.png)">
            </div>
            <div class="soda" style="--url: url(2.png)">
            </div>
        </div>
    </div>
</body>
</html>
```
Explanation:

- The HTML structure is minimal and focused on the effect
- Uses a banner container to hold everything
- The product div contains two soda divs that will create the rotation effect
- CSS custom properties (variables) are used inline to set different images for each soda div
- The `--url` variable will be used in the CSS to set background images
---
### 2. Basic CSS Setup
Create a styles.css file and start with these foundational styles:

```css
body {
    background-image: url('bg.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    margin: 0;
    padding: 0;
}
```
Explanation:

- Sets a background image for the entire page
- `background-size: cover` makes the background cover the entire viewport
- Removes default margin and padding from the body
---
### 3. Banner Container Styles
Add styles for the banner container:

```css
.banner{
    margin-top: -50px;
    height: 100vh;
    overflow: hidden;
    position: relative;
}
```
Explanation:

- `margin-top: -50px` pulls the banner slightly upward
- `height: 100vh` makes the banner take the full viewport height
- `overflow: hidden` prevents any content from spilling outside the container
- `position: relative` establishes a positioning context for child elements
---
### 4. Product Container Styles
Add styles for the product container:

```css
.product{
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    bottom: 0;
    z-index: 2;
    width: 500px;
    transition: 0.7s;
}
```
Explanation:

- `position: absolute` allows precise positioning within the banner
- `left: 50%` combined with transform: translateX(-50%) centers the element horizontally
- `bottom: 0` positions it at the bottom 
- `z-index: 2` ensures it appears above other elements
- `width: 500px` sets a fixed width
- `transition: 0.7s` adds smooth animation to all property changes
---
### 5. Soda Can Base Styles
Add the base styles for the soda can elements:

```css
.product .soda{
    position: absolute;
    bottom: 0;
    left: calc(50%);
    transform: translateX(-50%);
}

.soda{
    --left: 0px;
    background: 
        var(--url) var(--left),
        url(soda.png) 0 0;
    background-size: auto 100%;
    width: 280px;
    aspect-ratio: 2 / 4.08;
    background-blend-mode: multiply;
    transition: 0.8s;
    mask-image: url(soda.png);
    mask-size: auto 100%;
}
```
Explanation:

- The first rule positions each soda can absolutely at the bottom center of the product container
- `-left: 0px` defines a CSS variable that will be animated later
- The background uses two images:
    1. `var(--url)` - the custom property set in HTML (either 1.png or 2.png)
    2. `url(soda.png)` - a mask/shape that defines the can's outline
- `background-size: auto 100%` maintains the aspect ratio of the background images
- `width: 280px` sets the can width
- `aspect-ratio: 2 / 4.08` defines the proportion of the can
- `background-blend-mode: multiply` blends the two background images together
- `transition: 0.8s` adds smooth animation
- `mask-image: url(soda.png)` uses the soda.png as a mask to create the can shape
- `mask-size: auto 100%` ensures the mask fits properly
---
### 6. Initial State for Second Can
Add styles to hide the second soda can initially:

```css
.soda:nth-child(2){
    opacity: 0;
}
```
Explanation:

- Targets the second soda can element
- `opacity: 0` makes it completely transparent initially
---
### 7. Hover Effects
Add the hover effects that create the rotation animation:

```css
.product:hover{
    bottom: 100px;
}

.product:hover .soda:nth-child(2){
    opacity: 1;
    --left: 500px;
}

.product:hover .soda:nth-child(1){
    opacity: 0;
    --left: 500px;
}
```
Explanation:

- `product:hover` moves the entire product container 100px upward when hovered
- `product:hover .soda:nth-child(2)` targets the second can on hover:
- `opacity: 1` makes it fully visible
- `--left: 500px` shifts the background position, creating the rotation effect
- `product:hover .soda:nth-child(1)` targets the first can on hover:
- `opacity: 0` makes it transparent
- `--left: 500px` shifts its background position as well
---
### Key Concepts Explored
1. CSS Custom Properties (Variables)
    - Using `--url` and `--left` variables to control styling
    - Setting variables inline in HTML and using them in CSS

2. Advanced Background Techniques
    - Multiple background images on a single element
    - Background blend modes to combine images
    - Background position animation

3. CSS Masking
    - Using `mask-image` to create complex shapes
    - Controlling mask size and position

4. CSS Transitions and Animations
    - Smooth transitions between states
    - Coordinated animations across multiple elements

5. Positioning
    - Absolute positioning for precise control
    - Centering techniques using transform
    - `Z-index` for layering

### Customization Ideas
1. Adjust the rotation speed: Change the transition duration values
2. Modify the hover movement: Change the bottom value in the hover state
3. Try different blend modes: Experiment with other blend modes like screen, overlay, etc.
4. Add more can states: Create additional divs for a smoother rotation sequence
5. Change the can size: Adjust the width and aspect-ratio properties

---

### Conclusion
This rotating soda can effect demonstrates how CSS can create impressive animations without JavaScript. The techniques shown here,CSS variables, masking, blend modes, and transitions can be applied to create various interactive product displays and visual effects.