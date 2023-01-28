# wind-speed-satellite-images

# Built With
The code uses the following libraries and frameworks:

1. google.colab

2. pathlib

3. os

4. pandas

5. numpy

6. PIL

7. seaborn

8. matplotlib

9. cv2



# Prerequisites

1. Google Colab environment


2. Google Drive account and the ability to mount it to the Colab environment


3. nasa-data1 dataset, including the train and test images, and the training_set_labels.csv file


4. python library : pathlib, os, pandas, numpy, PIL, seaborn, matplotlib, cv2

5. the datasets are here: https://drive.google.com/drive/folders/1SXjabKRFmVq-iI5Qe1fyDQgM5B15HBCX?usp=sharing


# Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project

2. Create your Feature Branch (git checkout -b feature/AmazingFeature)

3. Commit your Changes (git commit -m 'Add some AmazingFeature')

4. Push to the Branch (git push origin feature/AmazingFeature)

5. Open a Pull Request

# Contact

Shuvam Das - shuvamd210@gmail.com

# Small summary

This repository contains a Python script, "spatial_operations_on_images.py", that performs various spatial operations on satellite images, such as displaying and cropping images, and identifying their dimensions. The script utilizes several libraries, including cv2, matplotlib, numpy, pandas, and PIL. The script also uses the Google Colab environment and reads from a dataset located on Google Drive.

The script first mounts the Google Drive and sets the working directory to a specific folder containing the dataset. It then displays information about the dataset, such as the number of training and test images.

Next, the script reads in and displays several images from the dataset, and also prints their dimensions. The script also demonstrates how to crop images and compare the differences between them.

It is important to note that the script assumes that the dataset is already present in the specified Google Drive folder and that the user has the correct permissions to access it. The script also assumes that the necessary libraries have been installed.
