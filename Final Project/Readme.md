# HybridNet: Multi-Label Image Classification with CNN-RNN

## Project Overview
HybridNet is a unified framework designed to perform multi-label image classification by combining Convolutional Neural Networks (CNNs) for feature extraction with Recurrent Neural Networks (RNNs) for modeling label dependencies. This approach allows the model to predict multiple labels for a single image, capturing both the visual content and relationships between different labels.

This project focuses on multi-label classification rather than caption generation. It predicts labels such as objects, actions, and attributes within an image.

## Key Features
- Combines CNNs for extracting image features with RNNs for understanding label dependencies.
- Trained and evaluated on the COCO dataset, which contains over 82,000 training images and 40,000 validation images.
- Achieves superior performance compared to traditional multi-label classification models by learning joint image-label embeddings.

## Requirements
To run this project, the following dependencies are required:

- Python 3.6 or higher
- PyTorch 1.6.0 or higher
- torchvision 0.7.0 or higher
- numpy 1.18.1 or higher
- scikit-image 0.16.2 or higher
- scipy 1.5.2 or higher
- nltk 3.4.5 or higher

You can install these dependencies by running:

```bash
pip install -r requirements.txt
Dataset
This model is trained and tested on the COCO dataset, which contains images annotated with multiple labels across 80 categories. You can download the dataset from the official COCO dataset website.

How to Run the Project
Clone the Repository<br>
git clone https://github.com/muhammadzain21/BWT-ML-DL.git
Prepare the Data
Download and preprocess the COCO dataset. Ensure that the images and annotations are stored in the data/images/ and data/annotations/ directories, respectively.

Train the Model
Run the training script with the following command:

bash
Copy code
python train.py --image_path data/images/img.jpg --vocab_path data/vocab.pkl --batch_size 256 --learning_rate 0.001 --num_epochs 10 --num_workers 4
Evaluate the Model
After training, you can evaluate the model on the validation set. The results will be printed to the console and saved to a log file for further analysis.

Model Architecture
The model architecture consists of two main components:

CNN: Extracts features from the input image.
RNN: Learns joint image-label embeddings to understand label dependencies and image-label relevance.
The model implementation can be found in the model.py file.

Results
The model's performance is evaluated on the COCO dataset, and results are printed to the console. The results include metrics such as accuracy, precision, and recall for the multi-label classification task.
