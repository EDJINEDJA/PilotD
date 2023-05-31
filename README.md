# RESTfull API(PilotD)
<p align="center">
    <a href="https://www.python.org/doc/" alt="Python 3.7">
        <img src="https://img.shields.io/badge/python-v3.7+-blue.svg" />
    </a>
    <a href="https://github.com/EDJINEDJA/PilotX/blob/main/License" alt="Licence">
        <img src="https://img.shields.io/badge/license-MIT-yellow.svg" />
    </a>
    <a href="https://github.com/EDJINEDJA/PilotX/commits/main" alt="Commits">
        <img src="https://img.shields.io/github/last-commit/EDJINEDJA/PilotX/master" />
    </a>
    <a href="https://github.com/EDJINEDJA/PilotX" alt="Activity">
        <img src="https://img.shields.io/badge/contributions-welcome-orange.svg" />
    </a>
    <a href="https://github.com/EDJINEDJA/PilotX" alt="Web Status">
        <img src="https://img.shields.io/website?down_color=red&down_message=down&up_color=success&up_message=up&url=http%3A%2F%2Fmatthaythornthwaite.pythonanywhere.com%2F" />
    </a>
</p>

## Table of Contents

<!--ts-->
* [Aims of PilotX](#Aims)
* [What is ICD](#ICD)
* [Usage](#Usage)

<!--te-->

## OVERVIEW
PilotD is an open-source project with the purpose of providing a RESTfull API for clients to access descriptions of ICD-10 codes and compare them to ICD-9 codes in the healthcare domain.
Given a textual description of the disease, this API is able to propose to the user the corresponding ICD and its relationship with its ICD-9 and other features.

## What is ICD
The ICD is the International Classification of Diseases, which doctors use to classify patients' problems according to their symptoms. As new types of disease emerge, disease classification tools are updated. There are several types of disease classification tools: ICD-9, ICD-10, and so on. It's important to distinguish between them, and to establish the right relationship between them. PilotX has been designed to address these issues.

## Usage
#### Install
- git clone 

Clone this repository in the main folder of your project to use PilotD
```bash
$ git clone https://github.com/EDJINEDJA/PilotD.git
```
- requirements

The toolkit support Python 3.10.6 

To install required packages use:

```bash
$ pip3 install -r requirements.txt
```
- run server (Uvicorn)
```bash
$ make run
```