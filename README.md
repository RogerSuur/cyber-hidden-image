## General

This is tool that finds the pgp key and location from this image

## Commands

### ./image -steg image.jpeg

finds public key from the medadata

### ./image -map image.jpeg

Searches the coordinates of taken picture

## Audit questions:

https://github.com/01-edu/public/tree/master/subjects/cybersecurity/inspector-image

### What does stenography mean?

Stenography is an old technique still used today of hiding data in such a way that should be concealed to observers.

### How some information can be hidden in normal files?

Information can be hidden by using pixel manipulation and LSB technique and changing least significant bits to contain secret data or
be hidden into files binary content with manipulating binary file.

### How this program works?

This program looks key and location from image file. It reads exif data and looks for gps information and
searches for public key block start.
