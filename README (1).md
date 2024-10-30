# Signboard Text Translation

### Project Overview
The Signboard Text Translation project aims to translate text found in signboards from English language to Hindi language. This project leverages computer vision and natural language processing to detect, extract, and translate text in images, making it accessible to users who may not understand the original language.

### Prerequisites
###### Language : Python
###### Libraries : OpenCV, Pytorch , Numpy, Pandas , Matplotlib

### Features
###### Text Detection: Identify text regions within images using OCR (Optical Character Recognition).
###### Text Extraction: Accurately extract detected text for translation processing.
###### Language Translation: Translate extracted text into the target language using NLP models.

### Dataset
For training and evaluating the translation model, we use a dataset containing English-Hindi text pairs, sourced from the NEWS2012RefEnHi1000.xml file. This dataset includes bilingual text references and is suitable for natural language translation tasks, especially for developing and fine-tuning Hindi-English translation models.

 ### Text Detection
##### Objective: Identify and locate areas within an image that contain text.
##### Process:
    1. This involves using computer vision techniques and Optical Character Recognition (OCR) tools, such as Tesseract, to detect regions where text appears on the signboard.
    2. These algorithms analyze the image for patterns that resemble text, considering elements like shapes, edges, and colors to discern text from the background.
    3. In the case of complex or noisy backgrounds (like signs with patterns or multiple colors), advanced image processing techniques (such as contour detection and image thresholding) may be applied to improve detection accuracy.

### Text Extraction
###### Objective: Convert the detected text regions into editable text that can be processed for translation.
###### Process:
    1. Once the text regions are identified, OCR tools like Tesseract are used to extract the actual text characters from those regions.
    2. This step may include language selection for OCR to enhance accuracy, as OCR engines often perform better when they know the language of the text.
    3. Post-processing steps, such as noise removal and spell-checking, may be applied to ensure that the extracted text is accurate, especially if the initial OCR results contain artifacts or errors from poor image quality.

### Language Translation:
###### Objective : Convert the detected English text into Hindi Text.
###### Process :
    1. Firstly I have used RNN Neural Network since it is a sequence Learning Problem.
    2. Since RNN Neural Network was not giving good accuracy I have used LSTM Nural Network which was giving slightly better accuracy than RNN Network.
    3. Nextly I have used a special form of LSTM that is GRU.
    4. Further in GRU Network I have used Attention Mechanism along with some Hyperparameter Tuning by changing the learning rate and number of epochs which was giving the best accuracy among all the previous models.

### Conclusion
The Signboard Text Translation project offers a practical solution for translating signboard text from one language to another, making essential information more accessible to a wider audience. By integrating computer vision and natural language processing techniques, this project streamlines the process from detecting text in images to translating it and displaying the output seamlessly. This tool has valuable applications for travelers, language learners, and accessibility-focused solutions. Future enhancements, such as supporting more languages and refining text overlay quality, will further expand its usability and impact in real-world settings.


