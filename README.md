## General

This is tool that finds the pgp key and location from this image

## Setup

1. Check if python3 is installed
   python3 --version
   If NOT(ubuntu):
   sudo apt update
   sudo apt install python3

## Commands

### ./image -steg image.jpeg

shows different options

### ./image -steg image.jpeg

Search adress and number associated with given name

## Audit questions:

https://github.com/01-edu/public/tree/master/subjects/cybersecurity/inspector-image

### What does stenography mean?

Stenography is an old technique of hiding data in such a way that should be concealed to humans.

### How some information can be hidden in normal files?

Information can be hidden by using LSB technique and changing least significant bits of an image to contain secret data but be not noticable or
be hidden into files binary content.

### How this program works?

This program looks key and location from image file. It reads exif data and looks for gps information and
searches for public key block start.
