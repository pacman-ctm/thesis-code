# Thesis of Pham Anh Cuong  
This is the source code that is used in the graduation thesis of Pham Anh Cuong (ID 19020038) of VNU University of Engineering and Technology for 2023 Spring Semester.

### About the folders:

- Data_making: About the code for creating image captioning dataset. 
- Train: About the training phase code. (Update 2024: The v1, v2 version are added because there might be some bugs in the initial version, but you should use the GRIT model below for more accurate result).
- Inference: About the inference phase code (usually after getting the snapshot after the training phase). The v2 version contains some code to export captions to json files to evaluate.
- Simple_Evaluate: About the evaluation phase of the models.

### Some notes:
- In my humble opinion, because my contribution is mostly the dataset, the code might be bad from my point of view because I just want to test my dataset. I think you should create your own code (for the 2 first models I noted below) using the dataset :D, or follow the vicap branch of GRIT repository noted below.
- Because most of my code files are used in the Google Colab platform, there might be some conflict if you clone this one, what you need to do is change the path in the source code and move the respective files to the correct directory as in the source code.

### About the models:
For my graduation thesis, I use three models with its architecture as follows:
- Model using **ResNet101** for feature extracting and **LSTM** for caption generating.
- Model using **Vision Transformer** for feature extracting and **Transformer Decoder** for caption generating.
- Model-based on the **GRIT** model [Arxiv](https://arxiv.org/abs/2207.09666), however, due to the lack of hardware condition, the code for this modification is available at the [vicap branch](https://github.com/davidnvq/grit/tree/vicap) in the source code repository of GRIT.