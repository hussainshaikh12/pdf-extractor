## pdf-extractor
Simple PDF extractor using opencv and tesseract 
View Demo here 👉
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=A_1_a4SE4ng)
## Table of Contents
- [pdf-extractor](#pdf-extractor)
- [Table of Contents](#table-of-contents)
- [Docker Setup](#docker-setup)
- [Create Virtual environment](#create-virtual-environment)
- [Built with](#built-with)
- [What I learned](#what-i-learned)
- [Chalenges](#chalenges)
- [Continued development](#continued-development)
- [Author](#author)
## Docker Setup
To Start up a postgre db and django container 
Quickly run the project using 
```bash
docker-compose up -d --build
```
This should be executed for migrations
```bash
docker-compose exec web python manage.py migrate
```
## Create Virtual environment

After cloning the repo you need to create a Virtual environment using the following command and install django for working with the examples.

First install virtualenv package globally

```bash
pip install virtualenv
```
Open cli in the folder of the cloned repo and then create env
```bash
virtualenv env
```
To activate the env (For windows, For other OS you can easily google)
```bash
env\Scripts\activate
```
Then insatll requirements 
```bash
pip install -r requirements.txt
```
Start the local setup using
```bash
python manage.py runserver
```

## Built with
- [Django](https://www.djangoproject.com/) - High-level Python web framework
- Bootstrap
- HTML5 and CSS
- Tesseract OCR and OpenCV
- pypdfium2


## What I learned

I am using this section to recap over some of my major learnings while working through this project. I feel writing these out and providing code samples of areas I want to highlight is a great way to reinforce my own knowledge.

- **Tesseract OCR**
  This is one of the best opensoure OCR tools. It needs a basic installation setup of the library along with its executable. 
  For the most basic use case you pass in the image to it and it returns the scanned text. 
  ```python
  # Simple use
  from pytesseract import pytesseract
  text = pytesseract.image_to_string(img)
  ```
  But this usually does not take into account the specific type of image you are scanning so you need to provide the language and psms(more on this below)
  ```python
  custom_config = r'--oem 3 --psm 4'
  text = pytesseract.image_to_string(img, config=custom_config,lang='eng')
  ```
  - **PSMs (Page segmentation modes)**
    These have a major impact on the accuracy of the OCR. 
    > By default Tesseract expects a page of text when it segments an image. If you’re just seeking to OCR a small region, try a different segmentation mode - Tesseract documentation.
    
    There are 14 PSMs in Tesseract
    I made use of --psm 4 which is used when you need to OCR column data (e.g., the data you would find in a spreadsheet, table, or receipt)

- **pypdfium2**
  This was one of the easiest library i found out to setup and convert pdfs to images. It returns Pillow image. 
  ```python
  pdf = pdfium.PdfDocument(path)
  page = pdf.get_page(0)
  img = page.render_to(pdfium.BitmapConv.pil_image)
  ```
- **OpenCV**
  Image pre-processing is a very important step in improving the scan accuracy. Rescaling is a technique used to increase the pixel density of the image as Tesseract works best with images with higher dpi. 
  
  So here using opencv i performed rescaling. here fx and fy are the scaling factor and INTER_CUBIC is used to scale the image to larger size.  
  ```python
  img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
  ```
## Chalenges
The project is not too complex and it has a simple auth setup and basic templates and views to upload the documents and test. The main feature of scanning the document and their accuracy is the tough part. For learning that I had to go to look at multiple places to figure out what and how im supposed to use the Tesseract library. Then I also doubted my descision on choosing it as keras-ocr was also looking good. I even did the image preprocessing using OpenCV but it was not working and i was getting all gibberish text and then i learnt that Tesseract by default performs a bunch of preprocessing and i was overdoing it. 

## Continued development

I am using this section to outline areas that I want to continue focusing on in future for this project. 

**Tasks To Do**
- [ ] Drag and drop for document upload
- [ ] Adding more image preprocessing

## Author

- Profile - [Hussain Shaikh](https://www.linkedin.com/in/hussainshk/)
- Twitter - [@HussainSk2001](https://twitter.com/HussainSk2001)


